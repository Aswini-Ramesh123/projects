import random
choices=["Rock","Paper","scissor"]
user_choice=input("Enter Your Choice: Rock , Paper , Scissor:").lower()
computer_choice=random.choice(choices)
print("Computer Choice:",computer_choice)
if user_choice==computer_choice:
    print("Match Tie")
elif user_choice=="Rock" and computer_choice=="Scissor" or \
    user_choice=="Paper" and computer_choice=="Rock" or \
    user_choice=="Scissor" and computer_choice=="Paper":
        print("You Win")
else:
    print("You Loss")
    

    
