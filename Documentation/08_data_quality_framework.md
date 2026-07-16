# Harbour & Co. Retail Operations Analytics

# Data Quality Framework

## 1. Purpose

This document defines the data quality approach used to validate the synthetic dataset created for Harbour & Co. Retail Operations Analytics.

The objective is to ensure that analytical outputs are based on accurate, consistent and reliable data.

The framework focuses on:

- Data completeness
- Data accuracy
- Data consistency
- Referential integrity
- Business rule validation
## 2. Data Quality Principles

The dataset will be assessed against the following quality dimensions:

| Dimension | Description |
|---|---|
| Completeness | Required fields contain valid values |
| Accuracy | Data reflects realistic business scenarios |
| Consistency | Values follow defined business rules |
| Integrity | Relationships between tables remain valid |
| Validity | Data conforms to expected formats and ranges |

## 3. Referential Integrity Checks

The following relationships will be validated:

| Check | Expected Result |
|---|---|
| Every order has a valid customer | No orphan records |
| Every order item has a valid order | No orphan records |
| Every order item has a valid product | No orphan records |
| Every inventory record has a valid product | No orphan records |
| Every shipment has a valid order | No orphan records |
| Every purchase order has a valid supplier | No orphan records |

## 4. Business Rule Validation

### Order Validation

Rules:

- Order dates must fall within the analysis period
- Order values must be greater than zero
- Completed orders must have associated shipments where applicable

---

### Shipment Validation

Rules:

- Shipment date cannot occur before order date
- Actual delivery date cannot occur before shipment date
- Delivery dates must be logically valid

---

### Inventory Validation

Rules:

- Inventory quantities cannot be negative
- Products must exist in the product catalogue
- Inventory locations must exist in the locations table

---

### Financial Validation

Rules:

- Order revenue must reconcile with order item values

Formula:

Total Order Value =
SUM(Order Item Revenue)

## 5. Data Quality Monitoring Approach

Data validation checks will be performed before:

- Loading data into MySQL
- Creating analytical SQL views
- Connecting Tableau dashboards

Any identified issues will be documented and resolved before analysis.