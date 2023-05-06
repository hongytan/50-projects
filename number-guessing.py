import random

x = input("Enter a range: ")
x = x.split()
a = int(x[0])
b = int(x[1])

num = random.randint(a,b)

guess = int(input("Guess the number between your given range: "))
lives = 6
while lives > 0:
    while guess < a or guess > b:
        guess = int(input("Invalid guess! Try again: "))
    if guess < num:
        guess = int(input("Number is higher! Try again: "))
    elif guess > num:
        guess = int(input("Number is lower! Try again: "))
    else:
        print(f"Congrats you got it! It was {num}.")
        break
    lives -= 1

if lives == 0:
    print(f"You failed! It was {num}.")