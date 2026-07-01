import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import date, timedelta

# Create Faker object
fake = Faker()

# Number of customers to generate
number_of_customers = 1000

# Customer segments
segments = [
    "Premium",
    "Standard",
    "Enterprise"
]

# UK cities
cities = [
    "London",
    "Manchester",
    "Birmingham",
    "Leeds",
    "Liverpool",
    "Bristol",
    "Sheffield",
    "Glasgow",
    "Edinburgh",
    "Cardiff"
]

# Create empty list to store customer records
customers = []

# Generate customer data
for customer_id in range(1, number_of_customers + 1):

    first_name = fake.first_name()
    last_name = fake.last_name()

    customer = {
        "customer_id": customer_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": f"{first_name.lower()}.{last_name.lower()}@email.com",
        "city": random.choice(cities),
        "signup_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        "customer_segment": random.choice(segments)
    }

    customers.append(customer)


# Convert list into DataFrame
customers_df = pd.DataFrame(customers)


# Save as CSV
customers_df.to_csv(
    "data/customers.csv",
    index=False
)

print("Customers dataset created successfully!")
print(customers_df.head())

# Generate Products Dataset

products = []

categories = [
    "Electronics",
    "Home & Kitchen",
    "Office Supplies",
    "Fitness",
    "Accessories"
]

for i in range(1, 201):
    products.append({
        "product_id": i,
        "product_name": fake.word().title() + " " + random.choice([
            "Pro",
            "Plus",
            "Max",
            "Standard"
        ]),
        "category": random.choice(categories),
        "cost_price": round(random.uniform(5, 100), 2),
        "selling_price": round(random.uniform(10, 200), 2),
        "supplier_id": random.randint(1, 20)
    })


products_df = pd.DataFrame(products)

products_df.to_csv(
    "data/products.csv",
    index=False
)

print("Products dataset created successfully!")
print(products_df.head())
# Generate Suppliers Dataset

suppliers = []

supplier_categories = [
    "Electronics",
    "Home & Kitchen",
    "Office Supplies",
    "Fitness",
    "Accessories"
]

for i in range(1, 21):
    suppliers.append({
        "supplier_id": i,
        "supplier_name": fake.company(),
        "country": fake.country(),
        "category": random.choice(supplier_categories),
        "lead_time_days": random.randint(2, 15),
        "supplier_rating": round(random.uniform(3, 5), 1)
    })


suppliers_df = pd.DataFrame(suppliers)

suppliers_df.to_csv(
    "data/suppliers.csv",
    index=False
)

print("Suppliers dataset created successfully!")
print(suppliers_df.head())
# Generate Orders Dataset

orders = []

warehouses = [
    "London",
    "Manchester",
    "Birmingham",
    "Edinburgh"
]

order_statuses = [
    "Delivered",
    "Processing",
    "Cancelled",
    "Returned"
]

payment_methods = [
    "Card",
    "PayPal",
    "Bank Transfer"
]

for i in range(1, 1001):

    order_date = fake.date_between(
        start_date="-1y",
        end_date="today"
    )

    orders.append({
        "order_id": i,
        "customer_id": random.randint(1, 100),
        "order_date": order_date,
        "warehouse": random.choice(warehouses),
        "order_status": random.choice(order_statuses),
        "payment_method": random.choice(payment_methods),
        "delivery_date": fake.date_between(
            start_date=order_date,
            end_date="+30d"
        )
    })


orders_df = pd.DataFrame(orders)

orders_df.to_csv(
    "data/orders.csv",
    index=False
)

print("Orders dataset created successfully!")
print(orders_df.head())
# Generate Order Items Dataset

order_items = []

for order_id in range(1, 1001):

    number_of_items = random.randint(1, 5)

    selected_products = random.sample(
        range(1, 201),
        number_of_items
    )

    for product_id in selected_products:
        order_items.append({
            "order_id": order_id,
            "product_id": product_id,
            "quantity": random.randint(1, 5)
        })


order_items_df = pd.DataFrame(order_items)

order_items_df.to_csv(
    "data/order_items.csv",
    index=False
)

print("Order Items dataset created successfully!")
print(order_items_df.head())
# Generate Order Items Dataset

order_items = []

for order_id in range(1, 1001):

    number_of_items = random.randint(1, 5)

    selected_products = random.sample(
        range(1, 201),
        number_of_items
    )

    for product_id in selected_products:
        order_items.append({
            "order_id": order_id,
            "product_id": product_id,
            "quantity": random.randint(1, 5)
        })


order_items_df = pd.DataFrame(order_items)

order_items_df.to_csv(
    "data/order_items.csv",
    index=False
)

print("Order Items dataset created successfully!")
print(order_items_df.head())