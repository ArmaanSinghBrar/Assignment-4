#Printing garde to corresponding marks
marks = float(input("Enter your marks:"))
if marks<0 or marks>100:
    print("Error Enter correct marks")
elif 0<=marks<25:
    print("Your grade is F")
elif 25<=marks<45:
    print("Your grade is E")
elif 45<=marks<50:
    print("Your grade is D")
elif 50<=marks<60:
    print("Your grade is C")
elif 60<=marks<80:
    print("Your grade is B")
elif 80<=marks<=100:
    print("Your grade is A")
