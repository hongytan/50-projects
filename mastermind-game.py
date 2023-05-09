# !! Assume user only inputs integers for inputs !!

player = 1      # 1 or 2

def get_number(player):
    x = input(f"Player {player}, set the number: ")
    while len(x) != 4:
        x = input(f"Player {player}, set the number: ")

    return x

def guess_number(player, num):
    x = input(f"Player {player}, guess the number: ")
    while len(x) != 4:
        x = input(f"Player {player}, guess the number: ")
    n = len(num)
    num_guess = 1

    while x != num:

        guess = ['X' for _ in range(n)]
        count = 0
        num_guess += 1

        for i in range(n):
            if x[i] == num[i]:
                count += 1
                guess[i] = x[i]

        print(f"Not quite the number. You did get {count} digits correct.")
        print(' '.join(guess))
        print()
        x = input("Enter your next choice of numbers: ")
        while len(x) != 4:
            x = input("Enter your next choice of numbers: ")
    
    print('Congrats! You got it! It was ' + num + '.\n')
    return num_guess

def game():
    x = get_number(1)
    p2 = guess_number(2, x)
    x = get_number(2)
    p1 = guess_number(1, x)

    if p1 < p2:
        print(f'It looks like Player 1 takes the cake! Beating Player 2: {p1}-{p2}.')
    else:
        print(f'It looks like Player 2 takes the cake! Beating Player 1: {p2}-{p1}.')

if __name__ == '__main__':
    game()