while True:
    user_input = input("Enter temperature in celcius (or 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    try:
        celcius = float(user_input)
        fahrenheit = (celcius * 9/5) + 32
        print(f"{celcius}°C = {fahrenheit}°F")
        
    except ValueError:
        print("Invalid input! Please enter a number or 'exit'. ")
        