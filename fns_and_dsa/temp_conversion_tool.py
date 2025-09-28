fahrenheit_to_celsius_factor = 5/9
celsius_to_fahrenheit_factor = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * fahrenheit_to_celsius_factor
def convert_to_fahrenheit(celsius):
    return (celsius * celsius_to_fahrenheit_factor) + 32

temp = input("Enter the temperature to convert: ")
try:
    temp = float(temp)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == "F":
        print(f"{temp}°F is {convert_to_celsius(temp)}°C")
    elif unit == "C":
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
    else:
        print("Invalid temperature unit, enter 'C' or 'F'.")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
