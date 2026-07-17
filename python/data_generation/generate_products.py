"""
Harbour & Co. Retail Operations Analytics

Product Data Generator

Generates product catalogue linked to existing suppliers.
"""

import pandas as pd
import random
from faker import Faker


fake = Faker("en_GB")


# -----------------------------------------------------
# Configuration
# -----------------------------------------------------

TOTAL_PRODUCTS = 2000


# -----------------------------------------------------
# Load Supplier Master Data
# -----------------------------------------------------

suppliers = pd.read_csv(
    "data/raw/suppliers.csv"
)


# -----------------------------------------------------
# Product Category Distribution
# -----------------------------------------------------

category_distribution = {
    "Fashion": 35,
    "Home": 25,
    "Lifestyle": 20,
    "Beauty": 10,
    "Consumer Goods": 10
}


# -----------------------------------------------------
# Product Catalogue Hierarchy
# -----------------------------------------------------

product_catalogue = {

    "Fashion": {

        "Clothing": [
            "Classic Cotton Shirt",
            "Slim Fit Denim Jacket",
            "Heritage Wool Coat",
            "Organic Linen Shirt",
            "Premium Knit Sweater"
        ],

        "Footwear": [
            "Premium Leather Boots",
            "Running Trainers",
            "Casual Canvas Shoes",
            "Formal Leather Shoes"
        ],

        "Accessories": [
            "Leather Wallet",
            "Canvas Backpack",
            "Classic Belt",
            "Designer Sunglasses"
        ]
    },


    "Home": {

        "Furniture": [
            "Oak Dining Table",
            "Wooden Storage Cabinet",
            "Modern Sofa",
            "Bedroom Side Table"
        ],

        "Kitchen": [
            "Ceramic Dinner Set",
            "Premium Cookware Set",
            "Glass Storage Containers",
            "Kitchen Knife Set"
        ],

        "Decor": [
            "Cotton Cushion Set",
            "Ceramic Vase",
            "Wall Art Frame",
            "Decorative Lamp"
        ]
    },


    "Lifestyle": {

        "Travel": [
            "Travel Backpack",
            "Cabin Luggage",
            "Travel Organiser"
        ],

        "Fitness": [
            "Fitness Training Mat",
            "Resistance Bands",
            "Workout Equipment"
        ],

        "Outdoor": [
            "Camping Chair",
            "Outdoor Water Bottle",
            "Hiking Equipment"
        ]
    },


    "Beauty": {

        "Skincare": [
            "Vitamin C Serum",
            "Hydrating Moisturiser",
            "Natural Face Cleanser"
        ],

        "Haircare": [
            "Hair Repair Treatment",
            "Strengthening Shampoo"
        ],

        "Cosmetics": [
            "Luxury Beauty Kit",
            "Foundation Set"
        ]
    },


    "Consumer Goods": {

        "Electronics": [
            "Wireless Speaker",
            "Smart Home Device",
            "Portable Charger"
        ],

        "Stationery": [
            "Premium Notebook Set",
            "Office Stationery Pack"
        ],

        "General": [
            "Storage Box",
            "Household Organiser"
        ]
    }
}


# -----------------------------------------------------
# Pricing Logic
# -----------------------------------------------------

price_ranges = {

    "Fashion": (10, 120),
    "Home": (20, 250),
    "Lifestyle": (5, 100),
    "Beauty": (3, 50),
    "Consumer Goods": (10, 150)

}


gross_margin = {

    "Fashion": 0.55,
    "Home": 0.45,
    "Lifestyle": 0.50,
    "Beauty": 0.65,
    "Consumer Goods": 0.35

}


# -----------------------------------------------------
# Product Status Logic
# -----------------------------------------------------

product_statuses = [
    "Active",
    "Active",
    "Active",
    "Active",
    "Discontinued"
]


# -----------------------------------------------------
# Generate Products
# -----------------------------------------------------

products = []


for product_id in range(1, TOTAL_PRODUCTS + 1):

    # Select category

    category = random.choices(
        list(category_distribution.keys()),
        weights=list(category_distribution.values())
    )[0]


    # Select matching sub-category

    sub_category = random.choice(
        list(product_catalogue[category].keys())
    )


    # Select product name from correct category

    product_name = random.choice(
        product_catalogue[category][sub_category]
    )


    # Match supplier category

    eligible_suppliers = suppliers[
        suppliers["supplier_category"] == category
    ]


    supplier_id = random.choice(
        eligible_suppliers["supplier_id"].tolist()
    )


    # Generate cost price

    cost_price = round(
        random.uniform(
            price_ranges[category][0],
            price_ranges[category][1]
        ),
        2
    )


    # Calculate selling price using margin

    selling_price = round(
        cost_price / (1 - gross_margin[category]),
        2
    )


    products.append(
        {

            "product_id": product_id,

            "product_name": product_name,

            "category": category,

            "sub_category": sub_category,

            "supplier_id": supplier_id,

            "cost_price": cost_price,

            "selling_price": selling_price,

            "product_status": random.choice(
                product_statuses
            ),

            "launch_date": fake.date_between(
                start_date="-5y",
                end_date="-1m"
            )

        }
    )


# -----------------------------------------------------
# Export CSV
# -----------------------------------------------------

df = pd.DataFrame(products)


df.to_csv(
    "data/raw/products.csv",
    index=False
)


print("Products dataset generated successfully.")
print(df.head())
print(f"Total products generated: {len(df)}")