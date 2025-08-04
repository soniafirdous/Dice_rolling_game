# #loop
# while True:
    
#   choice=input("Roll the dice? (yes/no): ").lower()
#   if choice =='yes':                              
#     import random
#     roll1=random.randint(1,6)
#     roll2=random.randint(1,6)
#     print(f"{roll1},{roll1}")
#   elif choice=="no":
#     print("Goodbye!,thanks for playing!")
#     break
#   else:
#       print("Invalid choice")  
      
print("The dice rolling game")
name=input("enter your name:")
print(f"Hi {name}! Let's play a game of dice rolling!")
#loop
i=6
score=0
while i > 0:
    
  choice=input("Roll the dice? (yes/no): ").lower()
  if choice =='yes':                              
    import random
    roll=random.randint(1,6)
    print(f"you rolled a {roll}")
    i-=1
    score+=roll
    print(f"you have {i} turn{'s' if i>1 else ''} left")
    print(f"your current score is {score}")
    if i==0:
        print("Game over")
        print(f"your final score is {score}")
    else:
        print("keep rolling ....")
  elif choice=="no":
    print("Goodbye!,thanks for playing!")
    break
  else:
      print("Invalid choice")  