
#Calculates the cost of the hotel
def hotel_cost(num_nights):
    price_per_night = 50
    total_cost = num_nights*price_per_night
    return total_cost

#Calculates the cost of the flight
def plane_cost(city_flight):
    if city_flight == 1:
        flight_cost = 60
    elif city_flight == 2:
        flight_cost = 40
    elif city_flight == 3:
        flight_cost = 35
    elif city_flight == 4:
        flight_cost = 250
    elif city_flight == 5:
        flight_cost = 45
    else:
        raise ValueError("Please choose a valid number for the city.")
    return flight_cost

#Calculates the cost of the car rental
def car_rental(rental_days, num_nights):
    car_rent_price_per_day = 25

    #wrapping the code in both while loop and try except block
    #to prevent the logical error. 
    #Number of car rental days cannot be more than the number of nights to stay at the hotel
    while True:
        try:
            #rental_days = int(input("Please enter the number of days you want to rent a car: "))
            if rental_days <= num_nights:
                total_cost = car_rent_price_per_day * rental_days
                break
            else:
                print("Car rental days cannot exceed the number of nights to stay!!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return total_cost


#Calculates the total cost of the holiday by adding 
#hotel, plane, and car rental prices together, adn returning a sum
def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_cost = hotel_cost + plane_cost + car_rental
    return total_cost


#Printing prompts to give info to user
print("Welcome to the Holiday Cost Calculator.")
print("""Please choose from the following 5 cities: 
1 - London
2 - Istanbul
3 - Rome
4 - New York
5 - Berlin""")


# Asking user to choose which city they want to fly
# The code is wrapped in try except block, to handle error when input is not the given options
# Also, the code is in While loop, so that if the input is wrong, 
# user can be asked to enter input again, until they enter correct value
while True:
    try:
        city_flight = int(input("Please enter the city you will be flying to (enter the corresponding numbers for each city): "))
        if 1 <= city_flight <= 5:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


#Asking user to enter the number of nights they will stay
# The code is wrapped in try except block, to handle error when input is anything other than string
# Also, the code is in While loop, so that if the input is wrong, 
# user can be asked to enter input again, until they enter correct value
while True:
    try:
        num_nights = int(input("Please enter the number of nights you will be staying at the hotel: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")


#Asking user to enter the number of nights they will stay
# The code is wrapped in try except block, to handle error when input is anything other than string
# Also, the code is in While loop, so that if the input is wrong, 
# user can be asked to enter input again, until they enter correct value
while True:
    try:
        rental_days = int(input("Please enter the number of days you want to rent a car: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#printing the total cost at the end
print(f"Your total price for the holiday is: £{holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days, num_nights))}")
