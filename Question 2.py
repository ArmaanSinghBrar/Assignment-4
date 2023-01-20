#Program to tell if a year is a leap or not a leap year
year = int(input("Enter a year :"))
if year%400==0:                                    #If divisible by 400 it is a leap year
    print("The given year is a leap year")
elif year%100==0:                                  #If not divisible by 400 but divisible by 100 it is not a leap year
    print("The given year is not a leap year")
elif year%4==0:                                    #If not divisible by 400 and 100 but divisible by 4 it is a leap year
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")
