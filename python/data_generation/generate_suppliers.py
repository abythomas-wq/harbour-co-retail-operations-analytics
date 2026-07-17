import pandas as pd
"""
Harbour & Co. Retail Operations Analytics
Supplier Data Generator

Generates supplier master data.
"""

import random
from faker import Faker

random.seed(42)
Faker.seed(42)

fake = Faker("en_GB")


# -----------------------------------------------------
# Configuration
# -----------------------------------------------------

TOTAL_SUPPLIERS = 250


suppliers = []


supplier_categories = [
    "Fashion",
    "Home",
    "Lifestyle",
    "Beauty",
    "Consumer Goods"
]

supplier_region_countries = {
    "UK": [
        "United Kingdom"
    ],
    "Europe": [
        "France",
        "Germany",
        "Italy",
        "Spain",
        "Portugal",
        "Netherlands"
    ],
    "Asia": [
        "China",
        "India",
        "Vietnam",
        "Bangladesh",
        "Japan",
        "South Korea"
    ],
    "North America": [
        "United States",
        "Canada",
        "Mexico"
    ]
}

supplier_statuses = [
    "Active",
    "Active",
    "Active",
    "Inactive"
]


# -----------------------------------------------------
# Generate Supplier Records
# -----------------------------------------------------
for supplier_id in range(1, TOTAL_SUPPLIERS + 1):

    selected_region = random.choice(
        list(supplier_region_countries.keys())
    )

    suppliers.append(
        {
            "supplier_id": supplier_id,
            "supplier_name": f"{fake.company()} Ltd",
            "supplier_region": selected_region,
            "supplier_category": random.choice(
                supplier_categories
            ),
            "contact_country": random.choice(
                supplier_region_countries[selected_region]
            ),
            "contract_start_date": fake.date_between(
                start_date="-10y",
                end_date="-1y"
            ),
            "supplier_status": random.choice(
                supplier_statuses
            )
        }
    )


# -----------------------------------------------------
# Export CSV
# -----------------------------------------------------

df = pd.DataFrame(suppliers)


df.to_csv(
    "data/raw/suppliers.csv",
    index=False
)


print("Suppliers dataset generated successfully.")
print(df.head())
print(f"Total suppliers generated: {len(df)}")