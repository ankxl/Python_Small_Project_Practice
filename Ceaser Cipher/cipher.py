"""
Ceasar Cipher by Ankit Rai
Ceasar Cipher is an ancient encryption algorithm used in Rome. 
It encrypts the letter by moving them over by a certain number.
For example a key of 1:
    A will be B
    B will be C
    ...
"""
import random, sys
import pyperclip

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encryption(message, key):
    print("Message is being encrypted ...")
    print("Encrypted message (Upper Case) is")
                    
    enc_message = []
                    
    for i in range(0,len(message)):
        if message[i].upper() in characters:
            # print("Yes")
            index = characters.index(message[i].upper())
            # print(f"{index} {key} {(index + int(key))%26}")
            index = (index + int(key))%26
            enc_message.append(characters[index].upper())
        else:
            enc_message.append(message[i])
    return(''.join(enc_message))


def decrypt(message, key):
    print("Message is being decrypted ...")
    print("Decrypted message (Upper Case) is")
                    
    dec_message = []
                    
    for i in range(0,len(message)):
        if message[i].upper() in characters:
            # print("Yes")
            index = characters.index(message[i].upper())
            # print(f"{index} {key} {(index + int(key))%26}")
            index = (26 + index - int(key))%26
            dec_message.append(characters[index].upper())
        else:
            dec_message.append(message[i])
    return(''.join(dec_message))


def main():
    while True:
        print("""Ceasar Cipher by Ankit R.
Do you want to (e)ncrypt or (d)ecrypt?""")
        mode = input("> ")

        if mode.lower() in ['e','d']:          
            
            print("Please enter the key (0 to 20) to use")
            key = input("> ")

            if (key.isdecimal()) and (0 <= int(key) <= 20):
                if mode.lower() == 'e':
                    print("Enter the message to encrypt")
                    message = input("> ")

                    enc_message = encryption(message, key)
                    print(enc_message)
                    try:
                        pyperclip.copy(enc_message)
                    except:
                        print("Unable to copy the encrypted message to clipboard")
                    else:
                        print("Full encrypted message copied to the clipboard")
                        break
                elif mode.lower() == 'd':
                    print("Enter the message to decrypt")
                    message = input("> ")

                    dec_message = decrypt(message, key)
                    print(dec_message)
                    try:
                        pyperclip.copy(dec_message)
                    except:
                        print("Unable to copy the decrypted message to clipboard")
                    else:
                        print("Full decrypted message copied to the clipboard")
                        break
                else:
                    continue

if __name__ == '__main__':
    main()