# Coursework Assessment 1
# Name:Toxirjon Obidov
# Student No:2428279

def welcome():
    """
    Prints welcome message.
    """
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")

def enter_message():
    """
    Prompts user to enter mode, message, and shift.
    Returns mode (e or d), message, and shift.
    """
    mode = input("Would you like to encrypt (e) or decrypt (d)? : ").lower()
    while mode not in ['e', 'd']:
        print("Invalid Mode")
        mode = input("Would you like to encrypt (e) or decrypt (d)? : ").lower()

    message = input("What message would you like to {}? ".format("encrypt" if mode == 'e' else "decrypt")).upper()

    shift = input("What is the shift number: ")
    while not shift.isdigit() or not 0 <= int(shift) <= 25:
        print("Invalid Shift")
        shift = input("What is the shift number: ")

    return mode, message, int(shift)

def encrypt(message, shift):
    """
    Encrypts the given message using Caesar Cipher.
    Returns the encrypted message.
    """
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    """
    Decrypts the given message using Caesar Cipher.
    Returns the decrypted message.
    """
    return encrypt(message, -shift)

def process_file(filename, mode, shift):
    """
    Processes the file and encrypts/decrypts the messages based on mode and shift.
    Returns a list of processed messages.
    """
    try:
        with open(filename, 'r') as file:
            messages = file.readlines()
            processed_messages = []
            for message in messages:
                processed_message = encrypt(message.strip().upper(), shift) if mode == 'e' else decrypt(message.strip().upper(), shift)
                processed_messages.append(processed_message)
        return processed_messages
    except FileNotFoundError:
        print("File not found.")
        return []

def is_file(filename):
    """
    Checks if the file exists.
    Returns True if the file exists, False otherwise.
    """
    import os
    return os.path.exists(filename)

def write_messages(messages):
    """
    Writes the given messages to a file called 'results.txt'.
    """
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')

def message_or_file():
    """
    Prompts the user to choose between entering a message or using a file.
    Returns mode (e or d), message (if entered), filename (if selected), and shift.
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? : ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        source = input("Would you like to read from a file (f) or the console (c)? : ").lower()
        if source in ['f', 'c']:
            break
        else:
            print("Invalid Source")

    if source == 'c':
        message = input("What message would you like to {}? ".format("encrypt" if mode == 'e' else "decrypt")).upper()
        shift = input("What is the shift number: ")
        while not shift.isdigit() or not 0 <= int(shift) <= 25:
            print("Invalid Shift")
            shift = input("What is the shift number: ")
        return mode, message, None, int(shift)
    else:
        filename = input("Enter a filename: ")
        while not is_file(filename):
            print("Invalid Filename")
            filename = input("Enter a filename: ")
        shift = input("What is the shift number: ")
        while not shift.isdigit() or not 0 <= int(shift) <= 25:
            print("Invalid Shift")
            shift = input("What is the shift number: ")
        return mode, None, filename, int(shift)


def main():
    welcome()

    while True:
        mode, message, filename, shift = message_or_file()

        if filename:
            processed_messages = process_file(filename, mode, shift)
            if processed_messages:
                print("Output written to results.txt")
                write_messages(processed_messages)
            else:
                print("No messages processed.")
        elif message:
            processed_message = encrypt(message, shift) if mode == 'e' else decrypt(message, shift)
            print("Processed Message:", processed_message)

if __name__ == "__main__":
    main()


