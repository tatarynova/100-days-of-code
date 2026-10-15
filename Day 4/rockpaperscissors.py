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

list_of_choices = ["rock", "paper", "scissors"]
random_choice = random.choice(list_of_choices)
print(random_choice)#picks out 0 1 or 2

user_choice=input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors")
print(user_choice)
print("Computer choose:")
#what draws computer
if random_choice == 0:
    print(rock)
elif random_choice == 1:
    print(paper)
elif random_choice == 2:
    print(scissors)

#rock
if user_choice == 0:
    if random_choice == 0: #rock
        print("Ties!")
    elif random_choice == 1:
        print("You lose!")
    else:
        print("You win!")
#paper
elif user_choice == 1:
    if random_choice == 0:
        print("You win!")
    if random_choice == 1:
        print("Ties!")
    else:
        print("You lose!")
#scissors
elif user_choice == 2:
    if random_choice == 0:
        print("You lose!")
    if random_choice == 1:
        print("You win!")
    else:
        print("Ties!")