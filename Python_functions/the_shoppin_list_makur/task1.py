def shopping_list_add(total_list, item):
    total_list.append(item)
    print(f"'{item}' has been added to your list.")

def remove_item(total_list, item):
    if item in total_list:
        total_list.remove(item)
        print(f"'{item}' has been removed from your list.")
    else:
        print(f"'{item}' is not in your shopping list.")

def display_list(total_list):
    if total_list:
        print("Here is your shopping list:")
        for i, item in enumerate(total_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")
    
total_list = []

while True:
    add_2_shoppingList = input("Add or remove items on your list: (Enter 'add' for add, enter 'remove' to remove, or enter'q' to quit): ")

    if add_2_shoppingList == "add":
        item = input("Enter the item you want to add: ")
        shopping_list_add(total_list, item)

    elif add_2_shoppingList == "remove":
        item = input("Enter the item you want to remove: ")
        remove_item(total_list, item)

    elif add_2_shoppingList == "view":
        display_list(total_list)

    elif add_2_shoppingList == "q":
        print("Exiting... Here is your final shopping list:")
        display_list(total_list)
        break

    else:
        print("Invalid input. Please enter 'add', 'remove', 'view', or 'q'.")