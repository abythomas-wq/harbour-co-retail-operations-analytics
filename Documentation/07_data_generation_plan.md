# Harbour & Co. Retail Operations Analytics

# Data Generation Plan

## 1. Purpose

This document defines the approach for generating synthetic operational data for Harbour & Co. Retail Operations Analytics.

All data used within this project is simulated and designed to represent a realistic premium UK omnichannel retailer.

The purpose of the generated dataset is to support analysis of:

- Retail sales performance
- Inventory efficiency
- Fulfilment operations
- Supplier performance
- Customer behaviour
## 2. Data Generation Principles

The synthetic dataset will follow realistic retail operating assumptions.

The data generation approach will prioritise:

- Logical relationships between entities
- Referential integrity
- Realistic business behaviour
- Analytical usefulness
- Data quality validation

Generated data should reflect the operational complexity of a large premium retailer rather than random numerical values.
## 3. Dataset Scope

The dataset will represent three years of Harbour & Co. operations.

Analysis Period:

January 2023 - December 2025

The dataset will include:

| Entity | Approximate Volume |
|---|---:|
| Customers | 50,000 |
| Products | 2,000 |
| Suppliers | 250 |
| Stores | 60 |
| Warehouses | 3 |
| Locations | 63 |
| Orders | 250,000 |
| Order Items | 750,000 |
| Inventory Snapshots | 500,000+ |
| Shipments | 250,000 |
| Purchase Orders | 50,000 |
## 4. Business Data Rules

The generated dataset will follow defined business rules to simulate realistic retail behaviour.

### Sales Channel Distribution

Orders will be distributed across:

| Channel | Approximate Share |
|---|---:|
| Store | 50% |
| Online | 40% |
| Click & Collect | 10% |

Online sales will demonstrate growth over the three-year period to reflect Harbour & Co.'s digital transformation strategy.
### Customer Behaviour

Customer segments will include:

| Segment |
|---|
| Premium |
| Regular |
| Occasional |

Premium customers will have:

- Higher average order value
- Higher purchase frequency
- Greater loyalty engagement
### Product Distribution

Products will be categorised across:

| Category |
|---|
| Womenswear |
| Menswear |
| Home |
| Beauty & Wellness |
| Food & Lifestyle |

Product pricing will reflect a premium retail positioning.
### Operational Challenges

The dataset will intentionally include realistic operational variation.

Examples:

- Some suppliers will have delayed deliveries
- Some products will experience stock shortages
- Online orders will have longer fulfilment journeys than store purchases
- Demand patterns will vary by category and season

### Data Generation Order

1. Locations
2. Stores
3. Warehouses
4. Suppliers
5. Products
6. Customers
7. Orders
8. Order Items
9. Inventory Snapshots
10. Shipments
11. Purchase Orders

Reason:
Tables are generated according to foreign key dependencies.
Master entities are created before transactional entities.
