#9.Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.

list=["kolhapur","pune","sangali","satara","mumbai"]

city=input("enter the city name:")
if city in list:
    print("valid city")
else:
    print("invalid city name")