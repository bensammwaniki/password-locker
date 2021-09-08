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
