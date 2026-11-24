import asyncio
import os
import tempfile
import unittest
from unittest.mock import patch

with tempfile.TemporaryDirectory() as temp:
    os.environ['BARBER_DATA_DIR'] = temp
    import barberly
    import scheduler

class CustomerConfigurationTests(unittest.TestCase):
    def test_missing_customer_does_not_book(self):
        with patch.object(scheduler, 'CUSTOMER_DEFAULT', {'customerId': '', 'firstName': '', 'lastName': '', 'email': '', 'phoneNumber': ''}), patch.object(scheduler, 'book_slot') as book:
            with self.assertRaises(ValueError):
                asyncio.run(scheduler._book_single_slot({}, None))
            book.assert_not_called()

    def test_missing_customer_id_does_not_fetch_history(self):
        with patch.object(barberly, 'CUSTOMER_ID', ''), patch.object(barberly.httpx, 'AsyncClient') as client:
            with self.assertRaises(ValueError):
                asyncio.run(barberly.fetch_booking_history())
            client.assert_not_called()
