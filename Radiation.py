
def deviation(data):

    #calculate the average
    list_length = len(data)

    average = sum(data)/ len(data)

    # Calculate the squared differences from the mean
    squared_diff = []
    for x in data:
        squared_diff.append((x - average) ** 2)
    
    #Calculate the variance (average of squared differences)
    variance = sum(squared_diff) / list_length

    #Calculate the standard deviation (square root of variances)
    deviation = variance ** 0.5

    return deviation


list = []
counter = 1
user_number_of_radiation_levels = int(input("Enter the number of radiation levels you want to enter: "))
for i in range(0, user_number_of_radiation_levels):
    element = int(input(f"Enter the radiation level number {counter} : "))
    counter += 1
    list.append(element)

    
print(deviation(list))





    # city_center = [22,19,20,31,28]
    # industrial_zone = [35,32,30,37,40]
    # residential_district = [15,12,18,20,14]
    # rural_outskirts = [9,13,16,14,7]
    # downtown = [25,218,22,21,26]