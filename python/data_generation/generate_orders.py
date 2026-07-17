"""
Harbour & Co. Retail Operations Analytics

Orders Data Generator

Generates customer order transactions linked to:
- Customers
- Stores

Business logic:
- Order frequency influenced by loyalty status
- Order dates occur after customer registration
- Every order is assigned a store
- Order value calculated later from order_items
"""


import pandas as pd
import random
from faker import Faker
from pathlib import Path

random.seed(42)
Faker.seed(42)

fake = Faker("en_GB")

# -----------------------------------------------------
# Reproducibility
# -----------------------------------------------------

random.seed(42)
Faker.seed(42)

fake = Faker("en_GB")


# -----------------------------------------------------
# Configuration
# -----------------------------------------------------

CUSTOMER_FILE = "data/raw/customers.csv"
STORE_FILE = "data/raw/stores.csv"

OUTPUT_FILE = Path("data/raw/orders.csv")


# -----------------------------------------------------
# Load Existing Data
# -----------------------------------------------------

customers = pd.read_csv(
    CUSTOMER_FILE,
    parse_dates=["registration_date"]
)

stores = pd.read_csv(
    STORE_FILE
)


# -----------------------------------------------------
# Order Frequency Logic
# -----------------------------------------------------

order_frequency = {

    "No Membership": {
        "min": 1,
        "max": 5
    },

    "Bronze": {
        "min": 2,
        "max": 8
    },

    "Silver": {
        "min": 5,
        "max": 15
    },

    "Gold": {
        "min": 8,
        "max": 25
    }
}


# -----------------------------------------------------
# Sales Channel Logic
# -----------------------------------------------------

sales_channels = [
    "Website",
    "Website",
    "Website",
    "Website",
    "Store",
    "Store",
    "Store",
    "Click & Collect",
    "Click & Collect",
    "Marketplace"
]


# -----------------------------------------------------
# Order Status Logic
# -----------------------------------------------------

order_statuses = [
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Shipped",
    "Processing",
    "Cancelled",
    "Returned"
]


# -----------------------------------------------------
# Payment Method Logic
# -----------------------------------------------------

payment_methods = [
    "Debit Card",
    "Debit Card",
    "Credit Card",
    "Credit Card",
    "Apple Pay",
    "PayPal",
    "Google Pay",
    "Gift Card"
]


# -----------------------------------------------------
# Generate Orders
# -----------------------------------------------------

orders = []

order_id = 1


for _, customer in customers.iterrows():

    loyalty = customer["loyalty_status"]

    order_range = order_frequency[loyalty]


    number_of_orders = random.randint(
        order_range["min"],
        order_range["max"]
    )


    for _ in range(number_of_orders):

        order_date = fake.date_between(
            start_date=customer["registration_date"],
            end_date="today"
        )


        sales_channel = random.choice(
            sales_channels
        )


        store_id = random.choice(
            stores["store_id"].tolist()
        )


        orders.append(
            {
                "order_id": order_id,
                "customer_id": customer["customer_id"],
                "store_id": store_id,
                "order_date": order_date,
                "sales_channel": sales_channel,
                "order_status": random.choice(
                    order_statuses
                ),
                "payment_method": random.choice(
                    payment_methods
                ),
                "total_order_value": 0
            }
        )


        order_id += 1


# -----------------------------------------------------
# Export CSV
# -----------------------------------------------------

df = pd.DataFrame(orders)


if OUTPUT_FILE.exists():
    OUTPUT_FILE.unlink()


df.to_csv(
    OUTPUT_FILE,
    index=False
)


# -----------------------------------------------------
# Validation Output
# -----------------------------------------------------

print("Orders dataset generated successfully.")
print(df.head())

print(
    f"Total orders generated: {len(df)}"
)

print(
    "\nSales Channel Distribution:"
)

print(
    df["sales_channel"].value_counts()
)