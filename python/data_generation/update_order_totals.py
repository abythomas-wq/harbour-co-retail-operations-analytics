import pandas as pd
from pathlib import Path
import random
from faker import Faker

random.seed(42)
Faker.seed(42)

fake = Faker("en_GB")

orders = pd.read_csv(
    "data/raw/orders.csv"
)

order_items = pd.read_csv(
    "data/raw/order_items.csv"
)


order_totals = (
    order_items
    .groupby("order_id")["line_total"]
    .sum()
    .round(2)
)


orders["total_order_value"] = (
    orders["order_id"]
    .map(order_totals)
)


orders["total_order_value"] = (
    orders["total_order_value"]
    .fillna(0)
)


orders.to_csv(
    "data/raw/orders.csv",
    index=False
)


print("Order totals updated successfully.")
print(orders.head())