"""
Harbour & Co. Retail Operations Analytics
Store Data Generator

Generates retail store records linked to locations table.
"""

import pandas as pd
import random
from faker import Faker


fake = Faker("en_GB")


# -----------------------------------------------------
# Configuration
# -----------------------------------------------------

TOTAL_STORES = 60

store_types = [
    "Flagship",
    "Standard",
    "Outlet"
]

store_status = [
    "Active"
]


# -----------------------------------------------------
# Load Locations Master Data
# -----------------------------------------------------

locations = pd.read_csv(
    "data/raw/locations.csv"
)


# Filter only retail stores
store_locations = locations[
    locations["location_type"] == "Store"
]


stores = []


# -----------------------------------------------------
# Generate Store Records
# -----------------------------------------------------

for _, location in store_locations.iterrows():

    stores.append(
        {
            "store_id": len(stores) + 1,
            "location_id": location["location_id"],
            "store_name": f"Harbour & Co. {location['location_name']}",
            "store_type": random.choice(store_types),
            "opening_date": fake.date_between(
                start_date="-15y",
                end_date="-1y"
            ),
            "store_size_sqft": random.randint(
                3000,
                25000
            ),
            "store_status": random.choice(store_status)
        }
    )

# -----------------------------------------------------
# Export CSV
# -----------------------------------------------------

df = pd.DataFrame(stores)

df.to_csv(
    "data/raw/stores.csv",
    index=False
)


print("Stores dataset generated successfully.")
print(df.head())
print(f"Total stores generated: {len(df)}")