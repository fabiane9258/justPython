#Combined conditionals and loops
number = input("Enter random number,(1-10):")
number = int(number)
for number in range(1, 11):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")