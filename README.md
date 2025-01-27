# Store and Product Inventory Management System

This repository contains a series of assignments that progressively build a robust Store and Product Inventory Management System. The project is implemented using Python and incorporates object-oriented programming principles, data structures (like stacks), and efficient handling of store and product data. It is designed to simulate real-world inventory management scenarios.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Structure](#structure)
4. [Technologies Used](#technologies-used)
5. [Getting Started](#getting-started)

---

## Overview
This project is based on four interconnected assignments that demonstrate the management of store and product information using custom classes and a stack data structure. It supports operations like adding/removing products, maintaining data integrity, retrieving products by store IDs, and categorizing stores by even or odd IDs.

The goal is to emulate a simplified inventory system that could be used by a retail business to organize, manage, and retrieve product and store information efficiently.

---

## Features
### Assignment 1:
- Implementation of basic `Product`, `Store`, and `MyStore` classes.
- Core functionalities include adding products to stores, retrieving product details, and calculating inventory statistics.

### Assignment 2:
- Enhanced functionalities in the `Store` and `MyStore` classes.
- Improved data handling and organization within the store-product relationship.

### Assignment 3:
- Use of external CSV files to import store and product data.
- Extended functionalities, including automated parsing and integration of external data into the system.

### Assignment 4:
- Introduction of a `StackStorage` class to manage store and product data using a stack implemented via the `deque` module.
- Features include:
  - Adding/removing products and stores.
  - Handling of odd/even store categorization.
  - Efficient retrieval of products for specified stores.
  - Integrity preservation of stack data during operations.

---

## Structure
The repository consists of:
1. **Python Classes**: Core classes such as `Product`, `Store`, `MyStore`, and `StackStorage`.
2. **CSV Data**: A sample file (`asn4Inventory.csv`) used to simulate real-world store and product data.
3. **Driver Code**: Scripts to execute and test the functionalities of each assignment.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**: 
  - `collections.deque`: To implement stack functionalities.
  - `csv`: For data import and processing.

---

## Getting Started
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/store-inventory-management.git
   cd store-inventory-management
