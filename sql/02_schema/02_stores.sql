-- =====================================================
-- Harbour & Co. Retail Operations Analytics
-- Stores Table
-- =====================================================

USE harbour_co_retail_analytics;

CREATE TABLE IF NOT EXISTS stores (
    store_id INT AUTO_INCREMENT PRIMARY KEY,
    location_id INT NOT NULL,
    store_name VARCHAR(100) NOT NULL,
    store_type VARCHAR(50) NOT NULL,
    opening_date DATE,
    store_size_sqft INT,
    store_status VARCHAR(20) NOT NULL,

    CONSTRAINT fk_stores_location
        FOREIGN KEY (location_id)
        REFERENCES locations(location_id)
);