print("Hello, this is an Unit Converter!")
print("You can convert various types of measurements using this program.")
response = 'yes'
while (response == 'yes'):
    question = int(raw_input("What do you want to do? \n"
                             "Press 1 to convert from Fahrenheit to Celsius, \n"
                             "Press 2 to convert from Celsius to Fahrenheit, \n"
                             "Press 3 to convert from Meters to Yards, \n"
                             "Press 4 to convert from Yards to Meters, \n"
                             "Press 5 to convert from Kilometers to Miles, \n"
                             "Press 6 to convert from Miles to Kilometers, \n"))
    def fahrenheit_to_celsius(x):
        return (x - 32) * 5 / 9

    def celsius_to_fahrenheit(x):
        return x * 9 / 5 + 32

    def meters_to_yards(x):
        return x / .9144

    def yards_to_meters(x):
        return x * .9144

    def kilo_to_mils(x):
        return x / 1.6093442

    def mile_to_kilo(x):
        return x * 1.609344

    if (question == 1):
        temp1 = int(raw_input("Enter the temperature in Fahrenheit: "))
        result1 = fahrenheit_to_celsius(temp1)
        print("The temperature in Celsius is: " + str(result1))
    elif (question == 2):
        temp2 = int(raw_input("Enter the temperature in Celsius: "))
        result2 = celsius_to_fahrenheit(temp2)
        print("The temperature in Fahrenheit is: " + str(result2))
    elif (question == 3):
        con1 = float(raw_input("Enter the number of meters: "))
        result3 = meters_to_yards(con1)
        print("The number of Yards: " + str(round(result3,3)))
    elif (question == 4):
        con2 = float(raw_input("Enter the number of yards: "))
        result4 = yards_to_meters(con2)
        print("The number of Meters: " + str(round(result4,3)))
    elif (question == 5):
        con3 = int(raw_input("Enter the number of kilometers: "))
        result5 = kilo_to_mils(con3)
        print("The number of miles: " + str(result5))
    elif (question == 6):
        con4 = int(raw_input("Enter the number of miles: "))
        result6 = mile_to_kilo(con4)
        print("The number of kilometers: " + str(result6))
    else:
        print("Please pick a number between 1 - 6!")
        response = 'yes'

    king = raw_input("Would you like to continue? 'y' = Yes and 'n' = No ").upper()
    if (king == "Y"):
        response = 'yes'
    elif (king == "N"):
        response = 'no'
