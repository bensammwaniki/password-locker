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

