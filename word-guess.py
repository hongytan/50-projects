w = 'python'
word = [*w]
n = len(word)

lives = 12

guessed_letters = set()
guessed_word = ['_' for _ in range(n)]

print('Guess the characters')
for _ in range(n):
    print('_', end=' ')
print()

while lives > 0 and '_' in guessed_word:
    # Guess a character that has not been guessed yet
    guess = input('Guess a character: ')
    while guess in guessed_letters:
        guess = input('Guess a different character: ')
    guessed_letters.add(guess)

    # Check if character is word
    if guess in word:
        indices = [i for i, x in enumerate(word) if x == guess]
        for i in indices:
            guessed_word[i] = guess

    for letter in guessed_word:
        print(letter, end=' ')
    print()

    lives -= 1

if lives == 0:
    print(f'You lose. The word is {w}.')
else:
    print(f'You win! The word is {w}.')
