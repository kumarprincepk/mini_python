# This is the the siccor paper rock game using random module
import random
l=["rock","scissor","paper"]
'''
rock vs paper -> paper wins
rock vs scissor -> rock wins
paper vs scissor -> scissor wins
'''
while True:
    ccount=0
    ucount=0
    uc= int(input('''
    Game Start ........
    1. Yes, I want to play game.
    2. No, I don't want to play game.
    '''))
    if uc==1:
        for a in range(1,6):
            usrInput= int(input('''
            1. Rock
            2. Scissor
            3. Paper
            '''))
            if usrInput==1:
                uchoice="rock"
            elif usrInput==2:
                uchoice="scissor"
            elif usrInput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer choice : -- ",Cchoice)
                print("User Choice : -- ", uchoice)
                print("Game Draw...")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer choice : -- ", Cchoice)
                print("User Choice : -- ", uchoice)
                print("You win")
                ucount=ucount+1
            else:
                print("Computer choice : -- ", Cchoice)
                print("User Choice : -- ", uchoice)
                print("Computer win")
                ccount = ccount + 1
        if ucount==ccount:
            print("Final Game Draw...")
            print("User Score : -- ", ucount)
            print("Computer Score : -- ", ccount)
        elif ucount>ccount:
            print("Final You Win Game ...")
            print("User Score : -- ", ucount)
            print("Computer Score : -- ", ccount)
        else:
            print("Final Computer Win The Game...")
            print("User Score : -- ", ucount)
            print("Computer Score : -- ", ccount)
    else:
        break;