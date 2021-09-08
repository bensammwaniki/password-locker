
class User:
    '''
    initialize class user
    '''
    user = []
    def __init__(self,username,password):
        '''
        Args:
        username(string)
        password(string)

        '''
        self.username=username
        self.password=password
    
    def save_user (self):
        """
        A method to saves a new user instace into the user
        """
        User.user.append(self)


    @classmethod
    def show_users(show):
        return show.user


    def delete_user(self):
        '''
        delete method deletes an account from the users list
        '''
        User.user.remove(self)

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
        for user in User.user_list:
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
                