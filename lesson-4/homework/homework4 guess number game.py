import random
n=random.randint(1,100)
f=0
while True:
    for i in range(10):
        guess=int(input("Enter a number: "))
        if guess>n:
            print("Too high!")
        elif guess<n:
            print("Too low!")
        else:
            print("You guessed it right!")
            f=1
            break
    if f:
        y=input("Want to play again? ")
        if y.lower() in ['y','yes','ok','k','okay']:
            f=0
            continue
        else:
            break
    else:
        y=input("You lost. Want to play again? ")
        if y.lower() in ['y','yes','ok','k','okay']:
            f=0
            continue
        else:
            break