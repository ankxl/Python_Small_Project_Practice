""""
Caesar Cipher Hacker program by Ankit R
This program hacks messages encrypted with the ceasar cipher
by doing a brute force attack against all possible keys (1 to 26)

"""


import random, sys, pyperclip

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(message, key):
    """Takes the message to be decrypted and key to use to decrypt
    using Ceasr Cipher decryption technique
    """                 
    dec_message = []
                    
    for i in range(0,len(message)):
        if message[i].upper() in characters:
            index = characters.index(message[i].upper())
            index = (26 + index - int(key))%26
            dec_message.append(characters[index].upper())
        else:
            dec_message.append(message[i])
    return(''.join(dec_message))

def main():
    print("Caesar Cipher Hacker program by Ankit R")
    print("Enter the Caesar Cipher encrypted message for brute force hacking")
    if message := input("> "):
        print("The encrypted messages will be decrypted using keys from 1 to 26")

        # Loop for all keys from 1 to 26
        for key in range(1, len(characters)+1):
            # Decode the message using key from iteration
            dec_message = decrypt(message,key)
            print(f"Key {key}: {dec_message}")




if __name__ == '__main__':
    main()