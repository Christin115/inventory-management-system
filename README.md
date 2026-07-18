# Inventory Management System

## Overview

The Inventory Management System is a Flask REST API that allows users to manage inventory items using a SQLite database. The application supports full CRUD operations, searching inventory, identifying low-stock items, and importing product information from the OpenFoodFacts API using a barcode.

## Features

* Create inventory items
* View all inventory items
* View a single inventory item
* Update inventory items
* Delete inventory items
* Search inventory by product name
* Display low-stock items
* Import product information from OpenFoodFacts
* Duplicate barcode protection

## Technologies Used

* Python 3
* Flask
* Flask-SQLAlchemy
* SQLite
* Requests
* OpenFoodFacts API

## Installation

Clone the repository:

```bash
git clone https://github.com/Christin115/inventory-management-system.git
cd inventory-management-system
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

The API runs at:

```
http://127.0.0.1:5000
```

## API Endpoints

### Home

GET /

### Get All Items

GET /items

### Get One Item

GET /items/<id>

### Create Item

POST /items

### Update Item

PUT /items/<id>

### Delete Item

DELETE /items/<id>

### Search Items

GET /search?name=keyword

### Low Stock

GET /low-stock

### Import Product

POST /import/<barcode>

Example:

```
POST /import/0737628064502
```

## Example Response

```json
{
  "id": 1,
  "name": "Thai peanut noodle kit includes stir-fry rice noodles & thai peanut seasoning",
  "barcode": "0737628064502",
  "brand": "Simply Asia, Thai Kitchen",
  "category": "Cereals and their products, Noodles, Rice Noodles",
  "package_size": "155 g",
  "origin": "Thailand",
  "quantity": 1,
  "price": 0.0
}
```

## Project Structure

```
inventory-management-system/
│
├── app.py
├── cli.py
├── config.py
├── requirements.txt
├── README.md
├── models/
├── routes/
├── services/
├── tests/
└── instance/
```

## Author

Christin Jordan
