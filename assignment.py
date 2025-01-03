
menu={'Bread': 40, 'Cookies': 80, 'Butter': 120,'Cheese': 180,'Yoghurt': 60}

cart=[]

while True:
    print("What do you want to do?\n")
    print("Enter 1 for viewing the items")
    print("Enter 2 for adding the items in cart")
    print("Enter 3 for updating the items in cart")
    print("Enter 4 for deleting the items in cart")
    print("Enter 5 for printing bill")
    print("Enter 6 to exit")

    n=int(input("Enter your choice:"))
    if n==1:
        print("Available MEnu Items:")
        for i,j in menu.items():
            print("Item Name:",i,"  ","Price:",j)

    elif n==2:
        item=input("Enter the Item Name to Add in the Cart:")
        if item in menu:
            q=int(input("enter the quantity:"))
            cart.append([item,q,menu[item],q*menu[item]])
            print(f"Item {item} added to the cart")
        else:
            print("Item Invalid")
    
    elif n==3:
        itemName=input("Enter the Item Name to Update:")
        for i in cart:
            if i[0]==itemName:
                q=int(input("Enter the Quantity to Update:"))
                i[1]=q
                i[3]=q*i[2]
                print("Updated Cart:")
                print(cart)

    elif n==4:
        itemName=input("Enter the item Name to remove:")
        for i in range(len(cart)):
            if cart[i][0]==itemName:
                cart.pop(i)
                print(f"Item {itemName} Removed")
                break
            else:
                print("Item not found")

    elif n==5:
        print("Your Shopping Bill:")
        if len(cart)<1:
            print("cart is empty")
        else:
            print("cart:",cart)

            for i in cart:
                total=i[3]
            print("Total Bill:",total)

    elif n==6:
        print("Thanks for Shopping")
        break
    else:
        print("enter valid choice")
