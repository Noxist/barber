# Barber booking source snapshot

This is a cleaned source snapshot with a new history. It is not the production Pompadour Booker deployment. Customer information is not included: configure `BARBERLY_CUSTOMER_ID`, `BARBER_CUSTOMER_FIRST_NAME`, `BARBER_CUSTOMER_LAST_NAME`, `BARBER_CUSTOMER_EMAIL` and `BARBER_CUSTOMER_PHONE` through the deployment's restricted configuration. Booking and customer history operations fail closed if required information is absent. Do not commit customer information or credentials.

This historical project can create real bookings and scheduled jobs. Do not run live booking or cancellation tests without separate explicit authorization.
