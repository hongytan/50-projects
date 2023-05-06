word = 'python'
word = [*word]
n = len(word)
guess_word = ['_' for _ in range(n)]

count = 0

print("Guess the characters")
for _ in word:
    print('_', end=' ')
print()

lives = 12
while count != n and lives > 0:

    guess = input("Guess a character: ")

    if guess in word:
        i = word.index(guess)
        guess_word[i] = guess
        count += 1

    for letter in guess_word:
        print(letter, end=' ')
    print()

ans = ''.join(guess_word)
if count == n:
    print(f'You win! The word is {ans}.')
else:
    print(f'You lose! The word is {ans}.')
