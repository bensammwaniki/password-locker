from user import User,Credentials


def new_user(username,password):
    """
    function to create  new user
    """
    newuser = User(username,password)
    return newuser


def saveUser(user):
    """
    function to save user
    """
    user.save_user()

def display_user():
    """
    display existing user
    """
    return User.display_user()   

def login_user(username,password):
    """
    function that checks whether a user exist and then login the user.
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user   

def create_new_credential(account,userName,password):
    """
    creates new credentials
    """
    new_credential = Credentials(account,userName,password)
    return new_credential

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
    """
    A function that copies the password .
    """
    return Credentials.copy_password(account)