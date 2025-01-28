####Omar Cooper
#### Rainfall Calculator




#### This program will prompt the user for the rainfall for each month, then calculate and display the highest and lowest amounts
import math
def rainfall():
#define a list of months
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    months_rain = []
#Promt inputs of rain for each month
    x = 0
    for m in months:
        user_input = int(input(f"Please enter rainfall for {months[x]}: "))
        while user_input < 0:
            user_input = int(input(f"Sorry the value must be 0 or larger. Please try again: "))
        months_rain.append(user_input)
        x += 1
#Calculate and display sum
    sum_rain = sum(months_rain)
    print(f"The amount of rainfall wass {sum_rain} inches of rain that year.")
#Calculate and display average
    avg_rain = sum(months_rain) / len(months)
    print(f"The average amount of rainfall wass {avg_rain:.2f} inches of rain that year.")
#Calculate months with highest and lowest rainfall
    print(f"The largest amount of rain was {max(months_rain)} inches.")
    print(f"The highest rainfall month is:",months[months_rain.index(max(months_rain))],'.')
    print(f"The smallest amount of rain was {min(months_rain)} inches.")
    print(f"The lowest rainfall month is:",months[months_rain.index(min(months_rain))],'.')

rainfall()

