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
    return User.show_users()   

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
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials.save_details()

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
def find_credential(account):
    """
    Function that finds a Credentials by an account 
    """
    return Credentials.searchcredential(account)    

def passlocker():
    print("Hello Please enter one of the following short code to proceed.\n CA ---  Create New Account  \n HA ---  Have An Account  \n")
    short_code=input("").lower().strip()  
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        saveUser(new_user(username,password))
        print("="*85)
        print(f"Hello {username}, Your account has been created succesfully!")
        print("="*50)
    elif short_code == "li":
        print("*"*50)
        print("Enter your Username and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To Passlock.\nThis is your pass word{password}")  
            print('\n')
    while True:
        print("Hi use these short codes to access the data :\n CC - Create a new credential \n DC - Display Credentials \n GP - Generate A randomn password \n DEL - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} \n\n- Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_user():
                print("Here's your list of acoounts: ")
                
                print('*' * 30)
                print('_'* 30)
                for account in display_user():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("................Sorry you don't have any credentials saved yet..........")    
        elif short_code == "del":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.deleteusercredentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")
        elif short_code == 'gp':

            password = generate_Password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passlocker.. See you next time!")
            break
        else:
            print("Sorry Check your entry and try again")

if __name__ == '__main__':
    passlocker()     