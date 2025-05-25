import random
comp_generate=random.randint(1,10)
attempt=3

while attempt > 0:
    user=int(input("Enter Number Between 1 to 10:"))
    if user > comp_generate:
        print("Too High! Try again")
    elif user < comp_generate:
        print("Too Low! Try Again")
    elif user == comp_generate:
        print("You Win")
        break
    attempt=attempt-1
    if attempt==0:
        print(f"Game Over! The Correct Number is {comp_generate}")

    
        
