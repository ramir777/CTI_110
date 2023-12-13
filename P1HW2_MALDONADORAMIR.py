#manipulating strings nd integers
#10-09-2023
#CTI-110 P1HW2 - Travel Expense
#Ramir Maldonado-Hernandez

print("this program calculates and displays travel expenses")

#Get input user
budget = int(input("Enter budget: "))

destination = input ("Enter your travel destination: ")

#Get input from user
gas = int(input("how much do you think you will spend on gas?: "))

#Get input from user
accomodation_hotel = int(input("how much will you need for accomodation/hotel?: "))

#Get input from user
food = int(input("how much do you need for food?: "))

print("------------Travel Expenses------------")

print("location:", destination)

print("Initial Budget:",budget)
      
print("Fuel:",gas)     

print("accomodation:",accomodation_hotel)

print("food:",food)

print("Remaining Balance:",budget-gas-accomodation_hotel-food)



