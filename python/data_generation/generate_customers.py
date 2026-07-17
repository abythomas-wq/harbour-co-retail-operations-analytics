"""
Harbour & Co. Retail Operations Analytics

Customer Data Generator

Generates customer master data for omnichannel retail analytics.
"""


import pandas as pd
import random
from faker import Faker
from pathlib import Path


fake = Faker("en_GB")


# -----------------------------------------------------
# Configuration
# -----------------------------------------------------

TOTAL_CUSTOMERS = 50000


# -----------------------------------------------------
# UK Postcode Area Logic
# -----------------------------------------------------

postcode_areas = [
    "E",
    "N",
    "NW",
    "SE",
    "SW",
    "W",
    "M",
    "B",
    "LS",
    "G",
    "BS",
    "L",
    "EH",
    "S",
    "NE"
]


# -----------------------------------------------------
# Customer Segmentation
# -----------------------------------------------------

customer_segments = [
    "Regular"
] * 55 + [
    "Premium"
] * 15 + [
    "Occasional"
] * 30


# -----------------------------------------------------
# Loyalty Programme
# -----------------------------------------------------

loyalty_statuses = [
    "No Membership",
    "No Membership",
    "Bronze",
    "Bronze",
    "Bronze",
    "Bronze",
    "Silver",
    "Silver",
    "Silver",
    "Gold"
]

# -----------------------------------------------------
# Acquisition Channels
# -----------------------------------------------------

acquisition_channels = [
    "Website",
    "Website",
    "Website",
    "Store",
    "Store",
    "Social Media",
    "Social Media",
    "Email Marketing",
    "Referral",
    "Marketplace"
]


# -----------------------------------------------------
# Generate Customers
# -----------------------------------------------------

customers = []


for customer_id in range(1, TOTAL_CUSTOMERS + 1):


    first_name = fake.first_name()
    last_name = fake.last_name()


    customers.append(
        {

            "customer_id": customer_id,

            "first_name": first_name,

            "last_name": last_name,

            "email": (
                f"{first_name.lower()}."
                f"{last_name.lower()}"
                f"{customer_id}"
                "@example.com"
            ),

            "postcode_area": random.choice(
                postcode_areas
            ),

            "customer_segment": random.choice(
                customer_segments
            ),

            "loyalty_status": random.choice(
                loyalty_statuses
            )if random.random() > 0.2 else "No Membership",

            "acquisition_channel": random.choice(
                acquisition_channels
            ),

            "registration_date": fake.date_between(
                start_date="-14y",
                end_date="-1m"
            )

        }
    )


# -----------------------------------------------------
# Export CSV
# -----------------------------------------------------

df = pd.DataFrame(customers)

output_file = Path("data/raw/customers.csv")

if output_file.exists():
    output_file.unlink()

df.to_csv(
    output_file,
    index=False
)

print("Customers dataset generated successfully.")
print(df.head())
print(f"Total customers generated: {len(df)}")