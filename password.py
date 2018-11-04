import random  
from user import User, Info
# import pyperclip

def register_user(username, password):
    '''
    creating a function to create users to the system
    '''
    new_user = User(username, password)
    return new_user

def save_user(user):
    '''
    Created a user function to save the new user
    '''
    User.save_user(user)

def check_user(username, password):
    '''
    function for verifying  user
    '''
    checking_user = Info.check_User(username, password)
    return checking_user

def create_info(username_name, account_name, info_details, password):
    '''
    function to create new information of a user
    '''
    new_info = Info(username_name,account_name, info_details, password)
    return new_info
    
def save_info(info):
    '''
    function to save new info inputed by the user
    '''
    Info.save_info(info)

def clipboard_info():
    '''
    function that copies my info to the clipboard
    '''
    return Info.clipboard_info(info_details)

def main():
    print("**"*30)
    print("Choose one option below \n 1. Create account \n 2. sign in \n 3. quit \n")
    
    choice = input()
    if choice == "3":
        sys.exit()

    elif choice == "1":
        print("**"*30)
        print("Create a new account")
        print ("\n")
        username = input('Create a username')
        password= input("Create password")
        save_user(register_user(username, password))
        print("Account created successfully!!")

    elif choice == "2":
        print("**"*30)
        print("Log in by entering your account credentials")
        username = ("Enter your username")
        password = ("Enter your password")





    
        


