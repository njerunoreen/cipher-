# Vigenère Cipher Encryption
def vigenere_encrypt(plaintext, key):
    # Alphabet used for encryption
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Remove spaces and convert to uppercase
    plaintext = plaintext.replace(' ', '').upper()  # Convert to uppercase and remove spaces
    key = key.replace(' ', '').upper()  # Remove spaces from the key
    
    # Repeat the key to match the length of the plaintext
    extended_key = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]

    ciphertext = []

    for i in range(len(plaintext)):
        # Encrypt each character
        p_char = plaintext[i]
        k_char = extended_key[i]
        
        # Find positions of the characters in the alphabet
        p_index = alphabet.index(p_char)
        k_index = alphabet.index(k_char)
        
        # Perform the Vigenère shift
        cipher_index = (p_index + k_index) % 26
        ciphertext.append(alphabet[cipher_index])
    
    return ''.join(ciphertext)

# Vigenère Cipher Decryption
def vigenere_decrypt(ciphertext, key):
    # Alphabet used for decryption
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Remove spaces and convert to uppercase
    ciphertext = ciphertext.replace(' ', '').upper()  # Convert to uppercase and remove spaces
    key = key.replace(' ', '').upper()  # Remove spaces from the key

    # Repeat the key to match the length of the ciphertext
    extended_key = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]

    plaintext = []

    for i in range(len(ciphertext)):
        # Decrypt each character
        c_char = ciphertext[i]
        k_char = extended_key[i]
        
        # Find positions of the characters in the alphabet
        c_index = alphabet.index(c_char)
        k_index = alphabet.index(k_char)
        
        # Perform the Vigenère reverse shift
        plain_index = (c_index - k_index) % 26
        plaintext.append(alphabet[plain_index])
    
    return ''.join(plaintext)

# Main interaction loop
def main():
    while True:
        print("\n=== Vigenère Cipher ===")
        choice = input("Type 'encrypt', 'decrypt', or 'exit': ").strip().lower()

        if choice == 'encrypt':
            text = input("Enter the text to encrypt: ")
            key = input("Enter the key: ")
            encrypted = vigenere_encrypt(text, key)
            print("Encrypted text:", encrypted)

        elif choice == 'decrypt':
            text = input("Enter the text to decrypt: ")
            key = input("Enter the key: ")
            decrypted = vigenere_decrypt(text, key)
            print("Decrypted text:", decrypted)

        elif choice == 'exit':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
