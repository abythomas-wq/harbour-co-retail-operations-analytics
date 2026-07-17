-- =====================================================
-- Harbour & Co. Retail Operations Analytics
-- Warehouses Table
-- =====================================================

USE harbour_co_retail_analytics;

CREATE TABLE IF NOT EXISTS warehouses (
    warehouse_id INT AUTO_INCREMENT PRIMARY KEY,
    location_id INT NOT NULL,
    warehouse_name VARCHAR(100) NOT NULL,
    warehouse_type VARCHAR(50) NOT NULL,
    capacity_units INT,
    operational_status VARCHAR(20) NOT NULL,
    opening_date DATE,

    CONSTRAINT fk_warehouses_location
        FOREIGN KEY (location_id)
        REFERENCES locations(location_id)
);