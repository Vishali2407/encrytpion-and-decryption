def encrypt(message, shift):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, shift):
    return encrypt(encrypted_message, -shift)

def main():
    print("Welcome to the Caesar Cipher encryption/decryption tool!")
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (an integer between 1 and 25): "))
    encrypted_message = encrypt(message, shift)
    print("Encrypted message:", encrypted_message)
    decrypted_message = decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
