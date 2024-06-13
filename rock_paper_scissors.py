import random

rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
"""

paper = """
         _______
    ---'    ____)____
               ______)
               _______)
              _______)
    ---.__________)
"""

scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
"""

while True:
    while True:
        game_images = [rock, paper, scissors]
        user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
        if user_choice > 2 or user_choice < 0:
            print("Invalid option. Please enter a valid option.")
        else:
            computer_choice = random.randint(0, 2)
            print("Your Choice:",user_choice)
            print(game_images[user_choice])
            print("Computer Chose:",computer_choice)
            print(game_images[computer_choice])
            if computer_choice == user_choice:
                print("Draw")
            elif computer_choice == 2 and user_choice == 0:
                print("You won")
            elif computer_choice == 0 and user_choice == 2:
                print("You lost")
            elif computer_choice > user_choice:
                print("You lose")
            elif computer_choice < user_choice:
                print("You won")
            break
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break

print("Thank you for playing!")
