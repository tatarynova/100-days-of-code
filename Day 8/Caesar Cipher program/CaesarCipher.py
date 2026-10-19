from hashlib import new

import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo.logo)


#Encode
def encrypt(message,number):
    #for each letter in a massage find a position of that letter in alphabet
    #shift that letter by user number
    #assign that shifted letter to new string
    encrypted_message=""
    for letter in message:
        if letter not in alphabet:
            encrypted_message += " "
        else:
            letter_index=alphabet.index(letter)
            new_letter=alphabet[letter_index+number]
            encrypted_message+=new_letter
    print(encrypted_message)

#Decode
def decrypt(message,number):
    decrypted_message=""
    for letter in message:
        if letter not in alphabet:
            decrypted_message+=" "
        else:
            letter_index=alphabet.index(letter)
            new_letter=alphabet[letter_index-number]
            decrypted_message+=new_letter
    print(decrypted_message)

while True:
    task = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    if task != "encode" and task != "decode":
        print("Invalid option, please type 'encode' or 'decode'.")
        continue

    message = input("Type your message: \n")
    number = eval(input("Type the shift number: \n"))
    if task=="encode":
        encrypt(message,number)
    else:
        decrypt(message,number)

    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no': \n")
    if go_again=="yes":
        continue
    else:
        break