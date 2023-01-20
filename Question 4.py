#Determining the number of candies
for candies in range(1,200):                             #running a loop for 200 candies
    if candies%5==2 and candies%6==3 and candies%7==2:   #If the number satisfies the condition of remainder
        print("The number of candies are",candies)
