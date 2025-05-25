import random
letters=['a','q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','z','x','c','v','b','n','m']
symbols=['!','@','#','$','%','^','&','*','(',')']
numbers=[1,2,3,4,5,6,7,8,9,0]
print("Welcome to create a random password generator")
letters1=int(input("How many letters you want?"))
symbols1=int(input("How many symbols you want?"))
numbers1=int(input("How many numbers you want?"))
letters_choice=[]
for i in range(letters1):
    letters_choice.append(random.choice(letters))
print("".join(letters_choice),end="")
symbol_choice=[]
for j in range(symbols1):
    symbol_choice.append(random.choice(symbols))
print("".join(symbol_choice),end="")
numbers_choice=[]
for k in range(numbers1):
    numbers_choice.append(random.choice(numbers))
print("".join(map(str,numbers_choice)),end="")
