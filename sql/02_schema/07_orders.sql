-- =====================================================
-- Harbour & Co. Retail Operations Analytics
-- Orders Table
-- =====================================================

USE harbour_co_retail_analytics;

CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    store_id INT,
    order_date DATE NOT NULL,
    sales_channel VARCHAR(50) NOT NULL,
    order_status VARCHAR(30) NOT NULL,
    payment_method VARCHAR(30),
    total_order_value DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_orders_store
        FOREIGN KEY (store_id)
        REFERENCES stores(store_id)
);

SELECT COUNT(*) FROM orders;