# 🧾 Inventory Management CLI Application

This is a lightweight Inventory Management Command Line Interface (CLI) tool built with **Python** and **SQLAlchemy ORM**. It helps you manage products, categories, suppliers, and orders in a structured SQLite database — ideal for small retail businesses, educational projects, or as a backend prototype.

---

## 📦 Features

✅ Add, View, Update, and Delete Products  
✅ Manage Product Categories and Suppliers  
✅ Associate Multiple Suppliers to Products (Many-to-Many)  
✅ View Low Stock Items for Restocking  
✅ Track Orders and Order Items  
✅ Persistent storage using SQLite + SQLAlchemy ORM  
✅ Modularized structure with clean separation of models and CLI logic

---

## 🧱 Tech Stack

- **Language:** Python 3.x
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Project Structure:** Modular, OOP-based

---

## 📂 Project Structure

```plaintext
inventory-cli/
│
├── models/
│   ├── base.py                # SQLAlchemy Base declaration
│   ├── category.py            # Category ORM model
│   ├── product.py             # Product ORM model
│   ├── supplier.py            # Supplier ORM model
│   ├── order.py               # Order ORM model
│   ├── order_item.py          # OrderItem ORM model
│   └── product_supplier.py    # Association table (Many-to-Many)
│
├── cli/
│   └── app.py                 # Main CLI logic
│
├── inventory.db               # SQLite database (generated on first run)
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation

---
 installation
git clone https://github.com/yourusername/inventory-cli.git
cd inventory-cli
pip install -r requirements.txt
