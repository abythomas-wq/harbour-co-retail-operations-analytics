SwiftFulfil Operations Analytics Project

End-to-End Data Analytics System for Business Performance & Fulfilment Optimisation

Executive Summary

This project simulates a real-world fulfilment and retail operations environment, designed to demonstrate an end-to-end analytics workflow from raw relational data to actionable business insights.

A structured SQL database was developed to model customers, orders, products, warehouses, and shipments. This was then analysed using SQL and Python to generate performance metrics, identify operational trends, and build a dashboard for decision-making.

The final output delivers insights into revenue performance, customer behaviour, and fulfilment efficiency, supported by strategic recommendations aimed at improving operational effectiveness and business growth.


Business Problem

Modern fulfilment operations require integrated visibility across sales, customers, and logistics. However, fragmented data systems often lead to:

* Limited visibility into revenue drivers
* Inefficient fulfilment tracking
* Poor understanding of customer behaviour
* Delayed decision-making due to siloed data

This project addresses these challenges by building a unified analytical system.

Data Source & Database Design

A relational database was designed to simulate a fulfilment ecosystem.

Core Design Principles

* Relational schema ensuring data integrity
* Normalised structure (eliminating redundancy)
* Primary & foreign key relationships
* Scalable structure for analytical querying

Key Entities

* Customers → stores customer profile data
* Orders → transaction-level records
* Order_Items → line-level product details
* Products → product catalogue
* Warehouses → fulfilment centres
* Shipments → delivery tracking information

Relationship Logic

* Customers → Orders (1-to-many)
* Orders → Order_Items (1-to-many)
* Products → Order_Items (many-to-one)
* Orders → Shipments (1-to-1 or 1-to-many depending on fulfilment flow)
* Warehouses → Shipments (fulfilment origin tracking)

This structure enables granular analysis of revenue, product demand, and fulfilment performance.

Data Dictionary

A structured data dictionary was developed to define:

* Field names
* Data types
* Primary/foreign keys
* Business meaning of each attribute

This ensures clarity, maintainability, and scalability of the dataset for future development.

Data Cleaning & Transformation

Data preparation was carried out using SQL and Python to ensure analytical accuracy.

Key transformations included:

* Standardising date formats for time-series analysis
* Handling missing and inconsistent values
* Aggregating transactional data for KPI generation
* Creating derived metrics (e.g., revenue per order, monthly sales)
* Structuring data for dashboard visualisation

KPI Design & Analytics Logic

The following KPIs were developed to evaluate business performance:

* Total Revenue
* Monthly Revenue Trend
* Average Order Value (AOV)
* Customer Acquisition Trend
* Product Performance
* Fulfilment / Shipping Efficiency

Each KPI was designed to support decision-making across sales, operations, and strategy.


Dashboard Overview

The dashboard provides a consolidated view of business performance, including:

* Revenue trends over time
* Customer behaviour patterns
* Product-level performance
* Operational fulfilment insights

The dashboard enables stakeholders to move from raw data to actionable insights within seconds.

(Insert dashboard screenshots here in GitHub)


Strategic Recommendations

Based on analytical findings, the following strategic improvements were identified:

* Optimise inventory allocation based on demand patterns
* Improve customer retention through targeted segmentation
* Enhance fulfilment efficiency by analysing warehouse performance
* Focus on high-performing product categories to maximise revenue
* Monitor seasonal trends to improve forecasting accuracy

These recommendations aim to improve both operational efficiency and revenue growth.


Conclusion

This project demonstrates an end-to-end data analytics workflow, covering database design, data transformation, KPI development, and business intelligence reporting.

It showcases the ability to translate raw operational data into structured insights that support strategic decision-making.

The system design reflects real-world analytical workflows used in business intelligence and operations analytics environments.


Tools & Technologies

* SQL (MySQL) – Database design & querying
* Python (Pandas) – Data transformation & analysis
* Excel – Initial exploration & validation
* Data Visualisation Dashboard – KPI reporting layer
* GitHub – Project documentation & version control