import colorama
from colorama import Fore, Back
colorama.init(autoreset = True)

# Available letters :
letters = 'abcdefghijklmnopqrstuvwxyz'

# define the encoder function :
def encrypt(request, message, shift_number):
    
    encrypt_message = [i for i in message]
    for i, letter in enumerate(encrypt_message):
        if letter in letters:
            if request == "encode":
                index = letters.index(letter) + shift_number
                if index < len(letters):
                    encrypt_message[i] = letters[index]
                else :
                    new_index = index - len(letters)
                    encrypt_message[i] = letters[new_index + 1]
            elif request == "decode":
                index = letters.index(letter) - shift_number
                if index >= 0:
                    encrypt_message[i] = letters[index]
                else :
                    new_index = (len(letters) - 1) - abs(index)
                    encrypt_message[i] = letters[new_index]
    message = "".join(encrypt_message)
    print(f"Here's the encoded result: {Fore.CYAN}{message}")
    Fore.RESET

# set the counter :
repeat = 1

# Start the loop  :
while repeat :

    print(Fore.GREEN + "Type 'encode' to encrypt, type 'decode' to decrypt:")
    request = input("-> ").lower()
    print(Fore.GREEN + "Type your message:")
    message = input("-> ").lower()
    print(Fore.GREEN + "Type the shift number:")
    shift_number = int(input("-> "))
    encrypt(request, message, shift_number)
    print(Fore.GREEN + "Type 'yes' if you want to go again. Otherwise type 'no'.")
    try_agin = input("-> ").lower()
    if try_agin == "yes": pass
    else : repeat = 0