from user import User


def function():
	print("               ____                                                      ")
	print("              |  _ \                    ||||                             ")
	print("              | |_) )  ____  ___   ___  ||||                             ")
	print("              |  __/  / _  |/ __  / __  ||||                             ")
	print("              | |    / (_| |\__ \ \__ \ ||||________                     ")
	print("              |_|    \_____| ___/  ___/ ||||________|                    ")
function()

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
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user   
