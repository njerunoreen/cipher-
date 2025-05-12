 
import math

# Encrypt using Columnar Transposition Cipher
def columnar_encrypt(plaintext, keyword):
    plaintext = plaintext.replace(" ", "").upper()
    keyword = keyword.upper()
    
    num_cols = len(keyword)
    num_rows = math.ceil(len(plaintext) / num_cols)
    
    # Pad plaintext to fit the grid
    padding = (num_cols * num_rows) - len(plaintext)
    plaintext += '_' * padding  # Underscore as padding character

    # Fill the grid row by row
    grid = ['' for _ in range(num_cols)]
    for i in range(len(plaintext)):
        col = i % num_cols
        grid[col] += plaintext[i]

    # Determine order of columns based on sorted keyword
    sorted_key = sorted((char, i) for i, char in enumerate(keyword))
    ciphertext = ''
    for _, i in sorted_key:
        ciphertext += grid[i]

    return ciphertext

# Decrypt using Columnar Transposition Cipher
def columnar_decrypt(ciphertext, keyword):
    ciphertext = ciphertext.replace(" ", "").upper()
    keyword = keyword.upper()
    
    num_cols = len(keyword)
    num_rows = math.ceil(len(ciphertext) / num_cols)

    # Determine column order from sorted keyword
    sorted_key = sorted((char, i) for i, char in enumerate(keyword))
    col_order = [i for _, i in sorted_key]

    # Figure out how many characters in each column
    col_lengths = [num_rows] * num_cols
    total_chars = len(ciphertext)

    # Fill columns based on the order
    columns = [''] * num_cols
    index = 0
    for i in col_order:
        columns[i] = ciphertext[index:index + num_rows]
        index += num_rows

    # Reconstruct the original text row by row
    plaintext = ''
    for row in range(num_rows):
        for col in range(num_cols):
            if row < len(columns[col]):
                plaintext += columns[col][row]

    return plaintext.replace('_', '')  # Remove padding

# Main interaction
def main():
    while True:
        print("\n=== Columnar Transposition Cipher ===")
        choice = input("Type 'encrypt', 'decrypt', or 'exit': ").strip().lower()

        if choice == 'encrypt':
            text = input("Enter the text to encrypt: ")
            keyword = input("Enter the keyword: ")
            result = columnar_encrypt(text, keyword)
            print("Encrypted text:", result)

        elif choice == 'decrypt':
            text = input("Enter the text to decrypt: ")
            keyword = input("Enter the keyword: ")
            result = columnar_decrypt(text, keyword)
            print("Decrypted text:", result)

        elif choice == 'exit':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please type 'encrypt', 'decrypt', or 'exit'.")

# Run the program
if __name__ == "__main__":
    main()
