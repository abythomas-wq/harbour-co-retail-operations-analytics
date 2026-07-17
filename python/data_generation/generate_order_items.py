"""
Harbour & Co. Retail Operations Analytics

Order Items Data Generator

Generates order line items linked to:
- orders
- products
- customers

Creates transactional detail required for revenue,
basket analysis and product performance analytics.
"""

import pandas as pd
import random


# -----------------------------------------------------
# Configuration
# -----------------------------------------------------

orders_file = "data/raw/orders.csv"
products_file = "data/raw/products.csv"
customers_file = "data/raw/customers.csv"

output_file = "data/raw/order_items.csv"


# -----------------------------------------------------
# Load Existing Data
# -----------------------------------------------------

orders = pd.read_csv(orders_file)

products = pd.read_csv(products_file)

customers = pd.read_csv(customers_file)


# -----------------------------------------------------
# Prepare Product Pools
# -----------------------------------------------------

product_lookup = products.set_index("product_id")


# -----------------------------------------------------
# Basket Size Logic
# -----------------------------------------------------

basket_sizes = [1, 2, 3, 4, 5, 6, 7, 8]

basket_weights = [
    20,
    25,
    20,
    15,
    10,
    5,
    3,
    2
]


# -----------------------------------------------------
# Quantity Logic
# -----------------------------------------------------

def generate_quantity(category):

    if category == "Fashion":
        return random.randint(1, 2)

    elif category == "Home":
        return random.randint(1, 3)

    elif category == "Lifestyle":
        return random.randint(1, 3)

    elif category == "Beauty":
        return random.randint(1, 4)

    elif category == "Consumer Goods":
        return random.randint(1, 5)

    else:
        return 1


# -----------------------------------------------------
# Discount Logic
# -----------------------------------------------------

def generate_discount(unit_price, loyalty_status):

    discount_probability = {

        "Gold": 0.35,
        "Silver": 0.25,
        "Bronze": 0.15,
        "No Membership": 0.10

    }

    probability = discount_probability.get(
        loyalty_status,
        0.10
    )


    if random.random() < probability:

        discount_rate = random.choice(
            [
                0.05,
                0.10,
                0.15,
                0.20
            ]
        )

        return round(
            unit_price * discount_rate,
            2
        )

    return 0.00


# -----------------------------------------------------
# Customer Loyalty Mapping
# -----------------------------------------------------

customer_loyalty = customers.set_index(
    "customer_id"
)["loyalty_status"].fillna(
    "No Membership"
)


# -----------------------------------------------------
# Generate Order Items
# -----------------------------------------------------

order_items = []

order_item_id = 1


for _, order in orders.iterrows():

    order_id = order["order_id"]

    customer_id = order["customer_id"]


    loyalty_status = customer_loyalty.get(
        customer_id,
        "No Membership"
    )


    number_of_products = random.choices(
        basket_sizes,
        weights=basket_weights
    )[0]


    selected_products = products.sample(
        n=number_of_products,
        replace=False
    )


    for _, product in selected_products.iterrows():

        quantity = generate_quantity(
            product["category"]
        )


        unit_price = product["selling_price"]


        discount_amount = generate_discount(
            unit_price * quantity,
            loyalty_status
        )


        line_total = round(
            (quantity * unit_price)
            - discount_amount,
            2
        )


        order_items.append(
            {
                "order_item_id": order_item_id,
                "order_id": order_id,
                "product_id": product["product_id"],
                "quantity": quantity,
                "unit_price": unit_price,
                "discount_amount": discount_amount,
                "line_total": line_total
            }
        )


        order_item_id += 1


# -----------------------------------------------------
# Export CSV
# -----------------------------------------------------

df = pd.DataFrame(order_items)


df.to_csv(
    output_file,
    index=False
)


print("Order items dataset generated successfully.")
print(df.head())
print(f"Total order items generated: {len(df)}")