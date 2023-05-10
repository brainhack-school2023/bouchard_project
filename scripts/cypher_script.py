import os
import argparse
from useful_functions import *


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Script for Cypher.')
    # Arguments for the script
    parser.add_argument('-i', '--i', default="default.txt", type=str, help='Path to the input text files containing the message.')
    parser.add_argument('-o','--o', default="default_out.txt", type=str, help='Path for the output file where the processed message will be written.')
    parser.add_argument('-k','--k', default="key", type=str, help='A string directly containing the key.')
    parser.add_argument('-m','--m', default="encryption", type=str, help='A string that can take the value "encryption" or "decryption" to tell the script if you want to encrypt or decrypt the input message.')
    args = parser.parse_args()
    
    # Turn value to boolean
    if args.m == "encryption":
        args.m = True
    elif args.m == "decryption":
        args.m = False

    # Get message to encrypt
    with open(args.i, 'r') as file:
        data_to_encrypt = file.read().rstrip()

    # Write the script depending on the output encrypted message.
    with open(args.o, 'w') as f:
        f.write(process_message(data_to_encrypt,args.k,args.m))








