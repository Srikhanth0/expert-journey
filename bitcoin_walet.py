balance= {}
history=[]


def walet():
    bitcoin = input("enter your bitcoin name")
    amount = int(input("enter your wallet amount"))
    if bitcoin not in balance:
        balance[bitcoin]=amount

    else:
        balance[bitcoin] = balance[bitcoin] + amount
    history.append(f"Deposited {amount} to {bitcoin}")

def withdraw(bitcoin):
    withdraw_amount = int(input("enter your withdrawal amount"))
    if withdraw_amount>balance[bitcoin]:
        print("insufficient funds")

    else:
        balance[bitcoin] = balance[bitcoin] - withdraw_amount
        history.append(f"withdrawn {withdraw_amount} from {bitcoin}")



while True:
    sign_in = int(input("welcome to the bitcoin walet \n"
                        " 1. press 1 if your a new user \n "
                        " 2. press 2 if your want to add to your walet \n "
                        " 3. press 3 to withdraw from walet \n"
                        " 4. press 4 to view history"))
    if sign_in==1:
        walet()
        query=input("type yes if you wanna view balance")
        if query.lower()=="yes":
            print(balance)

        else:
            pass

    elif sign_in==2:
        walet()
        pass

    elif sign_in==3:
        bitcoin = input("enter your bitcoin name")
        if bitcoin not in balance:
            print("no such bitcoin exists")
        else:
            withdraw(bitcoin)
            pass

    elif sign_in==4:
        print(history)


    else:
        print("Invalid choice")
        pass