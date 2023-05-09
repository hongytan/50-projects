import random

player = 'user' # Player variable
num = []        # List for numbers

# Return True if there is a winner else False
def winner(nums):
    if 21 in nums:
        return True
    return False

# Get valid inputs from player
def get_inputs(player, nums):

    if player == 'user': # User's turn
        input_len = int(input('How many numbers do you wish to enter?\n> '))
        print('Enter your values (> 0)')
        for _ in range(input_len):
            x = int(input('> '))
            while x < 1:
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

    return nums

# Let player choose to start first or second
def start_first_or_second(player):
    if player == 'user': # User
        start_place = input("Enter 'F' to start first.\nEnter 'S' to start second.\n> ") # Ask if user wants to start first or second
        while start_place != 'F' and start_place != 'S': # Ensure correctness of input
            start_place = input("Enter 'F' to start first.\nEnter 'S' to start second.\n> ")
    else: # Computer
        start_place = random.choice(['S','F'])

    return start_place

def game(player, nums):

    while 21 not in nums:

        # Get inputs
        nums = get_inputs(player, nums)
        if not nums:
            print('Numbers not consecutive! You lose.')
            break

        # Check for winner
        if winner(nums):
            print('Congrats! You win!')
            break

        # Next player
        player = 'user' if player == 'computer' else 'computer'

    return 

# ===========================================================================================

# Ask if user wants to start the game
start_game = input("Do you want to start the game? (y/n)\n> ")
while start_game != 'y' and start_game != 'n': # Ensure correctness of input
    start_game = input("Do you want to start the game? (y/n)\n> ")

if start_game == 'y': # User starts the game

    start_place = start_first_or_second('user')

    if start_place == 'F': # User starts first
        game(player, num)
    else: # Computer starts first
        player = 'computer'
        game(player, num)

else: # Computer starts the game and computer always starts first by my design
    player = 'computer'
    game(player, num)
