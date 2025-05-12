# Encrypt using Scytale Cipher
def scytale_encrypt(plaintext, num_columns):
    # Remove spaces and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()

    # Calculate the number of rows needed
    num_rows = len(plaintext) // num_columns
    if len(plaintext) % num_columns != 0:
        num_rows += 1  # Add an extra row if the plaintext doesn't fit perfectly

    # Create a list of empty strings for each column
    grid = ['' for _ in range(num_columns)]

    # Fill the grid column by column
    for i in range(len(plaintext)):
        grid[i % num_columns] += plaintext[i]

    # Join all columns to get the ciphertext
    return ''.join(grid)

# Decrypt using Scytale Cipher
def scytale_decrypt(ciphertext, num_columns):
    # Calculate the number of rows
    num_rows = len(ciphertext) // num_columns
    if len(ciphertext) % num_columns != 0:
        num_rows += 1

    # Create a list to store the grid
    grid = ['' for _ in range(num_rows)]

    # Fill the grid row by row
    index = 0
    for col in range(num_columns):
        for row in range(num_rows):
            if index < len(ciphertext):
                grid[row] += ciphertext[index]
                index += 1

    # Join all rows to get the decrypted message
    return ''.join(grid)

# Main interaction loop
def main():
    while True:
        print("\n=== Scytale Cipher ===")
        choice = input("Type 'encrypt', 'decrypt', or 'exit': ").strip().lower()

        if choice == 'encrypt':
            text = input("Enter the text to encrypt: ")
            columns = int(input("Enter the number of columns: "))
            encrypted = scytale_encrypt(text, columns)
            print("Encrypted text:", encrypted)

        elif choice == 'decrypt':
            text = input("Enter the text to decrypt: ")
            columns = int(input("Enter the number of columns: "))
            decrypted = scytale_decrypt(text, columns)
            print("Decrypted text:", decrypted)

        elif choice == 'exit':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
