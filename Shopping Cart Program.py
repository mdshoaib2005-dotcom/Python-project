#Exercise 2 Shopping Cart Program

item = input("What item would you like?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many items would you like?: "))

TotalPrice = price * quantity
print(f"You have bougth {quantity} x {item}")
print(f"Total price is Rs{TotalPrice}")
