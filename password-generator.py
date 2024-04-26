import random
import string

def generate_password(length=12, min_uppercase=1, min_lowercase=1, min_digits=1, min_special=1):
    """Generate a random password with customizable complexity."""
    if length < (min_uppercase + min_lowercase + min_digits + min_special):
        raise ValueError("Total minimum characters required exceeds password length.")

    password = ''
    # Generate required number of uppercase letters
    password += ''.join(random.choice(string.ascii_uppercase) for _ in range(min_uppercase))
    # Generate required number of lowercase letters
    password += ''.join(random.choice(string.ascii_lowercase) for _ in range(min_lowercase))
    # Generate required number of digits
    password += ''.join(random.choice(string.digits) for _ in range(min_digits))
    # Generate required number of special characters
    password += ''.join(random.choice(string.punctuation) for _ in range(min_special))
    # Fill the remaining length with random characters
    remaining_length = length - len(password)
    password += ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))
    # Shuffle the password characters to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the length of the password: "))
        min_uppercase = int(input("Enter minimum number of uppercase letters: "))
        min_lowercase = int(input("Enter minimum number of lowercase letters: "))
        min_digits = int(input("Enter minimum number of digits: "))
        min_special = int(input("Enter minimum number of special characters: "))

        password = generate_password(password_length, min_uppercase, min_lowercase, min_digits, min_special)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)
