-- =====================================================
-- Harbour & Co. Retail Operations Analytics
-- Locations Table
-- =====================================================

USE harbour_co_retail_analytics;

CREATE TABLE IF NOT EXISTS locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL,
    location_type VARCHAR(50) NOT NULL,
    address VARCHAR(150),
    city VARCHAR(50),
    region VARCHAR(50),
    postcode VARCHAR(20),
    operational_status VARCHAR(20) NOT NULL,
    opening_date DATE
);