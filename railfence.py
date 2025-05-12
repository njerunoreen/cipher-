# Encrypt using Rail Fence Cipher
def rail_fence_encrypt(plaintext, num_rails):
    if num_rails <= 1:
        return plaintext

    plaintext = plaintext.replace(" ", "").upper()
    rail = ['' for _ in range(num_rails)]
    direction_down = False
    row = 0

    for char in plaintext:
        rail[row] += char
        # Change direction if we hit top or bottom rail
        if row == 0 or row == num_rails - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1

    return ''.join(rail)

# Decrypt using Rail Fence Cipher
def rail_fence_decrypt(ciphertext, num_rails):
    if num_rails <= 1:
        return ciphertext

    # Create a placeholder matrix
    length = len(ciphertext)
    matrix = [['\n' for _ in range(length)] for _ in range(num_rails)]

    # Mark positions to fill later
    direction_down = None
    row, col = 0, 0
    for _ in range(length):
        if row == 0:
            direction_down = True
        if row == num_rails - 1:
            direction_down = False
        matrix[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    # Fill the marked positions with characters from ciphertext
    index = 0
    for r in range(num_rails):
        for c in range(length):
            if matrix[r][c] == '*' and index < length:
                matrix[r][c] = ciphertext[index]
                index += 1

    # Read the matrix in zigzag to reconstruct plaintext
    result = ''
    row, col = 0, 0
    for _ in range(length):
        result += matrix[row][col]
        if row == 0:
            direction_down = True
        if row == num_rails - 1:
            direction_down = False
        col += 1
        row += 1 if direction_down else -1

    return result

# Main interaction loop
def main():
    while True:
        print("\n=== Rail Fence Cipher ===")
        choice = input("Type 'encrypt', 'decrypt', or 'exit': ").strip().lower()

        if choice == 'encrypt':
            text = input("Enter the text to encrypt: ")
            rails = int(input("Enter the number of rails: "))
            encrypted = rail_fence_encrypt(text, rails)
            print("Encrypted text:", encrypted)

        elif choice == 'decrypt':
            text = input("Enter the text to decrypt: ")
            rails = int(input("Enter the number of rails: "))
            decrypted = rail_fence_decrypt(text, rails)
            print("Decrypted text:", decrypted)

        elif choice == 'exit':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
