menu={
    1:{"name": "soda", "price": 20},
    2:{"name": "chips", "price": 10},
    3:{"name": "juice", "price": 30},
    4:{"name": "biscuit", "price": 40},
}
print("welcome to the vending Machine!\n")
while True:
    for key, item in menu.items():
        print(f"{key}:{item['name']}-{item['price']}")
    choose_item=int(input("enter the number you want to buy:"))
    if choose_item not in menu:
        print("invalid choice! please try again")
        continue
    if choose_item in menu:
        payment=int(input("enter the amount you want to insert"))
        if menu[choose_item]['price']<=payment:
            print("dispense the item")
            change=payment-menu[choose_item]['price']
            if change>0:
                print("your change is:", change)
        else:
            print("need more money")
            continue

    buy_again=input("DO you want to buy another item?(yes/no):")
    if buy_again!= "yes":
        print("thank you for using vending machine! have a nice day")
        break
    

    