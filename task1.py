def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            shift_amount = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - shift_base + shift_amount) % 26 + shift_base)
        else:
            result += char
    return result

# Example usage
message = input("Enter message: ")
shift = int(input("Enter shift: "))
mode = input("Mode (encrypt/decrypt): ").lower()

output = caesar_cipher(message, shift, mode)
print(f"Result: {output}")
