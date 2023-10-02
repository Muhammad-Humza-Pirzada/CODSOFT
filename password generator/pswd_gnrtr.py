import random
import string

print("~~~~~~~Welcome to Password Generator~~~~~~~")

def Password_Generator():
    pass_length = int(input("~~~~~~~Enter Password Length That You Want: "))
    lowerData = string.ascii_lowercase
    upperData = string.ascii_uppercase
    digitData = string.digits
    symbolsData = string.punctuation
    combineData = lowerData+upperData+digitData+symbolsData
    pswd = "".join(random.sample(combineData, pass_length))
    if len(pswd) >= 10:
        print("Password length is out of 10 please enter under 10 or equal to 10")
    else:
        print("Random Password has been generated succesfully according to your length \n")
        print(f"This is Ramdom Passwod --> {pswd} \n")
    
    Password_Generator()

Password_Generator()