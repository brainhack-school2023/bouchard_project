# Useful functions for The Vigenere cipher exercise.
import sys

def encrypt_letter(letter, key):
    """
    return the encrypted letter with the key, e.g. encrypt_letter("l", "h") should return 'Ô'.
    """
    return chr((ord(letter) + ord(key)) % 1114112)


def decrypt_letter(letter, key):
    """
    return the decrypted letter with the key, e.g. decrypt_letter("Ô", "h") should return 'l'.
    """
    return chr((ord(letter) - ord(key)) % 1114112)


def process_message(message, key, encrypt):
    """
    return the encrypted message using the letters in key if encrypt is True, and the decrypted message if encrypt is False. 
    """

    # Variables needed
    len_key = len(key)
    key_indice = 0
    processed_message = ""

    # Loop over the message letters
    for msg_indice in range(len(message)):

        # Encrypt or decrypt message
        if encrypt:
            processed_message += encrypt_letter(message[msg_indice], key[key_indice])
        else:
            processed_message += decrypt_letter(message[msg_indice], key[key_indice])
        # Manage key reset
        key_indice += 1
        if key_indice == len_key: key_indice = 0

    return processed_message


if __name__ == '__main__':

    # Call the functions from terminal
    if sys.argv[1] == "process_message":
        # Call the process message function
        if sys.argv[4] == "False":
            sys.argv[4] = False
        elif sys.argv[4] == "True":
            sys.argv[4] = True
        print(globals()[sys.argv[1]](sys.argv[2],sys.argv[3],sys.argv[4]))

    elif sys.argv[1] == "test":
        # Run testing
        message = "Alpaca"
        key = "boum"
        encrypted_msg = process_message(message, key, True)
        decrypted_msg = process_message(encrypted_msg, key, False)
        if message == decrypted_msg:
            print("Test passed")
        else:
            print("Test failed")

    else: 
        # Call the functions individually
        print(globals()[sys.argv[1]](sys.argv[2],sys.argv[3]))
