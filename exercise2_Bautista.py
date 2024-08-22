grade = int(input("Enter your grade: "))

if grade >= 75:
    print("Passed")
elif grade == 74:
    print("Remedial")
elif grade <= 74 and grade >= 0:
    print("Failed")
else:
    print("You have entered an invalid input")