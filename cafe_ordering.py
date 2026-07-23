menu={
    "Coffee":25,
    "Tea":20,
    "Milk":40,
    "Iced Cappachino": 50,
    "Latte": 40,
    "cookie": 20,
    "cake": 80,
    "Samosa":15,

}


access_numbers=[100,200,300,400,500,600]

cart=[]

class Employee:

    def __init__(self):
            self.access_no=int(input("Enter your access number:"))
            self.item=input("enter newly adding item name:")
            self.rate=int(input("enter new rate of item:"))


    def verification(self):
            print("Welcome to coffee corner employee portal")
            print("Access number:",self.access_no)

            if self.access_no not in access_numbers:
                print("Access denied")

            else:
                print("access granted", self.item)
                print("rate:", self.rate)
                menu[self.item] += self.rate

class AddItem:
    def __init__(self):
        self.item=input("enter item name to add in cart:")
        self.quantity=int(input("enter how much quantity:"))

    def cart(self):
        while True:
            print(self.item)
            print(self.quantity)
            if self.item in menu:
                cart.append(self.item)
                cost=menu[self.item] * self.quantity
                cart.append(cost)

                print("your item in cart ",cart)

                exit_clause=input("do you want to exit?(y/n):")
                if exit_clause=="y":
                    quit()

                else:
                    break

class Checkout:

    def checkout_total(self):
        total=0
        for item in cart:
            if type(item) == int:
                total+=item



        print(f'Your final checkout items and bill is {cart} \n and your total amount is {total} ')



while True:

    Welcome = input("""Welcome to Coffee Coner !!! \n
                     Menu:                 rate: \n
                      "Coffee":             25   \n
                      "Tea":                20   \n
                      "Milk":               40   \n
                      "Iced Cappachino":    50   \n
                      "Latte":              40   \n
                      "cookie":             20   \n
                      "cake":               20   \n
                      "Samosa":             15   \n

                      type "Employee " to access the employee feature and "add" \n
                       feature to add items to the cart and "checkout" !!""")


    if Welcome.lower() == "employee":
        active_employee=Employee()
        active_employee.verification()

    elif Welcome.lower() == "add":
        activate_cart = AddItem()
        activate_cart.cart()

    elif Welcome.lower() == "checkout":
        activate_checkout = Checkout()
        activate_checkout.checkout_total()

    else:
        print("invalid input")




