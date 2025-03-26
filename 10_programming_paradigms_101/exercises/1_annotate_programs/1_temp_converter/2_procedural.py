#!/usr/bin/env python3

def gather_temperatures(prompt: str = 'Enter a temperature') -> list[float]:
    temperatures = []
    while True:
        user_input = input(prompt)
        
        if user_input.lower() == 'done':
            break
        
        try:
            temp = float(user_input)
            temperatures.append(temp)
        except ValueError:
            print(f"'{user_input}' is not a valid temperature, it has been ignored")
    
    return temperatures

def convert_to_fahrenheit(temperatures: list[float]) -> list[float]:
    return [(temp * 9/5) + 32 for temp in temperatures]

def main():
    print("\nTemperature Conversion Utility\n")
    print("Converts temperatures between Celsius and Fahrenheit")

    temperatures = gather_temperatures("Enter a temperature to convert (or 'done' to finish):\n>>> ")
    converted_temps = convert_to_fahrenheit(temperatures)

    print("\nOriginal Temperatures (Celsius):", temperatures)
    print("Converted Temperatures (Fahrenheit):", converted_temps)

main()
main()
