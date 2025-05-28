LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            index = LETTERS.index(char)
            new_index = (index + shift) % 26
            new_char = LETTERS[new_index]
            if is_upper:
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def show_banner():
    banner = r"""

  ______ ______   _______ ______  
 |  ____/ __ \ \ / /_   _|  ____| 
 | |__ | |  | \ V /  | | | |__    
 |  __|| |  | |> <   | | |  __|   
 | |   | |__| / . \ _| |_| |____  
 |_|    \____/_/ \_\_____|______| 

     Caesar Cipher Encrypt/Decrypt Tool
    """
    print(banner)

def main():
    show_banner()
    choice = input("Type 'encode' to encrypt, 'decode' to decrypt: ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == 'encode':
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted message:", encrypted)
    elif choice == 'decode':
        decrypted = caesar_decrypt(message, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice. Please use 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
