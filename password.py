import re
import sys
import string
import random
from getpass import getpass

def password_strength_checker(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Weak: Password should contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Weak: Password should contain at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Weak: Password should contain at least one number."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password should contain at least one special character."
    common_patterns = ["123", "abc", "password", "qwerty", "admin", "pass", "abcd"]
    if any(pattern in password for pattern in common_patterns):
        return "Weak: Password should not contain common patterns."
    return "Strong: The password passed all checks."

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = []
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))
    for i in range(length - 4):
        password.append(random.choice(all_characters))
    random.shuffle(password)
    return "".join(password)

def main():
    if len(sys.argv) < 2:
        password = getpass("Enter your password: ")
    else:
        password = sys.argv[1]

    strength_message = password_strength_checker(password)

    print(strength_message)

    if "Weak" in strength_message:
        response = input("Your password could be stronger. Would you like to create a new one? (yes/no): ")
        if response.lower() == "yes":
            while True:
                length = input("Enter the length of the new password (minimum 8 characters): ")
                try:
                    length = int(length)
                    if length < 8:
                        print("The length should be at least 8.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            new_password = generate_password(length)
            print("Your new password is: ", new_password)
            print(password_strength_checker(new_password))

if __name__ == "__main__":
    main()
