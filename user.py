import pyperclip
import string

import random
class User:
    '''
    initialize class user
    '''
    user_item = []
    def __init__(self,username,password):
        '''
        Args:
        username(string)
        password(string)

        '''
        self.username=username
        self.password=password
    
    def save_user(self):
        """
        A method to saves a new user instace into the user
        """
        User.user_item.append(self)

    @classmethod
    def show_users(show):
        return show.user_item


    def delete_user(self):
        '''
        delete method deletes an account from the users list
        '''
        User.user_item.remove(self)

class Credentials():
    """
    Create credentials class
    """
    credentials_list = []
    @classmethod
    def verify_user(show,username, password):
        """
        verify if the user is in our user_list 
        """
        a_user = ""
        for user in User.user_item:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

    def __init__(self,account,username, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.userName = username
        self.password = password
    
    def save_details(self):
        """
        store a new credential
        """
        Credentials.credentials_list.append(self)

    def deleteusercredentials(self):
        """
        delete user credentials
        """
        Credentials.credentials_list.remove(self)
    @classmethod
    def searchcredential(show, account):
        """
        Method that takes in a account_name and returns the details matching that account_name.
        """
        for match in show.credentials_list:
            if match.account == account:
                return match   
    @classmethod
    def copy_password(show,account):
        matched = Credentials.searchcredential(account)
        pyperclip.copy(matched.password)     
    @classmethod
    def credential_exist(show, account):
        """
        Method that checks if a credential exists.
        """
        for credential in show.credentials_list:
            if credential.account == account:
                return True
            else:
             return False     

    @classmethod
    def display_credentials(show):
        """
        Method that returns all items in the credentials list
        """
        return show.credentials_list

    def generatePassword(stringLength=8):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))
              