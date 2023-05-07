import random

# Player variable is a boolean: True (User), False (Computer)
player = True

num = [] # List for numbers

# Get valid inputs from player
def get_inputs(player, nums):

    if player: # User's turn
        input_len = int(input('How many numbers do you wish to enter?\n> '))
        print('Enter your values')
        for _ in range(input_len):
            x = int(input('> '))
            nums.append(x)

    # Check if numbers given by user are not consecutive
        if not all(nums[i+1] == nums[i]+1 for i in range(0, len(nums)-1)):
            print('Numbers are not consecutive! You lose!')
            return False
        
    else: # Computer's turn
        n = random.randint(1,5) + 1 #  Choose randomly the amount of numbers to enter
        last_num = 1 if not nums else nums[-1]+1 # Find the starting number for computer's turn
        x = [i for i in range(last_num, last_num+n)] # Array of numbers chosen
        nums.extend(x) # Extend array to back of nums

        print("Order of inputs after computer's turn is:")
        print(nums)
        print()
        print('Your turn.')
        print()

    return nums

# Let player choose to start first or second
def start_first_or_second(player):
    if player: # User
        start_place = input("Enter 'F' to start first.\nEnter 'S' to start second.\n> ") # Ask if user wants to start first or second
        while start_place != 'F' and start_place != 'S': # Ensure correctness of input
            start_place = input("Enter 'F' to start first.\nEnter 'S' to start second.\n> ")
    else: # Computer
        start_place = random.choice(['S','F'])

    return start_place

# ===========================================================================================

# Ask if user wants to start the game
start_game = input("Do you want to start the game? (y/n)\n> ")
while start_game != 'y' and start_game != 'n': # Ensure correctness of input
    start_game = input("Do you want to start the game? (y/n)\n> ")

if start_game == 'y': # User starts the game

    start_place = start_first_or_second(True)

    if start_place == 'F': # User starts first
        num = get_inputs(player, num)
    else: # Computer starts first
        player = False
        num = get_inputs(player, num)

    while 21 not in num:
        player = False if player else True
        num = get_inputs(player, num)
        if not num: break
    if player: print('You lose!')
    else: print('CONGRATULATIONS!!!\nYOU WON!')

    
else: # Computer starts the game and computer always starts first by my design
    player = False
    num = get_inputs(player, num)
    while 21 not in num:
        player = False if player else True
        num = get_inputs(player, num)
        if not num: break
    if player: print('You lose!')
    else: print('CONGRATULATIONS!!!\nYOU WON!')