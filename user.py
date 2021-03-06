class User:

    user_list = []

    def __init__(self,user_name,password,phone_number,email):
        self.user_name = user_name
        self.password = password
        self.phone_number = phone_number
        self.email = email


    def save_user(self):
        '''
        save_user method saves user object into the user_list
        '''
        User.user_list.append(self)


    def delete_user(self):
        '''
        delete_user method deletes user object from user_list
        '''
        User.user_list.remove(self)


    

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a user that matches that number.

        Args:
        number:Phone number to search for
        Returns:
        User  that matches the number.
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                return user

    @classmethod
    def user_exists(cls,number):
        '''
        Method that checks if a user exists from the user list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                return True

        return False   


    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list         