import json
import os

LIBRARY_MANAGEMENT = "library.json"

def load_inventory():
    if not os.path.exists(LIBRARY_MANAGEMENT):
        return {}
    with open (LIBRARY_MANAGEMENT, 'r') as f:
        return json.load(f)
    
def save_inventory(inventory):
    with open (LIBRARY_MANAGEMENT, 'w') as f:
        json.dump(inventory, f, indent=4)

def add_item(inventory):
    book_id = input("Enter the Book ID: ")
    if book_id in inventory:
        print('Book already exits!')
        return
    name = input("Enter the name of the book: ")
    author = input("Author of the book: ")
    price = int(input("Price of the book: "))
    inventory[book_id] = {"name" : name, "author" : author, "price" : price}
    print("Added book sucessfully!!!")

def update_item(inventory):
    book_id = input("Enter the book id to be updated: ")
    if book_id not in inventory:
        print("Item is not available in the inventory!!!")
        return
    # book_id = input(f"Enter the new book id {inventory[book_id]}: "
    name = input(f"Enter new name of the book or press enter to skip ({inventory[book_id]['name']}): ")
    author = input(f"Enter the new author or press enter to skip ({inventory[book_id]['author']}): ")
    price = input(f"Enter the new price or press enter to skip ({inventory[book_id]['price']}): ")
    inventory[book_id] = {
        "name": name or inventory[book_id]['name'],
        "author": author or inventory[book_id]['author'],
        "price": int(price) if price else inventory[book_id]['price']
    }
    print("Data updated successfully!!!")

def delete_item(inventory):
    book_id = input("Enter the book id to be deleted: ")
    if book_id in inventory:
        del inventory[book_id]
        print("Book deleted successfully!!!")
    else:
        print("Item not found!!!")

def view_items(inventory):
    if not inventory:
        print("Inventory Enpty!!!")
        return
    print("{:<10} {:<20} {:<20} {:<10}".format("ID", "Name", "Author", "Price"))
    for book_id, details in inventory.items():
        print("{:<10} {:<20} {:<20} {:<10}".format(book_id, details['name'], details['author'], details['price']))

def main():
    inventory = load_inventory()
    while True:
        print("\n****************** LIBRARY MANAGEMENT SYSTEM *********************")
        print("1. View inventory")
        print("2. Add books")
        print("3. Update books")
        print("4. Delete book")
        print("5. Save and Exit")
        choice = input("\n Enter your choice: ")
        if choice == "1":
            view_items(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            update_item(inventory)
        elif choice == "4":
            delete_item(inventory)
        elif choice == "5":
            save_inventory(inventory)
            print("Inventory saved. Exiting.")
            break
        else:
            print("Invalid choice. Try again!!!")
            
if __name__ == "__main__":
    main()