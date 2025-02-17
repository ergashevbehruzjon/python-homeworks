import random
player=0
comp=0
while True:
    ch=random.choice(["rock", "paper", "scissors"])
    user=input("Enter your choice (\"rock\" or \"paper\" or \"scissors\"): ")
    if user=="rock":
        if ch=="rock":
            print("Computer chose rock. It's a draw.")
        elif ch=="paper":
            comp+=1
            print("Computer chose paper. You lose.")
        else:
            player+=1
            print("Computer chose scissors. You win.")
    elif user=="paper":
        if ch=="rock":
            player+=1
            print("Computer chose rock. You win.")
        elif ch=="paper":
            print("Computer chose paper. It's a draw.")
        else:
            comp+=1
            print("Computer chose scissors. You lose.")
    elif user=="scissors":
        if ch=="rock":
            comp+=1
            print("Computer chose rock. You lose.")
        elif ch=="paper":
            player+=1
            print("Computer chose paper. You win.")
        else:
            print("Computer chose scissors. It's a draw.")
    if player==5:
        print("You get 5 points first. You win the game.")
        print("Computer:",comp,"points")
        break
    elif comp==5:
        print("Computer gets 5 points first. Computer wins the game.")
        print("You:",player,"points")
        break