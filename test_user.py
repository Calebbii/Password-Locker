import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating user test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases in User
        '''
        self.new_user = User("Vannce","1234","0710516225","vannce@gmail.com") #creating user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"Vannce")
        self.assertEqual(self.new_user.password,"1234")
        self.assertEqual(self.new_user.phone_number,"0710516225")
        self.assertEqual(self.new_user.email,"vannce@gmail.com")
        # self.user_name = user_name
        # self.password = password
        # self.phone_number = phone_number


    def test_save_user(self):
        '''
        save_user method saves user object into the user_list
        '''
        User.user_list.append(self)

    def test_delete_user(self):    
        '''
        delete_user method deletes user object from the user list
        '''
        self.new_user.save_user()
        test_user = User("Vannce","1234","0710516225","vannce@gmail.com") #new user
        test_user.save_user()

        self.new_user.delete_user() #Deleting a user object
        self.assertEqual(len(User.user_list),1)
    

    # def test_save_multiple_user(self):
    #     '''
    #     test_save_multiple_user checks if multiple user object can be saved to the user_list
    #     '''
    #     self.new_user.save_user()
    #     test_user = User("Vannce","1234","0710516225","vannce@gmail.com") #new user
    #     test_user.save_user()

    #     self.assertEqual(len(User.user_list),2)


    def test_find_user_by_number(self):
        '''
        finds user object in the user_list by number
        '''
        self.new_user.save_user()
        test_user = User("Vannce","1234","0710516225","vannce@gmail.com") #new user
        test_user.save_user()

        found_user = User.find_by_number("0710516225")
        self.assertEqual(found_user.email,test_user.email)


    def test_user_exists(self):
        '''
        test to check if we can return boolean if we can find a user
        '''
        self.new_user.save_user()
        test_user = User("Vannce","1234","0710516225","vannce@gmail.com") #new user
        test_user.save_user()
         
        user_exists = User.user_exists("0710516225")
        self.assertTrue(user_exists)

    def test_user_display(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)  


if __name__ == '__main__':
    unittest.main()
