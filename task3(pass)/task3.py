import secrets

def generate_password(length):
    password = ''
    for _ in range(length):
        char = chr(secrets.randbelow(94) + 33)
        password += char
    return password

def main():
    print("Password Generator")
    while True:
        try:
            password_length = int(input("Enter the  length of the password: "))
            if password_length <= 0:
                print("Please enter a positive length for the password.")
                continue
            password = generate_password(password_length)
            print("Generated Password:", password)
            generate_another = input("Generate another password? (yes/no): ").lower()
            if generate_another != 'yes':
                break
        except ValueError:
            print("Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
