"""
Harbour & Co. Retail Operations Analytics

Inventory Data Generator

Generates inventory snapshots linked to:
- products
- locations

Matches MySQL inventory table:

inventory_id
product_id
location_id
inventory_date
quantity_available
quantity_reserved
quantity_damaged
reorder_level
"""

import pandas as pd
import random
from faker import Faker
from datetime import date


fake = Faker("en_GB")


# -----------------------------------------------------
# Configuration
# -----------------------------------------------------

products_file = "data/raw/products.csv"
locations_file = "data/raw/locations.csv"

output_file = "data/raw/inventory.csv"


# -----------------------------------------------------
# Load Data
# -----------------------------------------------------

products = pd.read_csv(products_file)

locations = pd.read_csv(locations_file)


inventory = []

inventory_id = 1


# -----------------------------------------------------
# Inventory Logic Functions
# -----------------------------------------------------

def generate_quantity(product_status, location_type):

    if product_status == "Active":

        if location_type == "Warehouse":
            return random.randint(500, 5000)

        else:
            return random.randint(5, 300)

    else:
        # Discontinued products

        if location_type == "Warehouse":
            return random.randint(0, 500)

        else:
            return random.randint(0, 50)



def generate_reorder_level(location_type):

    if location_type == "Warehouse":
        return random.randint(100, 1000)

    else:
        return random.randint(10, 75)



def generate_reserved_stock(quantity_available):

    if quantity_available == 0:
        return 0

    return random.randint(
        0,
        max(1, int(quantity_available * 0.10))
    )



def generate_damaged_stock(quantity_available):

    if quantity_available == 0:
        return 0

    return random.randint(
        0,
        max(1, int(quantity_available * 0.03))
    )



# -----------------------------------------------------
# Generate Inventory
# -----------------------------------------------------

for _, location in locations.iterrows():

    location_products = products.sample(
        n=(
            len(products)
            if location["location_type"] == "Warehouse"
            else random.randint(300, 700)
        )
    )


    for _, product in location_products.iterrows():

        quantity_available = generate_quantity(
            product["product_status"],
            location["location_type"]
        )


        inventory.append(
            {
                "inventory_id": inventory_id,

                "product_id": product["product_id"],

                "location_id": location["location_id"],

                "inventory_date": fake.date_between(
                    start_date="-30d",
                    end_date="today"
                ),

                "quantity_available": quantity_available,

                "quantity_reserved": generate_reserved_stock(
                    quantity_available
                ),

                "quantity_damaged": generate_damaged_stock(
                    quantity_available
                ),

                "reorder_level": generate_reorder_level(
                    location["location_type"]
                )
            }
        )

        inventory_id += 1



# -----------------------------------------------------
# Export CSV
# -----------------------------------------------------

df = pd.DataFrame(inventory)


df.to_csv(
    output_file,
    index=False
)


print("Inventory dataset generated successfully.")

print(df.head())

print(
    f"Total inventory records generated: {len(df)}"
)


# -----------------------------------------------------
# Validation
# -----------------------------------------------------

print("\nValidation Checks")

print(
    "Valid product references:",
    df["product_id"].isin(
        products["product_id"]
    ).all()
)


print(
    "Valid location references:",
    df["location_id"].isin(
        locations["location_id"]
    ).all()
)


print(
    "\nQuantity validation:"
)

print(
    "Negative quantities:",
    (
        df[
            [
                "quantity_available",
                "quantity_reserved",
                "quantity_damaged"
            ]
        ] < 0
    ).any().any()
)