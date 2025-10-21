age = input("Enter your age:")
age = int(age)

if age < 18:
    print("You are a minor. Usikunywe pombe.")
elif age == 18:
    print("You just became an adult")
elif 19 <= age < 35:
    print("You are a youth") 
elif 35 <= age < 110:
    print("Go get your retirement benefits")
else:
    print("A'int no way dude🤣")
    
    #LOGIC OPERATORS
    
marks = input("Enter your marks(0-100): ")
marks = int(marks)

if marks >= 90:
    print("Grade: A")
elif 80 <= marks < 90:
    print("Grade: A-")
elif 70 <= marks < 80:
    print("Grade: B+")
elif 60 <= marks < 70:
    print("Grade: B")
else:
    print("Grade: F (Fail)")