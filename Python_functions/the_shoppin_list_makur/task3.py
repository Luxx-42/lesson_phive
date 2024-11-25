# Task 3 print out entire shop list
def display_list(total_list):
    if total_list:
        print("Here is your shopping list:")
        for i, item in enumerate(total_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")