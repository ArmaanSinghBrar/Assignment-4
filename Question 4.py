#Determining the number of candies
for candies in range(1,200):
    if candies%5==2 and candies%6==3 and candies%7==2:
        print("The number of candies are",candies)
