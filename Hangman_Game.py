import random

# Define the stages of Hangman
hangman_stages = {
    6: """
    _______
    |     |
    |
    |
    |
    |
    -
    """,
    5: """
    _______
    |     |
    |     O
    |
    |
    |
    -
    """,
    4: """
    _______
    |     |
    |     O
    |     |
    |
    |
    -
    """,
    3: """
    _______
    |     |
    |     O
    |    /|
    |
    |
    -
    """,
    2: """
    _______
    |     |
    |     O
    |    /|\\
    |
    |
    -
    """,
    1: """
    _______
    |     |
    |     O
    |    /|\\
    |    /
    |
    -
    """,
    0: """
    _______
    |     |
    |     O
    |    /|\\
    |    / \\
    |
    -
    """
}

word_list = ["apple", "beautiful", "potato", "elephant", "computer", "python", "hangman"]
print("Let's play Hangman!")
lives = 6
chosen_word = random.choice(word_list)
display = ['_' for _ in range(len(chosen_word))]
print(display)
game_over = False

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    # Check guessed letter against chosen word
    if guessed_letter in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guessed_letter:
                display[position] = guessed_letter
    else:
        lives -= 1
        print("Wrong guess! You lost a life.")
        if lives == 0:
            game_over = True
            print("Life's over! You lost.")
            break

    print(display)

    # Check if player has won
    if '_' not in display:
        game_over = True
        print("You win!")
        break

    # Print current stage of hangman
    print(hangman_stages[lives])
