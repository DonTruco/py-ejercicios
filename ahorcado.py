# List of possible words
import random

words = ['python', 'computer', 'programming', 'algorithm', 'function']

# Select a random word from the list
word = random.choice(words)

# Keep track of the player's guesses and the number of incorrect guesses
guesses = []
incorrect_guesses = 0

# Loop until the word is fully guessed or the player runs out of guesses
while incorrect_guesses < 6:
    # Print the current state of the game
    print("Word:", end=" ")
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("\nIncorrect guesses: " + str(incorrect_guesses))
    
    # Ask the player for a guess
    guess = input("Guess a letter: ").lower()
    
    # Check if the guess is correct
    if guess in word:
        print("Correct!")
        guesses.append(guess)
    else:
        print("Incorrect.")
        incorrect_guesses += 1
    
    # Check if the player has won
    if all(letter in guesses for letter in word):
        print("Congratulations, you won!")
        break

# If the player has run out of guesses, print the game over message
if incorrect_guesses == 6:
    print("Game over. The word was:", word)