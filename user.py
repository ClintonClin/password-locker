import pyperclip
import random

global user_list
class User:
    """
    Class that generates new instances of the user to sign up.
    """
    info_list = [] #empty info list
    user_list = [] #Empty user list
    #this are instance variables
    def __init__(self,username,password):
        self.username = username
        self.password = password

        def register(self)
       User.User_list.append(self)

class Info:
    '''
    Class to create new infomation of a user
    '''
    info_list = []
    users_info = []

    @classmethod
    def __init__(self, username_name, account_name, info_details, password):
        self.username_name = username_name
        self.account_name = account_name
        self.info_details = info_details
        self.password = password

    def save_info(self)
        '''
        created a function to new info of a user
        '''
        Info.info_list.append(self)
        