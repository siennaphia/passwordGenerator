# Password Strength Checker

Password Strength Checker is a command-line Python script that checks the strength of a password. The strength is determined based on various criteria, such as the length, complexity, and the presence of common patterns. If a password is considered weak, the script gives the user an option to generate a strong password.

## Installation

Make sure you have Python 3 installed. You can download it from [here](https://www.python.org/downloads/).

Clone this repository or download the script file to your local machine.

## Usage

You can run the script from the command line with or without a password as a command-line argument:

With a password:
```
python password_strength_checker.py yourpasswordhere
```

Without a password:
```
python password_strength_checker.py
```
If you don't provide a password as an argument, the script will prompt you to enter one.

If the script determines that the password is weak, it will ask if you want to generate a new, strong password. If you choose to do so, it will then ask for the desired length of the new password (minimum 8 characters). 

The new password will contain at least one lowercase letter, one uppercase letter, one digit, and one special character.