import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

game_continue = True

user_score = 0
computer_score = 0

name = input("Hello and welcome to Rock, Paper & scissors, before we begin please enter your name: \n").title()

while game_continue:

    user_choice = int(input(f"What do you choose {name}? Type 0 for rock, 1 for paper, 2 for scissors  \n"))

    while user_choice >= len(images) or user_choice < 0:
        print(f"You typed an invalid number {name}. Please try again!")
        user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors  \n"))

    print(images[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer Chose:  ")
    print(images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        user_score += 1
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        computer_score += 1
        print("Computer Won!")
    elif computer_choice > user_choice:
        computer_score +=1
        print("You lose!")
    elif user_choice > computer_choice:
        user_score += 1
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")

    print(f"Current Scorecard: {name} : {user_score}, Computer : {computer_score}   ")

    should_game_be_continued = input("Do you want to play again? Y/N \n").lower()

    while should_game_be_continued not in ['y','n']:
        print(f"You typed an invalid response {name}. Please try again!")
        should_game_be_continued = input("Do you want to play again? Y/N \n").lower()

    if should_game_be_continued == "n":
        game_continue = False

print(f"Final Scorecard: {name} : {user_score}, Computer : {computer_score}\n")

if user_score == computer_score:
    print("Game Drawn")
elif user_score > computer_score:
    print(f"Congratulations {name}, You Win!!!")
elif user_score < computer_score:
    print(f"Sorry, {name}, you lost the game, hence proven THE MACHINES WILL RISE AGAIN, just kidding!\n")

print("Hope you enjoyed the game!!!")