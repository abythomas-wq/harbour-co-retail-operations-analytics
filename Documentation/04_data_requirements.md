# Harbour & Co. Retail Operations Analytics

# Data Requirements Document

## 1. Purpose

This document defines the data requirements needed to support the business objectives, analytical requirements and KPI framework for Harbour & Co. Retail Operations Analytics.

The requirements have been derived from Project Horizon's objectives and stakeholder needs.

The document provides the foundation for designing the relational data model required to analyse retail operations, supply chain performance and digital transformation outcomes.

---

# 2. Data Requirement Principles

The data model should:

- Support operational performance analysis
- Enable accurate KPI calculation
- Maintain relationships between business processes
- Support historical analysis
- Allow scalable reporting through SQL and Tableau

---

# 3. Required Data Domains

The analytics solution requires data across the following business domains:

| Data Domain | Business Purpose |
|---|---|
| Customers | Understand customer behaviour and value |
| Products | Analyse product and category performance |
| Sales Orders | Measure commercial performance |
| Inventory | Analyse stock availability and efficiency |
| Suppliers | Evaluate supplier performance |
| Warehouses | Analyse fulfilment operations |
| Shipments | Measure delivery performance |
| Stores | Support omnichannel analysis |

---

# 4. Customer Data Requirements

## Business Purpose

To understand customer purchasing behaviour, retention and channel engagement.

## Required Data

| Attribute | Purpose |
|---|---|
| Customer ID | Unique customer identification |
| Customer demographics | Customer segmentation |
| Registration date | Customer lifecycle analysis |
| Location | Regional analysis |
| Customer segment | Value analysis |

## Supports KPIs

- Customer Retention Rate
- Customer Lifetime Value
- Channel Performance

---

# 5. Product Data Requirements

## Business Purpose

To analyse product performance, category contribution and inventory demand.

## Required Data

| Attribute | Purpose |
|---|---|
| Product ID | Product identification |
| Product name | Reporting |
| Category | Category analysis |
| Supplier | Supply chain analysis |
| Cost price | Profitability analysis |
| Selling price | Revenue analysis |

## Supports KPIs

- Revenue
- Category Revenue Contribution
- Inventory Performance

---

# 6. Sales Order Data Requirements

## Business Purpose

To understand commercial performance across physical and digital channels.

## Required Data

| Attribute | Purpose |
|---|---|
| Order ID | Transaction identification |
| Customer ID | Customer analysis |
| Order date | Sales trends |
| Sales channel | Channel comparison |
| Store ID | Store performance |
| Order value | Revenue calculation |

## Supports KPIs

- Revenue
- Average Order Value
- Channel Performance

---

# 7. Inventory Data Requirements

## Business Purpose

To understand stock availability, inventory efficiency and working capital management.

## Required Data

| Attribute | Purpose |
|---|---|
| Product ID | Product-level inventory analysis |
| Location ID | Stock distribution analysis |
| Stock quantity | Availability analysis |
| Inventory date | Historical trends |
| Stock movement | Inventory flow analysis |

## Supports KPIs

- Inventory Turnover
- Stock Availability Rate
- Inventory Ageing

---

# 8. Supplier Data Requirements

## Business Purpose

To measure supplier reliability and identify supply chain risks.

## Required Data

| Attribute | Purpose |
|---|---|
| Supplier ID | Supplier identification |
| Supplier name | Reporting |
| Purchase order date | Lead time calculation |
| Expected delivery date | Performance measurement |
| Actual delivery date | Reliability measurement |

## Supports KPIs

- Supplier On-Time Delivery Rate
- Supplier Lead Time

---

# 9. Warehouse Data Requirements

## Business Purpose

To analyse fulfilment operations and distribution efficiency.

## Required Data

| Attribute | Purpose |
|---|---|
| Warehouse ID | Location identification |
| Warehouse region | Operational comparison |
| Capacity | Efficiency analysis |
| Processing capability | Operational analysis |

## Supports KPIs

- Order Processing Time
- Fulfilment Performance

---

# 10. Shipment Data Requirements

## Business Purpose

To understand delivery performance and customer experience.

## Required Data

| Attribute | Purpose |
|---|---|
| Shipment ID | Shipment tracking |
| Order ID | Order relationship |
| Dispatch date | Processing analysis |
| Delivery date | Delivery performance |
| Carrier | Delivery partner analysis |

## Supports KPIs

- On-Time Delivery Rate
- Delivery Performance

---

# 11. Store Data Requirements

## Business Purpose

To support omnichannel analysis by connecting physical stores with digital operations.

## Required Data

| Attribute | Purpose |
|---|---|
| Store ID | Store identification |
| Location | Regional analysis |
| Store type | Performance comparison |
| Opening date | Store lifecycle analysis |

## Supports KPIs

- Store Performance
- Channel Performance

---

# 12. Data Quality Requirements

The dataset should include validation checks for:

| Validation Area | Example Check |
|---|---|
| Completeness | Required fields populated |
| Accuracy | Valid dates and values |
| Consistency | Matching IDs across tables |
| Integrity | Valid relationships between entities |

---

# 13. Data Model Considerations
The database design should follow a relational approach.

Key relationships include:

Customer → Orders → Order Items → Products

Products → Suppliers

Products → Inventory → Locations

Orders → Shipments → Delivery Performance

This structure will enable SQL-based analysis and Tableau reporting.
