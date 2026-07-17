import pandas as pd
import random
from faker import Faker
from datetime import timedelta

random.seed(42)
Faker.seed(42)

fake = Faker("en_GB")


"""
Harbour & Co. Retail Operations Analytics

Purchase Order Data Generator

Generates supplier purchase orders linked to:
- products
- suppliers

Matches MySQL purchase_orders table:

purchase_order_id
supplier_id
product_id
order_date
expected_delivery_date
actual_delivery_date
quantity_ordered
purchase_order_status
unit_cost
"""



# -----------------------------------------------------
# Configuration
# -----------------------------------------------------

TOTAL_PURCHASE_ORDERS = 50000

products_file = "data/raw/products.csv"
suppliers_file = "data/raw/suppliers.csv"

output_file = "data/raw/purchase_orders.csv"


# -----------------------------------------------------
# Load Data
# -----------------------------------------------------

products = pd.read_csv(
    products_file,
    parse_dates=["launch_date"]
)

suppliers = pd.read_csv(
    suppliers_file
)


# -----------------------------------------------------
# Active Products Only
# -----------------------------------------------------

products = products[
    products["product_status"] == "Active"
].copy()


# -----------------------------------------------------
# Status Configuration
# -----------------------------------------------------

purchase_statuses = [
    "Received",
    "Ordered",
    "Pending",
    "Delayed",
    "Cancelled"
]


status_weights = [
    65,
    15,
    10,
    8,
    2
]


# -----------------------------------------------------
# Quantity Logic
# -----------------------------------------------------

def generate_quantity(category):

    if category == "Fashion":
        return random.randint(100, 1000)

    elif category == "Home":
        return random.randint(100, 1500)

    elif category == "Beauty":
        return random.randint(200, 3000)

    elif category == "Consumer Goods":
        return random.randint(500, 5000)

    elif category == "Lifestyle":
        return random.randint(100, 1500)

    else:
        return random.randint(100, 1000)



# -----------------------------------------------------
# Generate Purchase Orders
# -----------------------------------------------------

purchase_orders = []


for purchase_order_id in range(
    1,
    TOTAL_PURCHASE_ORDERS + 1
):

    product = products.sample(
        1
    ).iloc[0]


    supplier_id = product["supplier_id"]


    order_date = fake.date_between(
        start_date="-10y",
        end_date="today"
    )


    expected_delivery_date = (
        order_date
        +
        timedelta(
            days=random.randint(
                14,
                45
            )
        )
    )


    status = random.choices(
        purchase_statuses,
        weights=status_weights
    )[0]


    if status in [
        "Received",
        "Delayed"
    ]:

        delay = random.randint(
            -3,
            10
        )

        actual_delivery_date = (
            expected_delivery_date
            +
            timedelta(
                days=delay
            )
        )

    else:

        actual_delivery_date = None



    unit_cost = round(
        product["cost_price"]
        *
        random.uniform(
            0.95,
            1.05
        ),
        2
    )


    purchase_orders.append(
        {
            "purchase_order_id": purchase_order_id,

            "supplier_id": supplier_id,

            "product_id": product["product_id"],

            "order_date": order_date,

            "expected_delivery_date": expected_delivery_date,

            "actual_delivery_date": actual_delivery_date,

            "quantity_ordered": generate_quantity(
                product["category"]
            ),

            "purchase_order_status": status,

            "unit_cost": unit_cost
        }
    )



# -----------------------------------------------------
# Export
# -----------------------------------------------------

df = pd.DataFrame(
    purchase_orders
)


df.to_csv(
    output_file,
    index=False,
    na_rep="NULL"
)


print(
    "Purchase orders dataset generated successfully."
)

print(
    df.head()
)

print(
    f"Total purchase orders generated: {len(df)}"
)


# -----------------------------------------------------
# Validation
# -----------------------------------------------------

print("\nValidation Checks")


print(
    "Valid supplier references:",
    df["supplier_id"].isin(
        suppliers["supplier_id"]
    ).all()
)


print(
    "Valid product references:",
    df["product_id"].isin(
        products["product_id"]
    ).all()
)


print(
    "Negative quantities:",
    (
        df["quantity_ordered"] < 0
    ).sum()
)


print(
    "Invalid delivery dates:",
    (
        pd.to_datetime(df["actual_delivery_date"])
        <
        pd.to_datetime(df["order_date"])
    ).sum()
)