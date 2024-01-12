user_1 = input("User 1, make your move: ")
user_2 = input("User 2, make your move: ")

if user_1 == "Rock":
    if user_2 == "Rock":
        print("Tie!!!")
    elif user_2 == "Paper":
        print("user 2 wins with Paper over Rock!!!")
    elif user_2 == "Scissors":
        print("user 1 wins with Rock over Scissors!!!")
elif user_1 == "Paper":
    if user_2 == "Rock":
        print("user 1 wins with Paper over Rock!!!")
    elif user_2 == "Paper":
        print("Tie!!!")
    elif user_2 == "Scissors":
        print("user 2 wins with Scissors over Paper!!!")
elif user_1 == "Scissors":
    if user_2 == "Rock":
        print("user 2 wins with Rock over Scissors!!!")
    elif user_2 == "Paper":
        print("user 1 wins with Scissors over Paper")
    elif user_2 == "Scissors":
        print("Tie!!!")
else:
    print("Wrong input, try again")