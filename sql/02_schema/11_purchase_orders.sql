-- =====================================================
-- Harbour & Co. Retail Operations Analytics
-- Purchase Orders Table
-- =====================================================

USE harbour_co_retail_analytics;

CREATE TABLE IF NOT EXISTS purchase_orders (
    purchase_order_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_id INT NOT NULL,
    product_id INT NOT NULL,
    order_date DATE NOT NULL,
    expected_delivery_date DATE,
    actual_delivery_date DATE,
    quantity_ordered INT NOT NULL,
    purchase_order_status VARCHAR(30) NOT NULL,
    unit_cost DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_purchase_orders_supplier
        FOREIGN KEY (supplier_id)
        REFERENCES suppliers(supplier_id),

    CONSTRAINT fk_purchase_orders_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

describe purchase_orders;

SHOW CREATE TABLE purchase_orders;








