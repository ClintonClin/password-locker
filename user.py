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