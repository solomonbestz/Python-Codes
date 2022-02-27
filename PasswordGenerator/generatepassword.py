import string
import secrets



def generatePassWord(length = 15, upper = True, lower = True, symbol = True):
    password = ""
    if upper: 
        password += string.ascii_uppercase
    if lower:
        password += string.ascii_lowercase
    if symbol:
        password += string.punctuation

    return "".join([secrets.choice(password) for n in range(length)])



if __name__== "__main__":
    print(generatePassWord())
