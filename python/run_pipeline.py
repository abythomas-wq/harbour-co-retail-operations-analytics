#!/bin/bash

echo "🚀 Starting SwiftFulfil full pipeline..."

# -------------------------
# 1. Run Python generator
# -------------------------
echo "📦 Generating datasets..."
python3 python/generate_data.py

if [ $? -ne 0 ]; then
    echo "❌ Python script failed. Stopping pipeline."
    exit 1
fi

# -------------------------
# 2. Reload MySQL
# -------------------------
echo "🗄️ Reloading MySQL tables..."

mysql --local-infile=1 -u root -p swiftfulfil <<EOF

TRUNCATE TABLE order_items;
TRUNCATE TABLE orders;
TRUNCATE TABLE shipments;

-- IMPORTANT: adjust paths if needed
LOAD DATA LOCAL INFILE '$(pwd)/data/customers.csv'
INTO TABLE customers
FIELDS TERMINATED BY ',' 
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '$(pwd)/data/products.csv'
INTO TABLE products
FIELDS TERMINATED BY ',' 
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '$(pwd)/data/orders.csv'
INTO TABLE orders
FIELDS TERMINATED BY ',' 
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '$(pwd)/data/order_items.csv'
INTO TABLE order_items
FIELDS TERMINATED BY ',' 
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '$(pwd)/data/shipments.csv'
INTO TABLE shipments
FIELDS TERMINATED BY ',' 
IGNORE 1 ROWS;

EOF

echo "📊 Verifying counts..."

mysql -u root -p swiftfulfil -e "
SELECT 'orders' AS tbl, COUNT(*) FROM orders
UNION ALL
SELECT 'order_items', COUNT(*) FROM order_items;
"

echo "✅ Pipeline completed successfully!"
