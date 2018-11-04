import random  
from user import User, Info
import pyperclip

def register_user(username, password)
    '''
    creating a function to create users to the system
    '''
    new_user = User(username, password)
    return new_user

def save_user(user)
    '''
    Created a user function to save the new user
    '''
    User.save_user(user)

def create_info(username_name, account_name, info_details, password)
    '''
    function to create new information of a user
    '''
    new_info = Info(username_name,account_name, info_details, password)
    return new_info
    
