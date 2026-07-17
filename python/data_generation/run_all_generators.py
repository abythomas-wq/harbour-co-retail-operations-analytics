import pandas as pd
import random
from faker import Faker


random.seed(42)
Faker.seed(42)

fake = Faker("en_GB")

import subprocess

scripts = [
    "generate_suppliers.py",
    "generate_products.py",
    "generate_customers.py",
    "generate_stores.py",
    "generate_warehouses.py",
    "generate_locations.py",
    "generate_orders.py",
    "generate_order_items.py",
    "update_order_totals.py",
    "generate_shipments.py",
    "generate_inventory.py",
    "generate_purchase_orders.py"
]

for script in scripts:
    print(f"Running {script}")
    subprocess.run(
        ["python3", f"python/data_generation/{script}"],
        check=True
    )

print("All datasets generated successfully.")