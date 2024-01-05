import math


print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
user_calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed : ")


# for the interest option:
if user_calculation == "investment" or user_calculation == "Investment" or user_calculation == "INVESTMENT": #including as many types for user entry as possible
    # requesting all the values from the user for calculation
    deposit_money = int(input("Enter the amount of money you are depositing : "))
    interest_rate = int(input("Enter your interest rate (do not include '%'. Just the number): "))
    years_of_invest = int(input("Enter the number of years you plan to invest : "))
    interest_type = input("Enter whether you want 'simple' or 'compound' interest : ")
    if interest_type == "simple":
        # formula for simple investment
        # A = P *(1+r*t)
        r = interest_rate / 100     # ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered,then r is 0.08
        P = deposit_money           # ‘P’ is the amount that the user deposits
        t = years_of_invest         # ‘t’ is the number of years that the money is being invested
        A = P * (1 + r * t)         # total amount once the simple interest has been applied
        print("With simple interest:")
        # casting total amount to int first, then string, so that the number looks cleaner
        print(f"The total amount you will have after {t} years with {interest_rate}% interest rate each year is : £" + str( int(A) ))
    elif interest_type == "compound":
        # formula for compound investment
        # A = P * math.pow((1+r), t)
        r = interest_rate / 100     # ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered,then r is 0.08
        P = deposit_money           # ‘P’ is the amount that the user deposits
        t = years_of_invest         # ‘t’ is the number of years that the money is being invested
        A = P * math.pow((1+r), t)  # total amount once the compound interest has been applied
        print("With compound interest:")
        # casting total amount to int first, then string, so that the number looks cleaner
        print(f"The total amount you will have after {t} years with {interest_rate}% interest rate each year is approximately : £" + str( int(A) )) 
    else:
        print("Wrong input. Please run again!!!")


# for the bond option
if user_calculation == "bond" or user_calculation =="Bond" or user_calculation == "BOND": #including as many types for user entry as possible
    # requesting all the values from the user for calculation
    house_value = int(input("Enter the house value : "))
    interest_rate = int(input("Enter your interest rate (do not include '%'. Just the number): "))
    bond_repay_months = int(input("Enter the number of months you plan to take to repay the bond : "))
    # formula for bond repayment
    # repayment = (i * P)/(1 - (1 + i)**(-n))
    P = house_value # P is the present value of the house
    i = (interest_rate/100)/12 # i is the monthly interest rate, first divided by 100, then by 12 to achieve monthly rate
    n = bond_repay_months
    each_month_payment = (i * P)/(1 - (1 + i)**(-n))
    print("With bond repayment:")
    # casting monthly payment value to integer to get rid of float value
    print(f"the total amount you will have to repay each month is approximately {int(each_month_payment)}") # casting monthly payment value to integer to get rid of float value
else:
    print("Wrong input. Please run again!!!")
