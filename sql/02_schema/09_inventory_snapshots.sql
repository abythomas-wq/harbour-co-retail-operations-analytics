-- =====================================================
-- Harbour & Co. Retail Operations Analytics
-- Inventory Snapshots Table
-- =====================================================

USE harbour_co_retail_analytics;

CREATE TABLE IF NOT EXISTS inventory_snapshots (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    location_id INT NOT NULL,
    inventory_date DATE NOT NULL,
    quantity_available INT NOT NULL,
    quantity_reserved INT DEFAULT 0,
    quantity_damaged INT DEFAULT 0,
    reorder_level INT,

    CONSTRAINT fk_inventory_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id),

    CONSTRAINT fk_inventory_location
        FOREIGN KEY (location_id)
        REFERENCES locations(location_id)
);