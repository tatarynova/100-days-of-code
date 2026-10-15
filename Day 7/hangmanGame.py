import random

word_list = ["mountain", "university", "book"]
random_word = random.choice(word_list)

#turn random word into a list
letter_list=[]
for letter in random_word:
    letter_list.append(letter)

#LIVE STAGES
hangman_stages=[
    """
    +---+

       |   |
           |
           |
           |
           |
     =========
     """,
    """
    +---+

       |   |
       O   |
           |
           |
           |
     =========
    """,
    """
    +---+

       |   |
       O   |
       |   |
           |
           |
     =========
     """,
    """
    +---+

       |   |
       O   |
      /|   |
           |
           |
     =========
     """,
    """
    +---+

       |   |
       O   |
      /|\  |
           |
           |
     =========
     """,
    """
    +---+

       |   |
       O   |
      /|\  |
      /    |
           |
     =========
     """,
    """
    +---+

       |   |
       O   |
      /|\  |
      / \  |
           |
     =========
     """
]
def print_stage(lives):
    if lives==6:
        stage=0
    elif lives==5:
        stage=1
    elif lives==4:
        stage=2
    elif lives==3:
        stage=3
    elif lives==2:
        stage=4
    elif lives==1:
        stage=5
    elif lives==0:
        stage=6
    return stage

print("Welcome to 'HangMan' game!")
print(random_word)

empty_word_list=["_"]*len(random_word)

print(f"Word to guess: {string(empty_word_list)} ")
lives=6

while lives!=0:
    guessed_letter = input("Make a guess: ")
    if guessed_letter in letter_list:
        index=-1
        for item in letter_list:
            index+=1
            if item == guessed_letter:
                empty_word_list[index]=guessed_letter #if the letter met in a word few times, second one is not being print out
        print(f"=========== {lives}/6 LIVES ==========")
        print(f"{hangman_stages[print_stage(lives)]}")
        print(f"{string(empty_word_list)}")
    else:
        lives-=1
        print(f"=========== {lives}/6 LIVES ==========")
        print(f"{hangman_stages[print_stage(lives)]}")
        print("Wrong guess!")
    if empty_word_list == letter_list:
        print("You win!")
        break

if lives==0:
    print(f"=========== {lives}/6 LIVES ==========")
    print("You have lost! Try again!")