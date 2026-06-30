# SwiftFulfil Operations Analytics - Database Design

## 1. Database Purpose

The SwiftFulfil Operations Analytics database is designed to support operational reporting and analysis for an e-commerce fulfilment business.

The database will capture key operational processes including:

- Customer orders
- Product management
- Inventory tracking
- Warehouse operations
- Employee activity
- Shipment performance

The purpose of the database is to enable analysis of operational efficiency, identify improvement opportunities, and support data-driven decision-making.

---

## 2. Business Scenario

SwiftFulfil operates multiple fulfilment centres that process customer orders.

The operational workflow:

Customer places order → Warehouse processes order → Products are picked and packed → Shipment is dispatched → Customer receives order

The database represents the activities involved in this fulfilment lifecycle.

---

## 3. Database Entities

The database contains the following core entities:

| Entity | Purpose |
|---|---|
| Customers | Stores customer information |
| Products | Stores product details |
| Suppliers | Stores supplier information |
| Warehouses | Stores fulfilment centre details |
| Inventory | Tracks product stock levels |
| Employees | Stores warehouse workforce information |
| Orders | Records customer orders |
| Order Items | Records products included in orders |
| Shipments | Tracks delivery information |
| Warehouse Activity | Records operational tasks performed by employees |

---

## 4. Entity Relationships

### Customers and Orders

One customer can place multiple orders.

Relationship:

Customer (1) → Orders (Many)

---

### Orders and Order Items

One order can contain multiple products.

Relationship:

Orders (1) → Order Items (Many)

---

### Products and Order Items

One product can appear in many orders.

Relationship:

Products (1) → Order Items (Many)

---

### Warehouses and Inventory

One warehouse stores many products.

Relationship:

Warehouses (1) → Inventory (Many)

---

### Suppliers and Products

One supplier can provide multiple products.

Relationship:

Suppliers (1) → Products (Many)

---

### Warehouses and Employees

One warehouse employs multiple employees.

Relationship:

Warehouses (1) → Employees (Many)

---

### Orders and Shipments

Each order has one shipment record.

Relationship:

Orders (1) → Shipments (1)

---

### Employees and Warehouse Activity

One employee can perform many operational activities.

Relationship:

Employees (1) → Warehouse Activity (Many)

---

## 5. Database Design Principles

The database follows relational database design principles:

### Primary Keys

Each table will contain a unique identifier to ensure every record can be uniquely identified.

### Foreign Keys

Relationships between tables will be created using foreign keys to maintain data integrity.

### Normalisation

The database structure follows approximately Third Normal Form (3NF).

This reduces:

- Duplicate data
- Update inconsistencies
- Storage inefficiency

Each table represents one business concept.

---

## 6. Future Analysis Areas

The database will support analysis including:

- Order volume trends
- Warehouse performance comparison
- Inventory availability
- Stock-out analysis
- Employee productivity
- Delivery performance
- Customer order patterns