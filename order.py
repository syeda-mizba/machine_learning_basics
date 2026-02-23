user = {
    'name': None,
    'email': None,
    'phone': None,
    'payment_method' : None
}

user['name'] = input("Enter Name :")
user['email'] = input("Enter email: ")
user['phone'] = input("Enter phone: ")
print(user)

cart = []
total_price = 0.0
while True:
    item = input('Item name : ')
    price = float(input('Item price : '))
    cart_item = {
        'item': item, 'price': float(price)
    }

    cart.append(cart_item)
    total_price += price 

    print('continue?')
    choice =input()

    if choice == 'no':
        break
print("Total Price")
print(total_price)   

    
