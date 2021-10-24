class Credential:

    credential_list = []

    def __init__(self,credential_name,password,phone_number,email):
        self.credential_name = credential_name
        self.password = password
        self.phone_number = phone_number
        self.email = email


    def save_credential(self):
        '''
        save_credential method saves credential object into the credential_list
        '''
        Credential.credential_list.append(self)


    def delete_credential(self):
        '''
        delete_credential method deletes credential object from credential_list
        '''
        Credential.credential_list.remove(self)
    

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a credential that matches that number.

        Args:
        number: Phone number to search for
        Returns:
        Credential  that matches the number.
        '''
        for credential in cls.credential_list:
            if credential.phone_number == number:
                return credential

    @classmethod
    def credential_exists(cls,number):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.phone_number == number:
                return True

        return False   


    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list         