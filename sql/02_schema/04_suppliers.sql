-- =====================================================
-- Harbour & Co. Retail Operations Analytics
-- Suppliers Table
-- =====================================================

USE harbour_co_retail_analytics;

CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    supplier_region VARCHAR(50),
    supplier_category VARCHAR(50),
    contact_country VARCHAR(50),
    contract_start_date DATE,
    supplier_status VARCHAR(20) NOT NULL
);