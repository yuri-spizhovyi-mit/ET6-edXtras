#!/usr/bin/env python3

class TemperatureConverter:
    def __init__(self):
        self.temperatures = []
        self.converted_temps = []

    def gather_temperatures(self, prompt: str = 'Enter a temperature'):
        while True:
            user_input = input(prompt)
            
            if user_input.lower() == 'done':
                break
            
            try:
                temp = float(user_input)
                self.temperatures.append(temp)
            except ValueError:
                print(f"'{user_input}' is not a valid temperature, it has been ignored")

    def convert_to_fahrenheit(self):
        self.converted_temps = [(temp * 9/5) + 32 for temp in self.temperatures]

    def main(self):
        print("\nTemperature Conversion Utility\n")
        print("Converts temperatures between Celsius and Fahrenheit")

        self.gather_temperatures("Enter a temperature to convert (or 'done' to finish):\n>>> ")
        self.convert_to_fahrenheit()

        print("\nOriginal Temperatures (Celsius):", self.temperatures)
        print("Converted Temperatures (Fahrenheit):", self.converted_temps)

converter_1 = TemperatureConverter()
converter_1.main()

converter_2 = TemperatureConverter()
converter_2.main()
