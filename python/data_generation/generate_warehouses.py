"""
Harbour & Co. Retail Operations Analytics
Warehouse Data Generator

Generates warehouse records linked to locations table.
"""

import pandas as pd
from faker import Faker
import random


fake = Faker("en_GB")


# -----------------------------------------------------
# Load Locations Master Data
# -----------------------------------------------------

locations = pd.read_csv(
    "data/raw/locations.csv"
)


# Filter warehouse locations only

warehouse_locations = locations[
    locations["location_type"] == "Warehouse"
]


warehouses = []


# -----------------------------------------------------
# Generate Warehouse Records
# -----------------------------------------------------

warehouse_types = [
    "Distribution Centre",
    "Fulfilment Centre"
]


for _, location in warehouse_locations.iterrows():

    warehouses.append(
        {
            "location_id": location["location_id"],
            "warehouse_name": location["location_name"],
            "warehouse_type": random.choice(
                warehouse_types
            ),
            "capacity_units": random.randint(
                100000,
                500000
            ),
            "operational_status": "Active",
            "opening_date": fake.date_between(
                start_date="-10y",
                end_date="-1y"
            )
        }
    )


# -----------------------------------------------------
# Export CSV
# -----------------------------------------------------

df = pd.DataFrame(warehouses)


df.to_csv(
    "data/raw/warehouses.csv",
    index=False
)


print("Warehouses dataset generated successfully.")
print(df.head())
print(f"Total warehouses generated: {len(df)}")