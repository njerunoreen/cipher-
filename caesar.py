# Function to encrypt text using Caesar Cipher
def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    
    # Loop through each character in the plaintext
    for char in plaintext:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabet characters remain unchanged
            encrypted_text += char
    
    return encrypted_text

# Function to decrypt text using Caesar Cipher
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    
    # Loop through each character in the ciphertext
    for char in ciphertext:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Non-alphabet characters remain unchanged
            decrypted_text += char
    
    return decrypted_text

# Main function to interact with the user
def main():
    while True:
        # Allow user to input their own text to encrypt
        plaintext = input("Enter the text you want to encrypt (or type 'exit' to quit): ").strip()
        
        # Option to exit the program
        if plaintext.lower() == 'exit':
            print("Exiting program.")
            break
        
        # Ask the user for a shift value
        try:
            shift = int(input("Enter the shift key (an integer): ").strip())
        except ValueError:
            print("Invalid shift key! Please enter an integer.")
            continue
        
        # Encrypt the text using Caesar Cipher
        encrypted_text = caesar_encrypt(plaintext, shift)
        print(f"Original Text: {plaintext}")
        print(f"Encrypted Text (Caesar Cipher): {encrypted_text}")
        
        # Allow user to input their own text to decrypt
        ciphertext = input("Enter the text you want to decrypt: ").strip()
        
        # Decrypt the text
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(f"Encrypted Text: {ciphertext}")
        print(f"Decrypted Text: {decrypted_text}")
        
        # Ask the user if they want to reset
        reset = input("Do you want to try again with a new message? (yes/no): ").strip().lower()
        if reset != 'yes':
            print("Exiting program.")
            break

# Run the program
if __name__ == "__main__":
    main()
