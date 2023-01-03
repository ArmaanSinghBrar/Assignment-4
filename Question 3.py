#Multiplication game for children
import random
list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = [1,2,3,4,5,6,7,8,9,10]
i=1
while i<11:
    a = random.choice(list_1)
    b = random.choice(list_2)
    c = a*b
    d=float(input(f"\nQuestion{i}: {a}×{b} ="))
    i+=1
    if c==d:
        print("Right!")
    elif c!=d:
        print(f"Wrong. The answer is {c}")
