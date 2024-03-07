import random
import functions_game
import picture_hangman
import hangman_words

# Choose word random
chosen_word = random.choice(hangman_words.word_list)
# Create blanks
display = ['_' for e in chosen_word]
# Attemps
lives = 6

print("Hello, Welcome to the hangman's game \n Let's Go \n")

# Game
while lives > -1:
    print(picture_hangman.logo)
    print(f'Ptzzzzzz the hide word is: {chosen_word} \n')
    guess = input("Guess the letter: ")
    # If the use entered none, return input
    if guess != '':
        # Replace blanks for guess letter and check they've already guessed.
        guess_lower = functions_game.display_user(guess, chosen_word, display)
        # While the user don't guess the word it will be doing this.
        if "_" in display and guess_lower != chosen_word:
            print(f"Lives: {lives}")
            print(display)
            print(picture_hangman.stages[lives])
            # When the user entered letter wrong the attempts will end.
            if guess_lower not in list(chosen_word):
                print("There are not match, try again.")
                print(f"Lives: {lives}")
                lives -= 1
                # Hangman's picture.
                print(picture_hangman.stages[lives])
                if lives == -1:
                    print(f"Game Over {picture_hangman.defeat[0]}")

        else:
            print(f"You guess the word: {chosen_word} \n Victory")
            break
    else:
        print("You not enter the letter")
