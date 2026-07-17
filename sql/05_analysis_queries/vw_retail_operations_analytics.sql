CREATE OR REPLACE VIEW vw_retail_operations_analytics AS

WITH inventory_summary AS (
    SELECT
        product_id,
        SUM(quantity_available) AS total_available_stock,
        SUM(quantity_reserved) AS total_reserved_stock,
        SUM(quantity_damaged) AS total_damaged_stock,
        COUNT(DISTINCT location_id) AS stock_locations
    FROM inventory_snapshots
    GROUP BY product_id
),

procurement_summary AS (
    SELECT
        product_id,
        COUNT(purchase_order_id) AS total_purchase_orders,
        AVG(unit_cost) AS average_unit_cost,
        AVG(
            DATEDIFF(
                actual_delivery_date,
                order_date
            )
        ) AS average_supplier_lead_time
    FROM purchase_orders
    GROUP BY product_id
),

shipment_summary AS (

    SELECT
        order_id,
        shipment_status,
        delivery_method,
        DATEDIFF(
            actual_delivery_date,
            shipment_date
        ) AS delivery_days,
        DATEDIFF(
            actual_delivery_date,
            expected_delivery_date
        ) AS delivery_delay_days,
        CASE
            WHEN actual_delivery_date IS NULL THEN 'Pending'
            WHEN actual_delivery_date <= expected_delivery_date THEN 'On Time'
            ELSE 'Delayed'
        END AS delivery_performance
    FROM shipments
)
SELECT

/* Order Information */

o.order_id,
oi.order_item_id,
o.order_date,
YEAR(o.order_date) AS order_year,
MONTH(o.order_date) AS order_month,
o.sales_channel,
o.order_status,
o.payment_method,


/* Customer Information */

c.customer_id,
c.customer_segment,
c.loyalty_status,
c.acquisition_channel,


/* Product Information */

p.product_id,
p.product_name,
p.category,
p.sub_category,
p.product_status,


/* Sales Metrics */

oi.quantity,
oi.unit_price,
oi.discount_amount,
oi.line_total AS revenue,

(p.cost_price * oi.quantity) AS product_cost,
(
    oi.line_total -
    (p.cost_price * oi.quantity)
) AS gross_profit,


/* Inventory Metrics */

i.total_available_stock,
i.total_reserved_stock,
i.total_damaged_stock,
i.stock_locations,


CASE
    WHEN i.total_available_stock <= i.total_reserved_stock
    THEN 'Stock Risk'
    ELSE 'Available'
END AS inventory_health,


/* Procurement Metrics */

pr.total_purchase_orders,
pr.average_unit_cost,
pr.average_supplier_lead_time,

/* Shipment Metrics */

sh.shipment_status,
sh.delivery_method,
sh.delivery_days,
sh.delivery_delay_days,
sh.delivery_performance

FROM order_items oi
INNER JOIN orders o
ON oi.order_id = o.order_id
INNER JOIN customers c
ON o.customer_id = c.customer_id
INNER JOIN products p
ON oi.product_id = p.product_id
LEFT JOIN inventory_summary i
ON p.product_id = i.product_id
LEFT JOIN procurement_summary pr
ON p.product_id = pr.product_id
LEFT JOIN shipment_summary sh
ON o.order_id = sh.order_id;






