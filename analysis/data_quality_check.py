import pandas as pd


customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
suppliers = pd.read_csv("data/suppliers.csv")
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")
departments = pd.read_csv("data/departments.csv")
employees = pd.read_csv("data/employees.csv")
shipments = pd.read_csv("data/shipments.csv")


print("Datasets loaded successfully!")

print("\nDataset sizes:")

print("Customers:", customers.shape)
print("Products:", products.shape)
print("Suppliers:", suppliers.shape)
print("Orders:", orders.shape)
print("Order Items:", order_items.shape)
print("Departments:", departments.shape)
print("Employees:", employees.shape)
print("Shipments:", shipments.shape)
print("\nMissing values:")

print("\nCustomers")
print(customers.isnull().sum())

print("\nProducts")
print(products.isnull().sum())

print("\nSuppliers")
print(suppliers.isnull().sum())

print("\nOrders")
print(orders.isnull().sum())

print("\nOrder Items")
print(order_items.isnull().sum())

print("\nEmployees")
print(employees.isnull().sum())

print("\nShipments")
print(shipments.isnull().sum())
print("\nDuplicate ID checks:")

print("Customers duplicate IDs:",
      customers["customer_id"].duplicated().sum())

print("Products duplicate IDs:",
      products["product_id"].duplicated().sum())

print("Suppliers duplicate IDs:",
      suppliers["supplier_id"].duplicated().sum())

print("Orders duplicate IDs:",
      orders["order_id"].duplicated().sum())

print("Departments duplicate IDs:",
      departments["department_id"].duplicated().sum())

print("Employees duplicate IDs:",
      employees["employee_id"].duplicated().sum())

print("Shipments duplicate IDs:",
      shipments["shipment_id"].duplicated().sum())

print("\nRelationship checks:")

# Orders should only contain existing customers

missing_customers = orders[
    ~orders["customer_id"].isin(customers["customer_id"])
]

print(
    "Orders with invalid customer_id:",
    len(missing_customers)
)


# Products should only contain existing suppliers

missing_suppliers = products[
    ~products["supplier_id"].isin(suppliers["supplier_id"])
]

print(
    "Products with invalid supplier_id:",
    len(missing_suppliers)
)


# Order items should only contain existing orders

missing_orders = order_items[
    ~order_items["order_id"].isin(orders["order_id"])
]

print(
    "Order items with invalid order_id:",
    len(missing_orders)
)


# Order items should only contain existing products

missing_products = order_items[
    ~order_items["product_id"].isin(products["product_id"])
]

print(
    "Order items with invalid product_id:",
    len(missing_products)
)


# Employees should only contain existing departments

missing_departments = employees[
    ~employees["department_id"].isin(departments["department_id"])
]

print(
    "Employees with invalid department_id:",
    len(missing_departments)
)


# Shipments should only contain existing orders

missing_shipment_orders = shipments[
    ~shipments["order_id"].isin(orders["order_id"])
]

print(
    "Shipments with invalid order_id:",
    len(missing_shipment_orders)
)
