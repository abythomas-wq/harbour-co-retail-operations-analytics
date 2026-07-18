CREATE OR REPLACE VIEW vw_project_horizon_dashboard AS

SELECT
/* Date Dimension */
order_year,
order_quarter,
order_month,
order_month_name,
/* Commercial Metrics */
sales_channel,
COUNT(DISTINCT order_id) AS total_orders,
SUM(quantity) AS units_sold,
SUM(revenue) AS total_revenue,
SUM(gross_profit) AS total_profit,
ROUND(
SUM(gross_profit) /
NULLIF(SUM(revenue),0) * 100,
2
) AS gross_margin_pct,
ROUND(
SUM(revenue) /
COUNT(DISTINCT order_id),
2
) AS average_order_value,
/* Product Dimension */
category,
sub_category,
/* Customer Dimension */
customer_segment,
loyalty_status,
/* Inventory Metrics */
SUM(total_available_stock) AS available_stock,
SUM(total_reserved_stock) AS reserved_stock,
SUM(total_damaged_stock) AS damaged_stock,
/* Procurement Metrics */
AVG(average_supplier_lead_time)
AS avg_supplier_lead_time,
AVG(average_unit_cost)
AS avg_unit_cost,
/* Fulfilment Metrics */
COUNT(
DISTINCT
CASE
WHEN delivery_performance = 'On Time'
THEN order_id
END
) AS on_time_orders,
COUNT(
DISTINCT
CASE
WHEN delivery_performance = 'Delayed'
THEN order_id
END
) AS delayed_orders,
ROUND(
AVG(delivery_days),
2
) AS average_delivery_days
FROM vw_retail_operations_analytics
GROUP BY
order_year,
order_quarter,
order_month,
order_month_name,
sales_channel,
category,
sub_category,
customer_segment,
loyalty_status;