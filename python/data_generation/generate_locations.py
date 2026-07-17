import pandas as pd
"""
Harbour & Co. Retail Operations Analytics
Location Data Generator

Generates operational locations including:
- Retail stores
- Distribution centres
"""

import random
from faker import Faker

random.seed(42)
Faker.seed(42)

fake = Faker("en_GB")

locations = []

# -----------------------------------------------------
# Retail Store Locations (60)
# -----------------------------------------------------

store_locations = [
    ("London Oxford Street", "London", "London"),
    ("Manchester Arndale", "Manchester", "North West"),
    ("Birmingham Bullring", "Birmingham", "West Midlands"),
    ("Leeds Trinity", "Leeds", "Yorkshire"),
    ("Glasgow Buchanan Street", "Glasgow", "Scotland"),
    ("Bristol Cabot Circus", "Bristol", "South West"),
    ("Liverpool ONE", "Liverpool", "North West"),
    ("Edinburgh Princes Street", "Edinburgh", "Scotland"),
    ("Cardiff St David's", "Cardiff", "Wales"),
    ("Nottingham Victoria Centre", "Nottingham", "East Midlands")
]

# Expand locations to 60 stores
for i in range(60):
    if i < len(store_locations):
        name, city, region = store_locations[i]
    else:
        city = fake.city()
        region = random.choice(
            [
                "London",
                "South East",
                "South West",
                "North West",
                "North East",
                "Midlands",
                "Scotland",
                "Wales"
            ]
        )
        name = f"Harbour & Co. {city}"

    locations.append(
        {
            "location_id": len(locations) + 1,
            "location_name": name,
            "location_type": "Store",
            "address": fake.street_address().replace("\n", ", "),
            "city": city,
            "region": region,
            "postcode": fake.postcode(),
            "operational_status": "Active",
            "opening_date": fake.date_between(
                start_date="-15y",
                end_date="-1y"
            )
        }
    )


# -----------------------------------------------------
# Distribution Centres (3)
# -----------------------------------------------------

warehouses = [
    ("Midlands Distribution Centre", "Birmingham", "West Midlands"),
    ("Northern Distribution Centre", "Leeds", "Yorkshire"),
    ("Southern Distribution Centre", "Reading", "South East")
]


for name, city, region in warehouses:
    locations.append(
        {
            "location_id": len(locations) + 1,
            "location_name": name,
            "location_type": "Warehouse",
            "address": fake.street_address().replace("\n", ", "),
            "city": city,
            "region": region,
            "postcode": fake.postcode(),
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

df = pd.DataFrame(locations)

df.to_csv(
    "data/raw/locations.csv",
    index=False
)

print("Locations dataset generated successfully.")
print(df.head())
print(f"Total locations generated: {len(df)}")