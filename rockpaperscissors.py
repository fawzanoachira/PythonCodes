import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

userPoint = 0
compPoint = 0

for i in range(3):
    computerInput = random.randint(0,2)
    userInput = int(input("Enter your choice, 0, 1, 2: "))
    if(userInput==0):
        print(rock)
    elif(userInput==1):
        print(paper)
    else:
        print(scissors)

    if(computerInput==0):
        print(rock)
    elif(computerInput==1):
        print(paper)
    else:
        print(scissors)
    
    if(userInput==computerInput):
        print("Draw")
    elif(userInput==0 and computerInput==1):
        print("Computer wins")
        compPoint+=1
    elif(userInput==0 and computerInput==2):
        print("User wins")
        userPoint+=1
    elif(userInput==1 and computerInput==0):
        print("User wins")
        userPoint+=1
    elif(userInput==1 and computerInput==2):
        print("Computer wins")
        compPoint+=1
    elif(userInput==2 and computerInput==0):
        print("Computer wins")
        compPoint+=1
    elif(userInput==2 and computerInput==1):
        print("User wins")
        userPoint+=1

if(userPoint>compPoint):
    print("User win the match")
elif(compPoint>userPoint):
    print("Computer win the match")
else:
    print("Match is draw")