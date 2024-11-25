# Task 2 write def function to remove items from list
def remove_item(total_list, item):
    if item in total_list:
        total_list.remove(item)
        print(f"'{item}' has been removed from your list.")
    else:
        print(f"'{item}' is not in your shopping list.")