import math

# First Columnar Transposition (Encrypt)
def columnar_encrypt(plaintext, keyword):
    plaintext = plaintext.replace(" ", "").upper()
    keyword = keyword.upper()
    
    num_cols = len(keyword)
    num_rows = math.ceil(len(plaintext) / num_cols)
    
    padding = (num_cols * num_rows) - len(plaintext)
    plaintext += '_' * padding
    
    grid = ['' for _ in range(num_cols)]
    for i in range(len(plaintext)):
        col = i % num_cols
        grid[col] += plaintext[i]
    
    sorted_key = sorted((char, i) for i, char in enumerate(keyword))
    ciphertext = ''
    for _, i in sorted_key:
        ciphertext += grid[i]
    
    return ciphertext

# Double Transposition Cipher Encrypt
def double_transposition_encrypt(plaintext, keyword1, keyword2):
    # First transposition
    first_transposition = columnar_encrypt(plaintext, keyword1)
    # Second transposition
    second_transposition = columnar_encrypt(first_transposition, keyword2)
    
    return second_transposition

# Main interaction loop
def main():
    while True:
        print("\n=== Double Transposition Cipher ===")
        choice = input("Type 'encrypt', 'decrypt', or 'exit': ").strip().lower()

        if choice == 'encrypt':
            text = input("Enter the text to encrypt: ")
            keyword1 = input("Enter the first keyword: ")
            keyword2 = input("Enter the second keyword: ")
            encrypted = double_transposition_encrypt(text, keyword1, keyword2)
            print("Encrypted text:", encrypted)

        elif choice == 'exit':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

