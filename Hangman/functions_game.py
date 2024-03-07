
# Replace blanks for guess letter and check they've already guessed.
def display_user(guess, chosen_word, display):
    guess_lower = guess.lower()
    if guess_lower not in display:
        for i, char in enumerate(chosen_word):
            if char == guess_lower:
                display[i] = guess_lower
    else:
        print(f"{guess_lower} already exist.")

    return guess_lower
