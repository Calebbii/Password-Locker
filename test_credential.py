import unittest
from credential import Credential

class Testcredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating credential test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases in credential
        '''
        self.new_credential = Credential("Vannce","1234","0710516225","vannce@gmail.com") #creating credential object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.credential_name,"Vannce")
        self.assertEqual(self.new_credential.password,"1234")
        self.assertEqual(self.new_credential.phone_number,"0710516225")
        self.assertEqual(self.new_credential.email,"vannce@gmail.com")


    def test_save_credential(self):
        '''
        save_credential method saves credential object into the credential_list
        '''
        Credential.credential_list.append(self)

    def test_delete_credential(self):    
        '''
        delete_credential method deletes credential object from the credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Vannce","1234","0710516225","vannce@gmail.com") #new credential
        test_credential.save_credential()

        self.new_credential.delete_credential() #Deleting a credential object
        self.assertEqual(len(Credential.credential_list),3)

    


    def test_find_credential_by_number(self):
        '''
        finds credential object in the credential_list by number
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Vannce","1234","0710516225","vannce@gmail.com") #new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_number("0710516225")
        self.assertEqual(found_credential.email,test_credential.email)


    def test_credential_exists(self):
        '''
        test tocheck if we can return boolean if we can finf a credential
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Vannce","1234","0710516225","vannce@gmail.com") #new credential
        test_credential.save_credential()
         
        credential_exists = Credential.credential_exists("0710516225")
        self.assertTrue(credential_exists)

    def test_credential_display(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credential.display_credentials(),Credential.credential_list)  


if __name__ == '__main__':
    unittest.main()
