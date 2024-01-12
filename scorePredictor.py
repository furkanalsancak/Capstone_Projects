
# Cricket match Score Predictor code

def score_Predictor():
    #Declaring variables and taking input from the user
    total_overs = input("Enter total overs: ")
    current_over = input("Enter current over : ")
    current_runs = input("Enter current score : ")

    #Converting
    convert_total_overs = int(total_overs)
    convert_current_over = int(current_over)
    convert_current_runs = int(current_runs)

    #formula for finding run rate
    run_rate = convert_current_runs / convert_current_over

    #formula for score predictor
    predictor = run_rate * convert_total_overs

    #printing runrate and score predictor
    print("\n----------------------")
    print(f"Run rate is : {round(run_rate, 2)}")
    print(f"Score predictor is : {round(predictor, 2)}")
    print("\n----------------------")


#Calling function
score_Predictor()