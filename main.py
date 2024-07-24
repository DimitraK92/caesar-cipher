from os import system
import signal
from alphabet_list import alphabet
from art import logo

def handler(signum, frame):
    system("cls")
    exit(1)

signal.signal(signal.SIGINT, handler)

def start_app():
    print(logo)
    restart = True
    while restart:
        caesar_cipher()
        restart = input("Do you want to go again? Y/N\n").upper() == "Y"
        
def caesar_cipher():
    (is_valid, option, start_text, shift) = validate_user_input()
    if not is_valid: return
    if option == "decode": shift *= -1
    end_text = ""
    for char in start_text:
        if char not in alphabet:
            end_text += char      
        else: 
            new_index = (alphabet.index(char) + shift) % (len(alphabet))
            end_text += alphabet[new_index]
    print(f"The {option}d message is: {end_text}")

def validate_user_input():
    option = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if option not in ["encode", "decode"]:
        print("Wrong input.")
        return (False, None, None, None)

    text = input("Type your message:\n").lower()

    shift = 0
    try:
        shift = int(input("Type the shift number:\n"))
    except Exception:
        print("Wrong input. Only integer numbers are allowed.")
        return (False, None, None, None)
    
    return (True, option, text, shift)

start_app()
