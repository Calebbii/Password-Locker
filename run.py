#!/usr/bin/env python3.8
from user import User
from credential import Credential


#functions for user_account

def create_user(user_name,password,phone_number,email):
  '''
  Function to create a new user
  '''
  new_user = User(user_name,password,phone_number,email)
  return new_user

def save_user(user):
    '''
    function to save user
    '''
    User.save_user(user)

def delete_user(user):
    '''
    function to delete user
    '''
    User.delete_user(user)

def find_user(number):
    '''
    function finds user
    '''
    return User.find_by_number(number)

def check_user(number):
    '''
    function to check if user exist by number
    '''
    return User.user_exists(number)

def display_users():
    '''
    function returns all saved users
    '''
    return User.display_users()





#functions for credential_account

def create_user(credentialname,password,phonenumber,email):
  '''
  Function to create new credential
  '''
  new_credential = Credential(credentialname,password,phonenumber,email)
  return new_credential

def save_credential(credential):
    '''
    function to save credential
    '''
    Credential.save_credential(credential)

def delete_credential(credential):
    '''
    function to delete credential
    '''
    Credential.delete_credential(credential)

def find_credential(number):
    '''
    function finds credential
    '''
    return Credential.find_by_number(number)

def check_credential(number):
    '''
    function to check if credential exist by number
    '''
    return Credential.credential_exists(number)

def display_credentials():
    '''
    function returns all saved credentials
    '''
    return User.display_credentials()









def main():
    print("Hello Welcome to your Password Manager\n")
    print("Use these short codes, c - credentials and u - user: create u - create a new user, del u - deletes a user, disp u - display user, find u - find a user, exit - exit the user list, lg - login")


    while True:
            short_code = input().lower()

            if short_code == 'create u':
                    print("New Account")
                    print("-"*15)

                    print ("User name ....")
                    user_name = input()

                    print("Enter password ...")
                    password = input()

                    print("Phone number ...")
                    phone_number = input()

                    print("Email address ...")
                    email = input()


                    save_user(create_user(user_name,password,phone_number,email)) # create and save new user.
                    print ('\n')
                    print(f"New user {user_name} created")
                    print ('\n')




                    #Login 
            if short_code == 'lg':
                print("Welcome !!")
                print("Enter your username")
                input_user_name = input()

                print("Enter your password")
                input_password = input()
                print("-"*10)
                print("-"*60)

                if input_user_name != user.user_name or input_password != password:
                    print("ACCESS DENIED!!")
                    print("Invalid username or password !!")
                    print("Try again")
                else:
                    print("ACCESS GRANTED!!")
                    print(f"Welcome {user_name} to your account")
                    print("Use the following command to do some action with your account: \n create u - command to create new account \n disp u -command to display user details \n find u - command to search for user \n del u - command to delete user \n disp c - command to display credentials \n find c - command to search credentials \n del c - command to delete credentials")

            elif short_code == 'disp u':

                if display_users():
                    print("Here is a list of all your users")
                    print('\n')

                    for user in display_users():
                        print(f"{user.credential_name} .....{user.phone_number}")

                    print('\n')
                else:
                    print('\n')
                    print("No users saved yet")
                    print('\n')




            elif short_code == 'disp c':

                if display_credential():
                    print("Here is a list of all your credentials")
                    print('\n')

                    for user in display_credentials():
                        print(f"{credential.credential_name} .....{credential.phone_number}")

                    print('\n')
                else:
                    print('\n')
                    print("No credentials saved yet")
                    print('\n')          


                #find user
            elif short_code == 'find u':
                print("Enter the number of the user you want to search for")

                search_number = input()
                print("-"*15)
                print("-"*50)
                if check_user(search_number):
                    search_user = find_user(search_number)
                    print(f"{search_user.credential_name}...{search_user.phone_number}")
                    print('-' * 20)

                    print(f"Phone number.......{search_user.phone_number}")
                    print(f"Email address.......{search_user.email}")
                else:
                    print("User does not exist")


                    #find credential
            elif short_code == 'find c':
                print("Enter the number to the credential you want to search for")

                search_number = input()
                print("-"*10)
                print("-"*50)
                if check_existing_credential(search_number):
                    search_credential = find_credential(search_number)
                    print(f"{search_credential.credential_name}")
                    print('-' * 20)

                    print(f"Phone number.......{search_credential.phone_number}")
                    print(f"Email address.......{search_credential.email}")
                else:
                    print("Credential does not exist")



                #delete user
            elif short_code == 'del u':

                print("Enter the number to the user you want to delete")

                delete_number = input()
                print("-"*15)
                print("-"*50)
                if check_user(delete_number):
                    dl_user = find_user(delete_number)
                    print(f"<<{dl_user.credential_name}>> will be deleted")
                    dl_user = delete_user(dl_user)
                    print("User deleted successfully")

                else:
                    print("User does not exist")


                    #delete credential
            elif short_code == 'del c':

                print("Enter the number to the credential you want to delete")

                delete_number = input()
                print("-"*15)
                print("-"*50)
                if check_credential(delete_number):
                    dl_user = find_credential(delete_number)
                    print(f"<<{dl_credential.credential_name}>> will be deleted")
                    dl_user = delete_user(dl_user)
                    print("Credential deleted successfully")

                else:
                    print("Credential does not exist")      

                    
            elif short_code == "exit":
                print("SESSION ENDED")
                break
            else:
                print("")

if __name__ == "__main__":
    main()