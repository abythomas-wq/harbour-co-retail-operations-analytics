CREATE TABLE business_performance_history (

    financial_year VARCHAR(10) PRIMARY KEY,

    revenue DECIMAL(12,2),

    gross_margin_pct DECIMAL(5,2),

    gross_profit DECIMAL(12,2)

);

INSERT INTO business_performance_history
(
financial_year,
revenue,
gross_margin_pct,
gross_profit
)

VALUES

('FY2023',238500000,42.80,102078000),

('FY2024',260400000,44.50,115878000),

('FY2025',281911937.13,46.95,132371488.87);

SELECT *
FROM business_performance_history;