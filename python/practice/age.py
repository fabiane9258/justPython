def main():
    
    CURRENT_YEAR = 2025

    while True:
        user_input = input("Enter your Year of Birth (or 'exit' to exit): ").strip()
        
        if user_input.lower() == "exit":
            print("I hope I was of help, Goodbye!")
            break
        
        try:
            birth_year = int(user_input)
            
            if birth_year < 1900  or birth_year > CURRENT_YEAR:
                print("Please enter a reasonable Year!")
                continue
                
            age = CURRENT_YEAR - birth_year
            
            if age <= 12:
                print(f"You are {age} years, you are  a Child")
            elif 13 <= age <= 19:
                print(f"You are {age} Years old, you are a Teenager")
            elif 20 <= age <= 60:
                print(f"You are {age} Years old, you are an Adult")
            else:
                print(f"You are {age} Years old, you are a Senior")
            
        except ValueError:
            print("Invalid Input, please enter correct format for Year of Birth!")
if __name__ == "__main__":
    main()