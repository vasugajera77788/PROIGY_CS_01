# Simple Caesar Cipher Program

def encrypt(text, shift):
    result = ""  # This will store the encrypted message
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just shifting backward

# Get input from the user
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
operation = input("Choose operation - encrypt or decrypt: ").strip().lower()

# Perform the chosen operation
if operation == 'encrypt':
    output = encrypt(message, shift)
    print("Encrypted message:", output)
elif operation == 'decrypt':
    output = decrypt(message, shift)
    print("Decrypted message:", output)
else:
    print("Invalid operation. Choose 'encrypt' or 'decrypt'.")
