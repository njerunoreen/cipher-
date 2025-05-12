# Transposition Cipher Function (based on your request)
def transposition_cipher(plaintext):
    # Separate characters by odd and even indices
    odd_chars = ''.join(plaintext[i] for i in range(len(plaintext)) if i % 2 == 0)  # Odd index (1st, 3rd, 5th, ...)
    even_chars = ''.join(plaintext[i] for i in range(len(plaintext)) if i % 2 != 0)  # Even index (2nd, 4th, 6th, ...)
    
    # Combine odd and even characters together
    return odd_chars + even_chars

# Function to decrypt the text
def decrypt_transposition(ciphertext):
    # Find the mid point of the string
    mid = len(ciphertext) // 2
    
    # Split the ciphertext into odd and even parts
    odd_chars = ciphertext[:mid]  # First half is odd-indexed characters
    even_chars = ciphertext[mid:]  # Second half is even-indexed characters
    
    # Rebuild the original text by alternating between odd and even characters
    decrypted_text = ''
    for i in range(len(odd_chars)):
        decrypted_text += odd_chars[i]
        if i < len(even_chars):
            decrypted_text += even_chars[i]
    
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
        
        # Encrypt the text using Transposition Cipher
        encrypted_text = transposition_cipher(plaintext)
        print(f"Original Text: {plaintext}")
        print(f"Encrypted Text (Transposition Cipher): {encrypted_text}")
        
        # Allow user to input their own text to decrypt
        ciphertext = input("Enter the text you want to decrypt: ").strip()
        
        # Decrypt the text
        decrypted_text = decrypt_transposition(ciphertext)
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

