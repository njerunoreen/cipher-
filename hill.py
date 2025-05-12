# Hill Cipher (2x2) without NumPy

# Convert a letter to number (A=0, B=1, ..., Z=25)
def letter_to_num(c):
    return ord(c.upper()) - ord('A')

# Convert number to letter
def num_to_letter(n):
    return chr((n % 26) + ord('A'))

# Modular inverse using Extended Euclidean Algorithm
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Get inverse of 2x2 matrix modulo 26
def matrix_inverse_2x2(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    det = (a * d - b * c) % 26
    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        raise ValueError("Matrix is not invertible.")

    # Adjugate matrix and apply modular inverse
    inv_matrix = [
        [(d * det_inv) % 26, (-b * det_inv) % 26],
        [(-c * det_inv) % 26, (a * det_inv) % 26]
    ]
    return inv_matrix

# Encrypt a 2-letter block
def encrypt_block(block, matrix):
    x = letter_to_num(block[0])
    y = letter_to_num(block[1])
    a = (matrix[0][0] * x + matrix[0][1] * y) % 26
    b = (matrix[1][0] * x + matrix[1][1] * y) % 26
    return num_to_letter(a) + num_to_letter(b)

# Hill encryption
def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += 'X'  # Padding if odd length

    cipher = ''
    for i in range(0, len(plaintext), 2):
        cipher += encrypt_block(plaintext[i:i+2], key_matrix)
    return cipher

# Hill decryption
def hill_decrypt(ciphertext, key_matrix):
    inv_matrix = matrix_inverse_2x2(key_matrix)
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        plaintext += encrypt_block(ciphertext[i:i+2], inv_matrix)
    return plaintext

# === Example Usage ===
key = [[3, 3], [2, 5]]  # Make sure this matrix is invertible mod 26
plaintext = input("Enter plaintext to encrypt: ")
cipher = hill_encrypt(plaintext, key)
print("Encrypted:", cipher)

decrypted = hill_decrypt(cipher, key)
print("Decrypted:", decrypted)
