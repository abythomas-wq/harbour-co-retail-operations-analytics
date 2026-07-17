# Harbour & Co. Retail Operations Analytics

# Database Schema Design

## 1. Purpose

This document defines the technical database schema for the Harbour & Co. Retail Operations Analytics solution.

The schema has been designed to support Project Horizon by enabling analysis of retail operations, including sales performance, inventory efficiency, fulfilment operations and supplier reliability.

---

## 2. Database Design Approach

The database follows a relational data model designed around key business processes.

The design prioritises:

- Data integrity
- Normalisation
- Analytical flexibility
- Clear relationships between business entities

---

## 3. Database Tables Overview

| Table | Purpose | Approximate Volume |
|---|---|---|
| customers | Customer master data | 50,000 rows |
| products | Product catalogue | 2,000 rows |
| suppliers | Supplier information | 250 rows |
| locations | Central reference table for all operational sites | 63 rows
| stores | Retail locations | 60 rows |
| warehouses | Distribution centres | 3 rows |
| orders | Customer transactions | 250,000 rows |
| order_items | Transaction line items | 750,000 rows |
| inventory_snapshots | Historical stock position | 500,000+ rows |
| shipments | Delivery performance | 250,000 rows |
| purchase_orders | Supplier transactions | 50,000 rows |

---

## 4. Table Definitions

## 4.1 Customers

### Business Purpose

Stores customer information required for customer behaviour and retention analysis.

### Primary Key

`customer_id`

### Columns

| Column | Data Type | Description |
|---|---|---|
| customer_id | INT | Unique customer identifier |
| first_name | VARCHAR(50) | Customer first name |
| last_name | VARCHAR(50) | Customer surname |
| email | VARCHAR(100) | Customer email address |
| postcode_area | VARCHAR(20) | Customer region |
| customer_segment | VARCHAR(50) | Customer classification |
| loyalty_status | VARCHAR(50) | Loyalty membership tier |
| acquisition_channel | VARCHAR(50) | Customer acquisition source |
| registration_date | DATE | Date customer joined |

# 4.2 Products

### Business Purpose

Stores product catalogue information required for commercial analysis, inventory management and supplier performance analysis.

The product entity represents the range of fashion, home, lifestyle and consumer products sold through Harbour & Co.'s retail and digital channels.

### Primary Key

`product_id`

### Foreign Keys

`supplier_id`

References:

`suppliers(supplier_id)`

### Columns

| Column | Data Type | Description |
|---|---|---|
| product_id | INT | Unique product identifier |
| product_name | VARCHAR(100) | Product description |
| category | VARCHAR(50) | Product category |
| sub_category | VARCHAR(50) | Product sub-category |
| supplier_id | INT | Product supplier |
| cost_price | DECIMAL(10,2) | Cost paid to supplier |
| selling_price | DECIMAL(10,2) | Customer selling price |
| product_status | VARCHAR(20) | Active or discontinued status |
| launch_date | DATE | Date product became available |

### Supports

- Revenue analysis
- Category performance
- Product profitability analysis
- Inventory analysis
- Supplier analysis

# 4.3 Suppliers

### Business Purpose

Stores supplier information required to analyse supply chain performance, procurement effectiveness and supplier reliability.

The supplier entity represents the organisations that provide products to Harbour & Co. across fashion, home, lifestyle and consumer categories.

### Primary Key

`supplier_id`

### Foreign Keys

None

### Columns

| Column | Data Type | Description |
|---|---|---|
| supplier_id | INT | Unique supplier identifier |
| supplier_name | VARCHAR(100) | Supplier organisation name |
| supplier_region | VARCHAR(50) | Supplier operating region |
| supplier_category | VARCHAR(50) | Type of supplier relationship |
| contact_country | VARCHAR(50) | Supplier country location |
| contract_start_date | DATE | Date supplier relationship began |
| supplier_status | VARCHAR(20) | Active or inactive status |

### Supports

- Supplier On-Time Delivery Rate
- Supplier Lead Time Analysis
- Procurement Performance
- Supply Chain Risk Assessment

# 4.4 Locations

## Business Purpose

Stores information about all physical operational locations within Harbour & Co.

The location entity provides a central reference structure for inventory management by representing all sites where products may be stored, processed or distributed.

This includes retail stores and distribution centres.

## Primary Key

`location_id`

## Foreign Keys

None

## Columns

| Column | Data Type | Description |
|---|---|---|
| location_id | INT | Unique location identifier |
| location_name | VARCHAR(100) | Operational location name |
| location_type | VARCHAR(50) | Store, Warehouse or Distribution Centre |
| address | VARCHAR(150) | Physical address |
| city | VARCHAR(50) | Location city |
| region | VARCHAR(50) | UK operating region |
| postcode | VARCHAR(20) | UK postcode |
| operational_status | VARCHAR(20) | Active or inactive status |
| opening_date | DATE | Date location became operational |

## Supports

- Inventory Visibility Analysis
- Stock Allocation Analysis
- Location Performance Analysis
- Store and Warehouse Integration


# 4.5 Stores

### Business Purpose

Stores information about Harbour & Co.'s physical retail locations across the United Kingdom.

The store entity supports analysis of retail performance, regional trends and omnichannel operations.

### Primary Key

`store_id`

### Foreign Keys

None

### Columns

| Column | Data Type | Description |
|---|---|---|
| store_id | INT | Unique store identifier |
| store_name | VARCHAR(100) | Store name |
| location | VARCHAR(100) | Store location |
| city | VARCHAR(50) | Store city |
| region | VARCHAR(50) | UK operating region |
| store_type | VARCHAR(50) | Store classification |
| opening_date | DATE | Date store opened |
| store_size_sqft | INT | Store floor area |
| store_status | VARCHAR(20) | Active or closed status |

### Supports

- Store Performance Analysis
- Regional Sales Analysis
- Omnichannel Performance Analysis
- Click & Collect Analysis

# 4.6 Warehouses

### Business Purpose

Stores information about Harbour & Co.'s distribution centres responsible for supporting e-commerce fulfilment and inventory movement across the UK.

The warehouse entity supports analysis of fulfilment operations, distribution efficiency and operational capacity.

### Primary Key

`warehouse_id`

### Foreign Keys

None

### Columns

| Column | Data Type | Description |
|---|---|---|
| warehouse_id | INT | Unique warehouse identifier |
| warehouse_name | VARCHAR(100) | Distribution centre name |
| location | VARCHAR(100) | Warehouse location |
| region | VARCHAR(50) | UK operating region |
| warehouse_type | VARCHAR(50) | Warehouse classification |
| capacity_units | INT | Maximum storage capacity |
| operational_status | VARCHAR(20) | Active or inactive status |
| opening_date | DATE | Date warehouse became operational |

### Supports

- Fulfilment Performance Analysis
- Warehouse Efficiency Analysis
- Distribution Capacity Planning
- Inventory Location Analysis

# 4.7 Orders

### Business Purpose

Stores customer transaction information across Harbour & Co.'s omnichannel sales channels.

The orders entity represents customer purchases made through physical stores, online platforms and click & collect services.

This table provides the foundation for analysing revenue performance, customer behaviour and sales channel effectiveness.

### Primary Key

`order_id`

### Foreign Keys

`customer_id`

References:

`customers(customer_id)`

`store_id`

References:

`stores(store_id)`

### Columns

| Column | Data Type | Description |
|---|---|---|
| order_id | INT | Unique order identifier |
| customer_id | INT | Customer placing the order |
| store_id | INT | Associated store where applicable |
| order_date | DATE | Date order was placed |
| sales_channel | VARCHAR(50) | Store, Online or Click & Collect |
| order_status | VARCHAR(30) | Order lifecycle status |
| payment_method | VARCHAR(30) | Customer payment method |
| total_order_value | DECIMAL(10,2) | Total order revenue |

### Supports

- Revenue Analysis
- Average Order Value Analysis
- Sales Channel Performance
- Customer Behaviour Analysis
- Store Performance Analysis

# 4.8 Order Items

### Business Purpose

Stores individual product-level details within each customer order.

The order items entity provides transaction-level granularity required for product performance analysis, category analysis and revenue calculations.

### Primary Key

`order_item_id`

### Foreign Keys

`order_id`

References:

`orders(order_id)`

`product_id`

References:

`products(product_id)`

### Columns

| Column | Data Type | Description |
|---|---|---|
| order_item_id | INT | Unique order line identifier |
| order_id | INT | Associated customer order |
| product_id | INT | Purchased product |
| quantity | INT | Number of units purchased |
| unit_price | DECIMAL(10,2) | Selling price per unit |
| discount_amount | DECIMAL(10,2) | Discount applied |
| line_total | DECIMAL(10,2) | Total value of order line |

### Supports

- Revenue Analysis
- Product Performance Analysis
- Category Performance Analysis
- Basket Analysis
- Supplier Value Analysis

# 4.9 Inventory Snapshots

### Business Purpose

Stores historical inventory positions across Harbour & Co.'s retail stores and distribution centres.

The inventory snapshots entity enables analysis of stock availability, inventory efficiency and product demand patterns over time.

Rather than representing only current stock levels, historical snapshots allow the organisation to understand how inventory changes throughout the product lifecycle.

### Primary Key

`inventory_id`

### Foreign Keys

`product_id`

References:

`products(product_id)`

`location_id`

References:

`locations(location_id)`

### Columns

| Column | Data Type | Description |
|---|---|---|
| inventory_id | INT | Unique inventory record identifier |
| product_id | INT | Product reference |
| location_id | INT | Stock holding location |
| inventory_date | DATE | Date of inventory snapshot |
| quantity_available | INT | Available stock units |
| quantity_reserved | INT | Stock allocated to customer orders |
| quantity_damaged | INT | Stock unavailable due to damage |
| reorder_level | INT | Minimum stock threshold |

### Supports

- Inventory Turnover Analysis
- Stock Availability Rate
- Inventory Ageing Analysis
- Stock Optimisation
- Location-Level Inventory Analysis

# 4.10 Schema Design Decisions

## Decision 001 — Introduction of Location Entity

                         locations
                             |
              --------------------------------
              |                              |
           stores                       warehouses


                             |
                             |
                 inventory_snapshots
                             |
                             |
                         products

### Change

A centralised locations entity was introduced to support inventory analysis across multiple operational sites.

### Reason

Initial modelling separated stores and warehouses. However, inventory management requires a common reference structure because stock can exist across different location types.

### Benefit

The updated design improves:

- data consistency
- scalability
- inventory analysis capability
- future expansion flexibility

## Decision 002 — Introduction of Location Entity

### Change

A centralised location entity was introduced to represent all physical operational sites within Harbour & Co.

Stores and warehouses are treated as specialised location types rather than independent inventory locations.

### Reason

Inventory exists across multiple operational environments, including retail stores and distribution centres. A unified location reference prevents duplication and enables consistent inventory analysis.

### Benefit

The updated design improves:

- Inventory visibility
- Data consistency
- Scalability
- Support for future operational sites

# 4.11 Shipments

### Business Purpose

Stores shipment and delivery information for customer orders fulfilled through Harbour & Co.'s distribution network.

The shipments entity supports analysis of fulfilment performance, delivery reliability and operational efficiency across the e-commerce supply chain.

This table enables Harbour & Co. to monitor whether its omnichannel fulfilment operations are meeting customer expectations as digital sales continue to grow.

### Primary Key

`shipment_id`

### Foreign Keys

`order_id`

References:

`orders(order_id)`


`warehouse_id`

References:

`warehouses(warehouse_id)`

### Columns

| Column | Data Type | Description |
|---|---|---|
| shipment_id | INT | Unique shipment identifier |
| order_id | INT | Associated customer order |
| warehouse_id | INT | Distribution centre responsible for fulfilment |
| shipment_date | DATE | Date order was dispatched |
| expected_delivery_date | DATE | Customer promised delivery date |
| actual_delivery_date | DATE | Date order was delivered |
| shipment_status | VARCHAR(30) | Current shipment lifecycle status |
| delivery_method | VARCHAR(50) | Delivery method used |

### Supports

- On-Time Delivery Analysis
- Fulfilment Performance Analysis
- Warehouse Performance Analysis
- Delivery Experience Analysis
- E-commerce Operations Optimisation

# 4.12 Purchase Orders

### Business Purpose

Stores procurement transactions between Harbour & Co. and its supplier network.

The purchase orders entity represents inventory replenishment requests made by Harbour & Co. to suppliers and supports analysis of procurement performance, supplier reliability and supply chain efficiency.

As a premium omnichannel retailer, effective supplier management is critical to maintaining product availability, controlling costs and supporting customer demand.

### Primary Key

`purchase_order_id`

### Foreign Keys

`supplier_id`

References:

`suppliers(supplier_id)`


`product_id`

References:

`products(product_id)`

### Columns

| Column | Data Type | Description |
|---|---|---|
| purchase_order_id | INT | Unique purchase order identifier |
| supplier_id | INT | Supplier responsible for fulfilling the order |
| product_id | INT | Product being purchased |
| order_date | DATE | Date purchase order was created |
| expected_delivery_date | DATE | Supplier committed delivery date |
| actual_delivery_date | DATE | Date inventory was received |
| quantity_ordered | INT | Number of units ordered |
| purchase_order_status | VARCHAR(30) | Current purchase order status |
| unit_cost | DECIMAL(10,2) | Cost per unit purchased from supplier |

### Supports

- Supplier Performance Analysis
- Procurement Analysis
- Supplier Lead Time Analysis
- Supply Chain Risk Assessment
- Inventory Replenishment Analysis

