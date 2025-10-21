def main():
    
    CURRENT_YEAR = 2025

    while True:
        user_input = input("Enter your Year of Birth: ").strip()
        
        if user_input.lower() == "exit":
            print("I hope I was of help, Goodbye!")
            break
        
        try:
            birth_year = int(user_input)
            
            if birth_year < 1900  or birth_year > 2025:
                print("Please enter a reasonable Year!")
                continue
                
            age = CURRENT_YEAR - birth_year
            print(f"Since you were born in {birth_year}, you are {age} years old.")
            
        except ValueError:
            print("Invalid Input, please enter correct format for Year of Birth!")
if __name__ == "__main__":
    main()