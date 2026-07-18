import requests

BASE_URL = "http://127.0.0.1:5000"


def menu():
    print("\n===== Inventory Management System =====")
    print("1. View All Items")
    print("2. View One Item")
    print("3. Add Item")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Search Items")
    print("7. View Low Stock")
    print("8. Import Product from OpenFoodFacts")
    print("9. Exit")


while True:

    menu()

    choice = input("\nChoose an option: ")

    # ----------------------------
    # View All
    # ----------------------------
    if choice == "1":

        response = requests.get(f"{BASE_URL}/items")

        print("\nInventory:\n")

        for item in response.json():
            print(item)

    # ----------------------------
    # View One
    # ----------------------------
    elif choice == "2":

        item_id = input("Item ID: ")

        response = requests.get(f"{BASE_URL}/items/{item_id}")

        print(response.json())

    # ----------------------------
    # Add Item
    # ----------------------------
    elif choice == "3":

        data = {
            "name": input("Name: "),
            "barcode": input("Barcode: "),
            "quantity": int(input("Quantity: ")),
            "price": float(input("Price: "))
        }

        response = requests.post(
            f"{BASE_URL}/items",
            json=data
        )

        print(response.json())

    # ----------------------------
    # Update Item
    # ----------------------------
    elif choice == "4":

        item_id = input("Item ID: ")

        print("Leave blank if unchanged.\n")

        data = {}

        name = input("New Name: ")

        if name:
            data["name"] = name

        barcode = input("New Barcode: ")

        if barcode:
            data["barcode"] = barcode

        quantity = input("New Quantity: ")

        if quantity:
            data["quantity"] = int(quantity)

        price = input("New Price: ")

        if price:
            data["price"] = float(price)

        response = requests.patch(
            f"{BASE_URL}/items/{item_id}",
            json=data
        )

        print(response.json())

    # ----------------------------
    # Delete Item
    # ----------------------------
    elif choice == "5":

        item_id = input("Item ID: ")

        response = requests.delete(
            f"{BASE_URL}/items/{item_id}"
        )

        print(response.json())

    # ----------------------------
    # Search
    # ----------------------------
    elif choice == "6":

        name = input("Search Name: ")

        response = requests.get(
            f"{BASE_URL}/search?name={name}"
        )

        for item in response.json():
            print(item)

    # ----------------------------
    # Low Stock
    # ----------------------------
    elif choice == "7":

        response = requests.get(
            f"{BASE_URL}/low-stock"
        )

        print("\nLow Stock Items\n")

        for item in response.json():
            print(item)

    # ----------------------------
    # OpenFoodFacts
    # ----------------------------
    elif choice == "8":

        barcode = input("Barcode: ")

        response = requests.post(
            f"{BASE_URL}/import/{barcode}"
        )

        print(response.json())

    # ----------------------------
    # Exit
    # ----------------------------
    elif choice == "9":

        print("\nGoodbye!\n")

        break

    else:

        print("Invalid option.")