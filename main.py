import random
print("\n Welcome to Ultimate Password Generator\n")

def genrate_password(len):
    len = int(len)
    smallLetters = "abcdefghijklmnopqrstuvwxyz"
    capitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    specialCharacters = "!@#$%^&*()[]{}<>?/.,;:|"
    allCharacters = [smallLetters, capitalLetters, numbers, specialCharacters]
    password = ""
    for i in range(len):
        c = random.choice(allCharacters)
        password += random.choice(c)
    print("Your generated password is: ", password)

# Nana Encryption
def encrypt(text):
    text = str(text)
    text_list = list(text)
    key_list = list(text)
    key_length = len(key_list)
    print("key_list: ", key_list)
    print("key length: ", key_length)

encrypt("Hello")