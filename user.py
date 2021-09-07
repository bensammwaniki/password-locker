
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

        