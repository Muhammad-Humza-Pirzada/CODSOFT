# Task 1

# items list in which items will be added by users
item = [
    
]

# The function of add items
def addItem(add_item):
    item.append(add_item)
    print("Item added successfully")
    

# the function of delete items 
def deleteItem(delete_item):
    if delete_item >= 0 and delete_item < len(item):
        delete_item = item.pop(delete_item)
        print(f'Deleted Task: {delete_item}')
    else:
        print("Invalid Index!")


# the function of display item
def displayItem():
    if len(item) > 0:
        print("Todo List")
        for index, add_item in enumerate(item):
            print(f'{index + 1}. {add_item}')

    else:
        print("Todo list in empty")
        

# condition  
while True:
    try:
        print("\n Choose option that you want to do.")
        print("Choose 1 to Add Item. ")
        print("Choose 2 to Delete Item. ")
        print("Choose 3 to Display all Items. ")
        print("Choose 4 to Exit. ")
        
        choise = int(input("Enter your choice: "))

        
        if choise == 1:
            add_item = input("Add Item: ")
            addItem(add_item)
        elif choise == 2:
            delete_item = int(input("Select number to Delete Item: ")) - 1
            deleteItem(delete_item)
        elif choise == 3:
            displayItem()
        elif choise == 4:
            print("You have exit from Application:")
            print("Thank you.....")
            break
        else:
            print("Invalid number please try again")
    except:
        print("Invalid Number please try again.")
    