# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',
    '&': '.-...',  "'": '.----.', '@': '.--.-.',
    ')': '-.--.-', '(': '-.--.',  ':': '---...',
    ',': '--..--', '=': '-...-',  '!': '-.-.--',
    '.': '.-.-.-', '-': '-....-', '+': '.-.-.',
    '"': '.-..-.', '?': '..--..', '/': '-..-.',
    ' ': '/'
}

# Reverse dictionary for decoding
MORSE_CODE_DICT_REVERSED = {v: k for k, v in MORSE_CODE_DICT.items()}


def encode_to_morse(text):
    """Encode text to Morse code."""
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)


def decode_from_morse(morse_code):
    """Decode Morse code to text."""
    words = morse_code.strip().split(' / ')
    decoded = []
    for word in words:
        letters = word.split()
        decoded_word = ''.join(MORSE_CODE_DICT_REVERSED.get(code, '') for code in letters)
        decoded.append(decoded_word)
    return ' '.join(decoded)


def main():
    while True:
        print("\nMorse Code Encoder/Decoder")
        print("1. Encode text to Morse code")
        print("2. Decode Morse code to text")
        print("3. Reset (Return to main menu)")
        print("4. Exit")
        
        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            # Encoding mode
            text = input("Enter text to encode: ")
            encoded = encode_to_morse(text)
            print("Encoded Morse code:", encoded)
            reset = input("Do you want to reset and return to the main menu? (y/n): ")
            if reset.lower() == 'y':
                continue  # Go back to the main menu
        
        elif choice == '2':
            # Decoding mode
            morse_code = input("Enter Morse code to decode (use space to separate letters and / to separate words): ")
            decoded = decode_from_morse(morse_code)
            print("Decoded text:", decoded)
            reset = input("Do you want to reset and return to the main menu? (y/n): ")
            if reset.lower() == 'y':
                continue  # Go back to the main menu
        
        elif choice == '3':
            # Reset (return to the main menu)
            print("\nReturning to main menu...\n")
            continue  # Go back to the main menu
        
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            input("Press Enter to continue...")

# Run the program
if __name__ == "__main__":
    main()
