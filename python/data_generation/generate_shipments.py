import pandas as pd
import random
from faker import Faker
from datetime import timedelta

random.seed(42)
Faker.seed(42)

fake = Faker("en_GB")
"""
Harbour & Co. Retail Operations Analytics

Shipment Data Generator

Generates shipment records linked to:
- orders
- warehouse locations

Matches MySQL shipments table:

shipment_id
order_id
warehouse_id
shipment_date
expected_delivery_date
actual_delivery_date
shipment_status
delivery_method
"""


# -----------------------------------------------------
# Configuration
# -----------------------------------------------------

orders_file = "data/raw/orders.csv"
locations_file = "data/raw/locations.csv"

output_file = "data/raw/shipments.csv"


# -----------------------------------------------------
# Load Data
# -----------------------------------------------------

orders = pd.read_csv(
    orders_file,
    parse_dates=["order_date"]
)

locations = pd.read_csv(
    locations_file
)


# Only warehouses can fulfil shipments
warehouses = pd.read_csv(
    "data/raw/warehouses.csv"
)

# -----------------------------------------------------
# Filter Orders Requiring Shipment
# -----------------------------------------------------

shipment_orders = orders[
    orders["sales_channel"].isin(
        [
            "Website",
            "Marketplace"
        ]
    )
].copy()


# -----------------------------------------------------
# Logic Functions
# -----------------------------------------------------

def generate_delivery_method(channel):

    if channel == "Website":

        return random.choice(
            [
                "Standard Delivery",
                "Express Delivery",
                "Next Day Delivery"
            ]
        )

    elif channel == "Marketplace":

        return random.choice(
            [
                "Standard Delivery",
                "Express Delivery"
            ]
        )



def generate_expected_days():

    return random.randint(
        2,
        7
    )



def generate_actual_delivery(
    shipment_status,
    shipment_date,
    expected_delivery_date
):

    if shipment_status in [
        "Processing",
        "Shipped",
        "Cancelled"
    ]:
        return None


    if shipment_status in [
        "Delivered",
        "Returned"
    ]:

        # Mostly on-time deliveries
        delay = random.choices(
            [
                -1,
                0,
                1,
                2,
                3
            ],
            weights=[
                10,
                60,
                20,
                8,
                2
            ]
        )[0]


        return (
            expected_delivery_date
            +
            timedelta(days=delay)
        )



# -----------------------------------------------------
# Generate Shipments
# -----------------------------------------------------

shipments = []


shipment_id = 1


for _, order in shipment_orders.iterrows():

    warehouse_id = random.choice(
       warehouses["warehouse_id"].tolist()
    )

    # Shipment date after order date

    shipment_date = (
        order["order_date"]
        +
        timedelta(
            days=random.randint(1,3)
        )
    )


    expected_delivery_date = (
        shipment_date
        +
        timedelta(
            days=generate_expected_days()
        )
    )


    shipment_status = order["order_status"]


    actual_delivery_date = generate_actual_delivery(
        shipment_status,
        shipment_date,
        expected_delivery_date
    )


    shipments.append(
        {
            "shipment_id": shipment_id,

            "order_id": order["order_id"],

            "warehouse_id": warehouse_id,

            "shipment_date": shipment_date.date(),

            "expected_delivery_date": expected_delivery_date.date(),

            "actual_delivery_date": (
                actual_delivery_date.date()
                if actual_delivery_date
                else None
            ),

            "shipment_status": shipment_status,

            "delivery_method": generate_delivery_method(
                order["sales_channel"]
            )
        }
    )


    shipment_id += 1



# -----------------------------------------------------
# Export CSV
# -----------------------------------------------------

df = pd.DataFrame(shipments)


df.to_csv(
    output_file,
    index=False,
    na_rep="NULL"
)


print("Shipments dataset generated successfully.")

print(df.head())

print(
    f"Total shipments generated: {len(df)}"
)


# -----------------------------------------------------
# Validation
# -----------------------------------------------------

print("\nValidation Checks")


print(
    "Valid order references:",
    df["order_id"].isin(
        orders["order_id"]
    ).all()
)


print(
    "Valid warehouse references:",
    df["warehouse_id"].isin(
        warehouses["warehouse_id"]
    ).all()
)


print(
    "Invalid delivery dates:",
    (
        pd.to_datetime(df["actual_delivery_date"])
        <
        pd.to_datetime(df["shipment_date"])
    ).sum()
)