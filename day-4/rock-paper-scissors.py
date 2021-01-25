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

choices = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
lose = "You lose."
won = "You won."
draw = "Draw."
if choice >= 3 or choice < 0:
    print("Invalid number, you lose!")
else:
    player_choice = choices[choice]
    print(player_choice)
    print("Computer chose:")
    random_num = random.randint(0, 2)
    computer_choice = choices[random_num]
    print(computer_choice)
    if choice == random_num:
        print(draw)
    elif choice == 0 and random_num == 1:
        print(lose)
    elif choice == 1 and random_num == 2:
        print(lose)
    elif choice == 2 and random_num == 0:
        print(lose)
    else:
        print(won)
