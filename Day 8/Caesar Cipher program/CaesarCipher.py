#TODO 1: figure out how to print spaces
#TODO 2: add case sencitivity
#TODO 3: finish decrypt function

import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo.logo)

task=input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
message=input("Type your message: ")
number=eval(input("Type the shift number: "))

#Encode
def encrypt(message,number):
    #for each letter in a massage find a position of that letter in alphabet
    #shift that letter by user number
    #assign that shifted letter to new string
    encrypted_message=""
    for letter in message:
        if letter==" ":
            continue
        else:
            letter_index=alphabet.index(letter)
            new_letter=alphabet[letter_index+number]
            encrypted_message+=new_letter
    print(encrypted_message)

if task=="encode":
    encrypt(message,number)

#Decode