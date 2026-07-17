-- =====================================================
-- Harbour & Co. Retail Operations Analytics
-- Customers Table
-- =====================================================

USE harbour_co_retail_analytics;

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    postcode_area VARCHAR(20),
    customer_segment VARCHAR(50),
    loyalty_status VARCHAR(50),
    acquisition_channel VARCHAR(50),
    registration_date DATE
);