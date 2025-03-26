#!/usr/bin/env python3

print("\nTemperature Conversion Utility\n")
print("Converts temperatures between Celsius and Fahrenheit")

temperatures = []
converted_temps = []

while True:
    user_input = input("Enter a temperature to convert (or 'done' to finish):\n>>> ")

    if user_input.lower() == 'done':
        break

    try:
        temp = float(user_input)
        temperatures.append(temp)
    except ValueError:
        print(f"'{user_input}' is not a valid temperature, it has been ignored")

for temp in temperatures:
    converted_temp = (temp * 9/5) + 32
    converted_temps.append(converted_temp)

print("\nOriginal Temperatures (Celsius):", temperatures)
print("Converted Temperatures (Fahrenheit):", converted_temps)
