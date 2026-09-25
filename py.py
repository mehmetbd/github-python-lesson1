import random
number=random.randint(1,50)
hearts=5
while hearts>0:
    guess=int(input("guess the number:"))
    if guess==number:
        print("you won!")
        break
    else:
        print("game over")
        hearts-=1
        print("hearts remaining:",hearts)
    if hearts == 0:
        print("you lose")