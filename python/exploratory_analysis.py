import pandas as pd

# Load datasets

customers_df = pd.read_csv("data/customers.csv")
products_df = pd.read_csv("data/products.csv")
suppliers_df = pd.read_csv("data/suppliers.csv")
orders_df = pd.read_csv("data/orders.csv")
order_items_df = pd.read_csv("data/order_items.csv")
employees_df = pd.read_csv("data/employees.csv")
shipments_df = pd.read_csv("data/shipments.csv")


print("Customers")
print(customers_df.head())

print("\nProducts")
print(products_df.head())

print("\nOrders")
print(orders_df.head())
print("\nCustomer Information")
print(customers_df.info())

print("\nProduct Information")
print(products_df.info())

print("\nOrder Information")
print(orders_df.info())
print("\nMissing Values - Customers")
print(customers_df.isnull().sum())

print("\nMissing Values - Products")
print(products_df.isnull().sum())

print("\nMissing Values - Orders")
print(orders_df.isnull().sum())

