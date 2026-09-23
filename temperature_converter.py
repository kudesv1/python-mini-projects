def celsius_to_fahrenheit():
    while True:
        try:
            celsius_temp = float(input("Enter temp in Celsius: "))
            fahrenheit_temp = celsius_temp * 9/5 + 32
            print(f"Temp in Fahrenheit: {fahrenheit_temp}")
            break
        except ValueError:
            print("Please, enter a valid number")

def fahrenheit_to_celsius():
    while True:
        try:
            fahrenheit_temp = float(input("Enter temp in Fahrenheit: "))
            celsius_temp = (fahrenheit_temp - 32) * 5/9
            print(f"Temp in Celsius: {celsius_temp}")
            break
        except ValueError:
            print("Please, enter a valid number")

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Choose option (1 or 2): ")
    
    if choice == '1':
        celsius_to_fahrenheit()
    elif choice == '2':
        fahrenheit_to_celsius()
    else:
        print("Invalid choice. Restart the program to try again.")

if __name__ == "__main__":
    main()
