#A mock banking system that deposits and withdraws funds

correct_username = "1"
correct_password = "1"

balance = 0.0
logged_in = False

#Get the username and password

class InsufficientFundsError(Exception):
    def __init__(self, message = "Insufficient Funds. Withdraw amount exceeds balance!!!"):
        super().__init__(message)

while not logged_in:
    username = input("Enter username : ")
    password = input("Enter password : ")

    if username == correct_username and password == correct_password:
        print("Login successful!\n")
        logged_in = True
    else:
        print("Incorrect username or password! Please try again")

while True:
    try:

        print(f"Hi {username}, your current balance is £{balance}")
        print('''
            1 - Deposit Funds
            2 - Withdraw Funds
            3 - Exit
        ''')

        choice = input('''Choose your option : ''')
        
        if choice == "1":
            #Ask for input from user, increment and print the balance
            amount = float(input("Enter the deposit amount: "))
            if amount > 3000:
                print("Warning. You cannot deposit more than £3000 at a time!")
            else:
                balance += amount
            print(f"New balance is {balance}\n")
        elif choice == "2":
            #Ask for input from user, decrement and print the balance
            amount = float(input("Enter the deposit amount: "))
            if amount > balance:
                InsufficientFundsError
                # print("Insufficient Funds. Withdraw Cancelled!!!")
            else:
                balance -= amount
            print(f"New balance is {balance}\n")
        elif choice == "3":
            #output final balance and log off
            print(f"Final balance is {balance}")
            print("Goodbye!")
            logged_in = False
            break
        else:
            print("Invalid choice. Enter option 1, 2 or 3.\n")
    except:
        print("There is something wrong with your input. Try again")