
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
    def verify_user(cls,username, password):
        """
        verify if the user is in our user_list 
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

    def __init__(self,account,userName, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password
    
    def save_details(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)   