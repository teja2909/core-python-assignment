def add_menu_item(menu,item):
    menu.append(item) if item not in initial_menu else print("Item is already on the menu!")
def remove_menu_item(menu,item):
    menu.remove(item) if item in initial_menu else print("Item is not on the menu!")
def check_menu_item(menu,item):
    return  f"{item} is available!" if item in initial_menu else f"{item} is not available"
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
print(initial_menu)
while True:
    print("\n Menu options\n 1.Add item to the menu\n 2.Remove item from the menu\n 3.Check for item on the menu\n 4.View the menu\n 5.Exit")
    choice=input("Enter an option(1-5): ")
    if choice=='1':
        add_item=input("Enter an item to add to the menu: ")
        add_menu_item(initial_menu,add_item)
        print("Updated menu:", initial_menu)
    elif choice=='2':
        remove_item=input("Enter an item to remove from the menu: ")
        remove_menu_item(initial_menu,remove_item)
        print("Updated menu:", initial_menu)
    elif choice=='3':
        check_item=input("Enter an item to check availability: ")
        print("Availability: ",check_menu_item(initial_menu,check_item))
    elif choice=='4':
        print("Current Menu: ",initial_menu)
    elif choice=='5':
        print("Have a great day!")
        break
    else:
        print("Invalid choice! Please select a valid option")




