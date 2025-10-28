def fabian():
    while True:
        user_input = input("Enter a number or 'exit' to quit: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye")
            break
        
        try:
            num = float(user_input)
            
            if num == 0:
                print(f"{num} is zero")
            
            elif num > 0: # to handle +ve
                if num.is_integer() and num % 2 == 0:
                    print(f"{num} is positive, an integer and even number")
                elif num.is_integer() and num % 2 != 0:
                    print(f"{num} is positive, an integer and is odd")
                else:
                    print(f"{num} is positive, and is a decimal")
                    
            else: # to handle -ve
                if num.is_integer() and num % 2 == 0:
                    print(f"{num} is negative, an integer and even number")
                elif num.is_integer() and num % 2 != 0:
                    print(f"{num} is negative, an integer and is odd")
                else:
                    print(f"{num} is negative, and is a decimal")
                    
        except ValueError:
            print("Invalid Input, Please enter a number!")
                
if __name__ == "__main__":
    fabian()