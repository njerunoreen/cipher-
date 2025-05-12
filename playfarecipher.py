def prepare_text(text, for_encrypt=True):
    text = text.upper().replace("J", "I").replace(" ", "")
    if for_encrypt:
        prepared = ""
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i + 1] if i + 1 < len(text) else "X"
            if a == b:
                prepared += a + "X"
                i += 1
            else:
                prepared += a + b
                i += 2
        if len(prepared) % 2 != 0:
            prepared += "X"
        return prepared
    else:
        return text  # For decryption, we assume the input is already even-paired


def create_grid(keyword):
    keyword = keyword.upper().replace("J", "I")
    seen = set()
    grid = []
    for char in keyword:
        if char not in seen and char.isalpha():
            seen.add(char)
            grid.append(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            grid.append(char)
    return [grid[i:i+5] for i in range(0, 25, 5)]


def find_position(grid, letter):
    for row in range(5):
        for col in range(5):
            if grid[row][col] == letter:
                return row, col
    return None


def encrypt_pair(grid, a, b):
    row1, col1 = find_position(grid, a)
    row2, col2 = find_position(grid, b)

    if row1 == row2:  # Same row
        return grid[row1][(col1 + 1) % 5] + grid[row2][(col2 + 1) % 5]
    elif col1 == col2:  # Same column
        return grid[(row1 + 1) % 5][col1] + grid[(row2 + 1) % 5][col2]
    else:  # Rectangle
        return grid[row1][col2] + grid[row2][col1]


def decrypt_pair(grid, a, b):
    row1, col1 = find_position(grid, a)
    row2, col2 = find_position(grid, b)

    if row1 == row2:  # Same row
        return grid[row1][(col1 - 1) % 5] + grid[row2][(col2 - 1) % 5]
    elif col1 == col2:  # Same column
        return grid[(row1 - 1) % 5][col1] + grid[(row2 - 1) % 5][col2]
    else:  # Rectangle
        return grid[row1][col2] + grid[row2][col1]


def playfair_cipher(text, keyword="KEY", mode="encrypt"):
    grid = create_grid(keyword)
    prepared = prepare_text(text, for_encrypt=(mode == "encrypt"))
    result = ""

    for i in range(0, len(prepared), 2):
        a, b = prepared[i], prepared[i + 1]
        if mode == "encrypt":
            result += encrypt_pair(grid, a, b)
        else:
            result += decrypt_pair(grid, a, b)
    return result


# === Main Interface ===
def main():
    while True:
        choice = input("\nType 'encrypt', 'decrypt', or 'exit': ").strip().lower()
        if choice == "encrypt":
            text = input("Enter text to encrypt: ")
            encrypted = playfair_cipher(text, keyword="KEY", mode="encrypt")
            print("Encrypted text:", encrypted)
        elif choice == "decrypt":
            text = input("Enter text to decrypt: ")
            decrypted = playfair_cipher(text, keyword="KEY", mode="decrypt")
            print("Decrypted text:", decrypted)
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please type 'encrypt', 'decrypt', or 'exit'.")

if __name__ == "__main__":
    main()
