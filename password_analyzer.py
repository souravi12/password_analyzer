import getpass
import string


def check_pwd():
    password = getpass.getpass("Enter your password: ")
    score=0
    #adding here ki how many are there ig?
   
    lower_count = upper_count = num_count = wspace_count = special_count = 0
    for char in (password):
        
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char.isdigit():
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1
       
    if len(password) >= 8: score += 1
    if lower_count > 0: score += 1
    if upper_count > 0: score += 1
    if num_count > 0: score += 1
    if special_count > 0: score += 1

    print("\nPassword check")
    


    if upper_count ==0:
        print("hint: Add uppercase letters")
    if lower_count ==0:
        print("Add lowercase letters")
    if num_count ==0:
        print("Add numbers")                    
    if special_count ==0:
        print("Add special characters") 

    if   score == 1: 
        remarks = "Very Bad Password!!! Change ASAP"
    elif score == 2:
        remarks = "Not A Good Password!!! Change ASAP"
    elif score ==3:
        remarks = "It's a weak password, consider changing"
    elif score == 4:
        remarks = "It's a hard password, but can be better"
    elif score == 5:

        remarks = "A very strong password"
 
    print(f"Hint: {remarks}")

def ask_pwd(another_pwd=False):
    while True:
        if another_pwd:
            choice=input('Do you want to enter another password (y/n):')    
        else:
            choice=input('Do you want to check your password (y/n):')
        if choice.lower() == 'y':
            check_pwd()
            another_pwd=True
        elif choice.lower() == 'n':
            print('Thank you for using the password checker <3')
            return False
        else:
            print('Do you want to try again?')
if __name__ == '__main__':
    print('welcome to PWD checker ^^')

    ask_pw = ask_pwd()
    while ask_pw:
        check_pwd()
        ask_pw = ask_pwd(True)
