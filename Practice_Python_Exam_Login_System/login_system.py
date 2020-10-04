'''
This Python exam will involve implementing a mini log-in system.  Users will be
able to sign up, log in, change their password, and delete their accounts.
'''

def init_db(file):
    '''
    Loads the given .csv file containing user credentials.
    Each row is a comma-separated list including username and password.

    Example(s):
    lbrandon,My_Crazy_Password_1234
    tjones,4er3yw6rt5R
    dennisq,0987poiu1234QwEr

    Stores the usernames and passwords in a users dictionary where the username is the key and the password is the value.

    Creates an empty logged_in dictionary for storing user log-ins where the username is the key and the value is a bool indicating
    if the user is logged in or not.
    '''

    users = {}

    logged_in = {}

    return users, logged_in

def check_username_password(users, username, password):
    '''
    Checks whether the username exists in the users dictionary and that the password matches the username.  Returns boolean.
    '''

    pass

def is_valid_password(password):
    '''
    Checks whether the given password is valid.  Returns boolean.

    The length of a valid password should be at least 8 characters and it should contain
    at least one lowercase character, one uppercase character, and one number.
    '''

    pass

def sign_up(users, logged_in, username, password):
    '''
    Allows users to sign up.
    If the username already exists in the users dictionary, prints a friendly message.
    If the password does not satisfy the rule(s) (not valid), prints a friendly message.
    Otherwise, saves the username and the corresponding password in the users dictionary, and prints a
    success message.

    Note(s):
    The user is not automatically logged in when he/she signs up.
    '''

    pass

def log_in(users, logged_in, username, password):
    '''
    Allows users to log in.
    If the username does not exist in the users dictionary or the password is incorrect, prints an error message.
    Otherwise, saves the username and the value of True in the logged_in dictionary, and prints a welcome message.

    Note(s):
    Even if a user is already logged in, he/she can log in again.
    '''

    pass

def change_password(users, username, old_password, new_password):
    '''
    Allows users to change their password.
    If the username does not exist in the users dictionary, prints an error message.
    If the old_password is incorrect, prints an error message.
    If the new_password does not satisfy the rule(s) (not valid), prints an error message.
    Otherwise, changes the user's password in the users database, and prints a success message.
    '''

    pass

def delete_account(users, logged_in, username, password):
    '''
    Allows users to delete their account.
    If the username does not exist in the users database, prints an error message.
    If the old_password is incorrect, prints an error message.
    Otherwise, deletes the user's account from the users dictionary, and prints a success message.

    Note(s):
    Also deletes the user's information in the logged_in dictionary.
    '''

    pass

def get_sign_ups(users):
    '''
    Returns a list of users who are signed up (in the users dictionary).
    '''

    pass

def get_log_ins(logged_in):
    '''
    Returns a list of users who are logged in (in the logged_in dictionary).
    '''

    pass

def write_users_db(users, file):
    '''
    Writes all usernames and passwords in the users dictionary, to the given file.
    Each row is a comma-separated list including username and password.

    Example(s):
    lbrandon,My_Crazy_Password_1234
    tjones,4er3yw6rt5R
    dennisq,0987poiu1234QwEr
    '''

    pass

def main():

    #create database of users and empty database of logged in users
    users, logged_in = init_db('users.csv')

    while True:

        #print options
        print("Options:\n"
              "Press 1 to log in\n" +
              "Press 2 to sign up\n" +
              "Press 3 to change password\n" +
              "Press 4 to delete account\n" +
              "Press 5 to show statistics (sign ups and log ins)\n" +
              "Press 6 to save all sign ups to the file\n"
              "Press 0 to quit\n")

        #get user input
        option_input = input()

        # try to cast as int
        try:
            option = int(option_input)

        # catch ValueError
        except ValueError:
            print("Invalid option.")

        else:

            if option == 0:
                #quit
                pass
            elif option == 1:
                #log in
                pass
            elif option == 2:
                #sign up
                pass
            elif option == 3:
                #change password
                pass
            elif option == 4:
                #delete account
                pass
            elif option == 5:
                #show statistics
                pass
            elif option == 6:
                # save user credentials to 'users_output.csv'
                pass
                print("Saved!")

            print("=" * 80)


if __name__ == "__main__":
    main()
