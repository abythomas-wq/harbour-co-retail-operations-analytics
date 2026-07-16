# Harbour & Co. Retail Operations Analytics

# Data Model Design Document

## 1. Purpose

This document defines the relational database design for Harbour & Co. Retail Operations Analytics.

The data model has been designed to support Project Horizon's objectives by representing key retail operations including sales, inventory management, fulfilment, supplier performance and customer behaviour.

The model follows a relational database approach to ensure data integrity, analytical flexibility and scalability.

---

# 2. Data Modelling Approach

The database design follows a process-oriented approach.

Each entity represents a key business process:

- Customer purchasing activity
- Product management
- Inventory control
- Supplier operations
- Warehouse fulfilment
- Delivery execution

The model has been designed to answer the business questions identified during requirements analysis.

---

# 3. High-Level Entity Relationship Overview

The core business processes are connected as follows:
Customers
    |
    |
Orders
    |
    |
Order Items
    |
    |
Products
    |
    |
Inventory
    |
    |
Locations

Products
    |
    |
Suppliers

Orders
    |
    |
Shipments
    |
    |
Carriers


---

# 4. Core Entities

## 4.1 Customers

### Business Purpose

Stores customer information required to analyse purchasing behaviour, retention and customer value.

### Primary Key

customer_id

### Attributes

| Field | Description |
|---|---|
| customer_id | Unique customer identifier |
| first_name | Customer first name |
| last_name | Customer surname |
| email | Customer email |
| location | Customer region |
| customer_segment | Customer classification |
| registration_date | Date customer joined |

### Supports

- Customer Retention Rate
- Customer Lifetime Value
- Customer Segmentation

---

# 4.2 Products

### Business Purpose

Stores product information required for commercial, inventory and supplier analysis.

### Primary Key

product_id

### Foreign Key

supplier_id

### Attributes

| Field | Description |
|---|---|
| product_id | Unique product identifier |
| product_name | Product description |
| category | Product category |
| supplier_id | Product supplier |
| cost_price | Product cost |
| selling_price | Retail price |

### Supports

- Revenue Analysis
- Category Performance
- Inventory Analysis

---

# 4.3 Suppliers

### Business Purpose

Stores supplier information to evaluate supply chain reliability.

### Primary Key

supplier_id

### Attributes

| Field | Description |
|---|---|
| supplier_id | Unique supplier identifier |
| supplier_name | Supplier name |
| supplier_region | Supplier location |
| supplier_category | Supplier type |

### Supports

- Supplier Performance Analysis
- Procurement Decisions

---

# 4.4 Stores

### Business Purpose

Represents Harbour & Co.'s physical retail locations.

### Primary Key

store_id

### Attributes

| Field | Description |
|---|---|
| store_id | Unique store identifier |
| store_name | Store name |
| location | Store location |
| region | Operating region |
| opening_date | Store opening date |

### Supports

- Store Performance
- Omnichannel Analysis

---

# 4.5 Warehouses

### Business Purpose

Represents distribution centres supporting online fulfilment.

### Primary Key

warehouse_id

### Attributes

| Field | Description |
|---|---|
| warehouse_id | Warehouse identifier |
| warehouse_name | Distribution centre name |
| location | Warehouse location |
| capacity | Processing capacity |

### Supports

- Fulfilment Performance
- Operational Efficiency

---

# 4.6 Orders

### Business Purpose

Stores customer transactions across sales channels.

### Primary Key

order_id

### Foreign Keys

- customer_id
- store_id

### Attributes

| Field | Description |
|---|---|
| order_id | Order identifier |
| customer_id | Customer placing order |
| order_date | Transaction date |
| sales_channel | Store, Online, Click & Collect |
| store_id | Associated store |
| order_status | Order completion status |

### Supports

- Revenue
- Average Order Value
- Channel Analysis

---

# 4.7 Order Items

### Business Purpose

Stores individual products purchased within each order.

### Primary Key

order_item_id

### Foreign Keys

- order_id
- product_id

### Attributes

| Field | Description |
|---|---|
| order_item_id | Order line identifier |
| order_id | Associated order |
| product_id | Purchased product |
| quantity | Units purchased |
| unit_price | Selling price |

### Supports

- Product Analysis
- Category Performance

---

# 4.8 Inventory

### Business Purpose

Tracks product availability across stores and warehouses.

### Primary Key

inventory_id

### Foreign Keys

- product_id
- location_id

### Attributes

| Field | Description |
|---|---|
| inventory_id | Inventory record |
| product_id | Product reference |
| location_id | Stock location |
| quantity_available | Available units |
| inventory_date | Stock snapshot date |

### Supports

- Inventory Turnover
- Stock Availability
- Inventory Ageing

---

# 4.9 Shipments

### Business Purpose

Tracks order fulfilment and delivery performance.

### Primary Key

shipment_id

### Foreign Keys

- order_id
- warehouse_id

### Attributes

| Field | Description |
|---|---|
| shipment_id | Shipment identifier |
| order_id | Related order |
| warehouse_id | Dispatch location |
| dispatch_date | Shipment date |
| delivery_date | Customer delivery date |
| carrier | Delivery partner |

### Supports

- Order Processing Time
- On-Time Delivery Rate

---

# 5. Relationship Summary

| Parent Entity | Child Entity | Relationship |
|---|---|---|
| Customer | Orders | One-to-Many |
| Orders | Order Items | One-to-Many |
| Products | Order Items | One-to-Many |
| Suppliers | Products | One-to-Many |
| Products | Inventory | One-to-Many |
| Orders | Shipments | One-to-One |
| Warehouses | Shipments | One-to-Many |

---

# 6. Data Design Assumptions

The following assumptions apply:

- Financial and operational data is simulated
- Dataset represents a realistic premium retailer
- Historical transaction data is generated for analytical purposes
- Inventory snapshots represent periodic stock positions
- Delivery dates are used to calculate fulfilment performance

---

# 7. Future Analytical Views

The database will support creation of SQL views including:

- vw_sales_performance
- vw_inventory_performance
- vw_fulfilment_metrics
- vw_supplier_performance
- vw_customer_analysis

These views will provide cleaned analytical datasets for Tableau reporting.
