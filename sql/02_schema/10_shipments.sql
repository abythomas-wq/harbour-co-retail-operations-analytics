-- =====================================================
-- Harbour & Co. Retail Operations Analytics
-- Shipments Table
-- =====================================================

USE harbour_co_retail_analytics;

CREATE TABLE IF NOT EXISTS shipments (
    shipment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    warehouse_id INT NOT NULL,
    shipment_date DATE NOT NULL,
    expected_delivery_date DATE,
    actual_delivery_date DATE,
    shipment_status VARCHAR(30) NOT NULL,
    delivery_method VARCHAR(50),

    CONSTRAINT fk_shipments_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_shipments_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES warehouses(warehouse_id)
);