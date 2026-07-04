import pandas as pd
import numpy as np
from faker import Faker
product_catalogue = pd.read_csv(
    "data/product_catalogue.csv"
)
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

for i in range(1, 201):
    
    cost_price = round(random.uniform(5, 100), 2)
    selling_price = round(cost_price * random.uniform(1.2, 2.5), 2)

    products.append({
        "product_id": i,
        "product_name": product_catalogue.loc[i-1, "product_name"],       
        "category": product_catalogue.loc[i-1, "category"],
        "cost_price": cost_price,
        "selling_price": selling_price,
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
        "category": product_catalogue.loc[i-1, "category"],
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

# =========================
# SEGMENT CONFIGURATION (REALISTIC VERSION)
# =========================

segment_product_bias = {
    "Standard": (5, 70),
    "Premium": (60, 140),
    "Enterprise": (120, 300)
}

segment_config = {
    "Standard": {
        "orders_per_customer": (1, 3),
        "quantity_range": (1, 2),
        "basket_size": (1, 3)
    },
    "Premium": {
        "orders_per_customer": (2, 5),
        "quantity_range": (1, 4),
        "basket_size": (2, 6)
    },
    "Enterprise": {
        "orders_per_customer": (4, 8),
        "quantity_range": (2, 8),
        "basket_size": (3, 10)
    }
}

# stronger category realism
segment_category_bias = {
    "Standard": ["Accessories", "Office Supplies"],
    "Premium": ["Office Supplies", "Fitness", "Accessories"],
    "Enterprise": ["Electronics", "Office Supplies"]
}

# =========================
# Generate Orders + Order Items
# =========================

orders = []
order_items = []
order_id = 1

for customer in customers:

    segment = customer["customer_segment"]
    config = segment_config[segment]

    num_orders = random.randint(*config["orders_per_customer"])

    for _ in range(num_orders):

        # -------------------------
        # ORDER HEADER
        # -------------------------
        orders.append({
            "order_id": order_id,
            "customer_id": customer["customer_id"],
            "order_date": fake.date_between(start_date="-2y", end_date="today"),
            "warehouse": random.choice(["Manchester", "London", "Birmingham", "Leeds"]),
            "order_status": random.choices(
                ["Completed", "Returned", "Cancelled"],
                weights=[0.85, 0.10, 0.05]
            )[0],
            "payment_method": random.choice(["Card", "PayPal", "Cash"]),
            "delivery_date": fake.date_between(start_date="-2y", end_date="today")
        })

        # -------------------------
        # ORDER ITEMS
        # -------------------------
        num_items = random.randint(*config["basket_size"])

        for _ in range(num_items):

            allowed_categories = segment_category_bias[segment]
            price_min, price_max = segment_product_bias[segment]

            eligible_products = [
                p for p in products
                if (p["category"] in allowed_categories)
                and (price_min <= p["selling_price"] <= price_max)
            ]

            # safety fallback (rare, but safe)
            if not eligible_products:
                eligible_products = [
                    p for p in products
                    if price_min <= p["selling_price"] <= price_max
                ]

            # weighted selection (enterprise bias amplified)
            weights = [
                (p["selling_price"] ** 1.3) *
                (1.0 if segment == "Standard"
                 else 1.4 if segment == "Premium"
                 else 2.2)
                for p in eligible_products
            ]

            product = random.choices(
                eligible_products,
                weights=weights,
                k=1
            )[0]

            quantity = random.randint(*config["quantity_range"])

            order_items.append({
                "order_id": order_id,
                "product_id": product["product_id"],
                "quantity": quantity
            })

        order_id += 1

print("Orders dataset created successfully!")
print("Order items dataset created successfully!")
# Generate Departments Dataset

departments = []

department_names = [
    "Warehouse",
    "Sales",
    "Finance",
    "Customer Service",
    "Logistics"
]

department_locations = [
    "Manchester",
    "London",
    "Birmingham",
    "Leeds",
    "Liverpool"
]


for i in range(1, 6):

    departments.append({
        "department_id": i,
        "department_name": department_names[i-1],
        "location": department_locations[i-1]
    })


departments_df = pd.DataFrame(departments)

departments_df.to_csv(
    "data/departments.csv",
    index=False
)

print("Departments dataset created successfully!")
print(departments_df.head())


# Generate Employees Dataset

employees = []

department_roles = {
    1: [
        "Warehouse Associate",
        "Supervisor",
        "Manager"
    ],
    2: [
        "Sales Representative",
        "Supervisor",
        "Manager"
    ],
    3: [
        "Analyst",
        "Accountant",
        "Manager"
    ],
    4: [
        "Customer Advisor",
        "Supervisor",
        "Manager"
    ],
    5: [
        "Logistics Coordinator",
        "Supervisor",
        "Manager"
    ]
}


for i in range(1, 51):

    department_id = random.randint(1, 5)

    employees.append({
        "employee_id": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "department_id": department_id,
        "job_role": random.choice(
            department_roles[department_id]
        ),
        "hire_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    })


employees_df = pd.DataFrame(employees)

employees_df.to_csv(
    "data/employees.csv",
    index=False
)

print("Employees dataset created successfully!")
print(employees_df.head())


# Generate Shipments Dataset

shipments = []

carriers = [
    "DHL",
    "UPS",
    "Royal Mail",
    "FedEx"
]


shipment_statuses = [
    "Delivered",
    "In Transit",
    "Delayed"
]


for order_id in range(1, 1001):

    shipment_date = fake.date_between(
        start_date="-1y",
        end_date="today"
    )

    shipments.append({
        "shipment_id": order_id,
        "order_id": order_id,
        "shipment_date": shipment_date,
        "carrier": random.choice(carriers),
        "shipment_status": random.choice(shipment_statuses),
        "delivery_days": random.randint(1, 7)
    })


shipments_df = pd.DataFrame(shipments)

shipments_df.to_csv(
    "data/shipments.csv",
    index=False
)

print("Shipments dataset created successfully!")
print(shipments_df.head())
