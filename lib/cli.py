
from models.base import Base
from models.category import Category
from models.product import Product
from models.customer import Customer
from models.supplier import Supplier
from models.order import Order
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///inventory.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def category_menu():
    while True:
        print("\n--- Category Menu ---")
        print("1. Add Category")
        print("2. View Categories")
        print("3. Delete Category")
        print("4. Find Category")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Name: ")
            description = input("Description: ")
            Category.create(session, name, description)
        elif choice == '2':
            for c in Category.get_all(session):
                print(c)
        elif choice == '3':
            id = int(input("Category ID to delete: "))
            cat = Category.find_by_id(session, id)
            if cat:
                cat.delete(session)
                print("Deleted.")
            else:
                print("Not found.")
        elif choice == '4':
            id = int(input("ID: "))
            cat = Category.find_by_id(session, id)
            print(cat or "Not found.")
        elif choice == '5':
            break

def product_menu():
    while True:
        print("\n--- Product Menu ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Delete Product")
        print("4. Find Product")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Name: ")
            description = input("Description: ")
            price = float(input("Price: "))
            qty = int(input("Stock quantity: "))
            category_id = int(input("Category ID: "))
            category = Category.find_by_id(session, category_id)
            if category:
                Product.create(session, name, description, price, qty, category)
            else:
                print("Invalid category ID")
        elif choice == '2':
            for p in Product.get_all(session):
                print(p)
        elif choice == '3':
            id = int(input("Product ID to delete: "))
            prod = Product.find_by_id(session, id)
            if prod:
                prod.delete(session)
                print("Deleted.")
            else:
                print("Not found.")
        elif choice == '4':
            id = int(input("ID: "))
            prod = Product.find_by_id(session, id)
            print(prod or "Not found.")
        elif choice == '5':
            break

def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Delete Customer")
        print("4. Find Customer")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            Customer.create(session, name, phone, email, address)
        elif choice == '2':
            for c in Customer.get_all(session):
                print(c)
        elif choice == '3':
            id = int(input("Customer ID to delete: "))
            cust = Customer.find_by_id(session, id)
            if cust:
                cust.delete(session)
                print("Deleted.")
            else:
                print("Not found.")
        elif choice == '4':
            id = int(input("ID: "))
            cust = Customer.find_by_id(session, id)
            print(cust or "Not found.")
        elif choice == '5':
            break

def supplier_menu():
    while True:
        print("\n--- Supplier Menu ---")
        print("1. Add Supplier")
        print("2. View Suppliers")
        print("3. Delete Supplier")
        print("4. Find Supplier")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Name: ")
            contact_person = input("Contact Person: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            Supplier.create(session, name, contact_person, phone, email, address)
        elif choice == '2':
            for s in Supplier.get_all(session):
                print(s)
        elif choice == '3':
            id = int(input("Supplier ID to delete: "))
            supp = Supplier.find_by_id(session, id)
            if supp:
                supp.delete(session)
                print("Deleted.")
            else:
                print("Not found.")
        elif choice == '4':
            id = int(input("ID: "))
            supp = Supplier.find_by_id(session, id)
            print(supp or "Not found.")
        elif choice == '5':
            break

def order_menu():
    while True:
        print("\n--- Order Menu ---")
        print("1. Add Order")
        print("2. View Orders")
        print("3. Delete Order")
        print("4. Find Order")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            customer_id = int(input("Customer ID: "))
            customer = Customer.find_by_id(session, customer_id)
            if not customer:
                print("Invalid customer ID")
                continue
            status = input("Status: ")
            total_amount = float(input("Total Amount: "))
            Order.create(session, customer, status, total_amount)
        elif choice == '2':
            for o in Order.get_all(session):
                print(o)
        elif choice == '3':
            id = int(input("Order ID to delete: "))
            order = Order.find_by_id(session, id)
            if order:
                order.delete(session)
                print("Deleted.")
            else:
                print("Not found.")
        elif choice == '4':
            id = int(input("ID: "))
            order = Order.find_by_id(session, id)
            print(order or "Not found.")
        elif choice == '5':
            break

def main():
    while True:
        print("\n=== Inventory CLI ===")
        print("1. Manage Categories")
        print("2. Manage Products")
        print("3. Manage Customers")
        print("4. Manage Suppliers")
        print("5. Manage Orders")
        print("6. Exit")
        option = input("Choose an option: ")

        if option == '1':
            category_menu()
        elif option == '2':
            product_menu()
        elif option == '3':
            customer_menu()
        elif option == '4':
            supplier_menu()
        elif option == '5':
            order_menu()
        elif option == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == '__main__':
    main()