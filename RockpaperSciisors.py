import random
computerScore=0
playerscore=0
arr=['Rock','Paper','Scissors']
inPlay=True
def play():
    global inPlay
    global computerScore
    global playerscore
    while inPlay:
        player=input("Rock Paper or Scissors?").capitalize()
        computer=random.choice(arr).capitalize()
        print(f"You Selected:{player} vs Computer Selected:{computer}")
        if player==computer:
            print('Tie Game')
        elif player=="Rock":
            if(computer=='Paper'):
                print("You lose")
                computerScore+=1
            else:
                print("You win")
                playerscore+=1
        elif player=="Paper":
            if(computer=='Scissors'):
                print("You lose")
                computerScore+=1
            else:
                print("You win")
                playerscore+=1
        elif player=="Scissors":
            if(computer=='Rock'):
                print("You lose")
                computerScore+=1
            else:
                print("You win")
                playerscore+=1
        print(f"Your Score({playerscore}) vs Computer({computerScore})")
        inPlay=input("Play again?")
        if inPlay=='exit':
            break
play()