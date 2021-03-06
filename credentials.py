# import random
# chars="abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ123456789!@#$&"
class Credentials:
   
    credentials = [
        {
            "id": 1,
            "user": 1,
            "platform": "Twitter",
            "password": "SomeTwitterPassword123"
        },
        {
            "id": 2,
            "user": 2,
            "platform": "Facebook",
            "password": "SomeFacebookPassword123"
        }
    ]


    def __init__(self):
        pass


    @classmethod
    def createCredential(cls, credential):
        '''
        function that will be used to create platform credentials
        '''
        count = len(cls.credentials)
        if count > 0:
            id_ = cls.credentials[count - 1]['id'] + 1
            credential["id"] =int(id_)
        else:
            credential["id"] = 1
        cls.credentials.append(credential)
        return {"message": "Credential created successfully", "data": credential, "statusCode": 201}

    # @classmethod
    # def generated_password(cls,range):
    #     password_len=int(10)
    #     password_count=int(1)
    #     for x in range(0,password_count):
    #         password=""
    #         for x in range(0,password_len):
    #             password_char=random.choice(chars)
    #             password1=password + password_char
    #             cls.range.append(password1)
    #     return {"message": "password generated successfully", "data": range, "statusCode": 200}

    @classmethod
    def getCredential(cls, cred_id):
        '''
        Method that takes in a id and returns a credentials that matches that id.
        '''
        for cred in cls.credentials:
            if cred["id"] == int(cred_id):
                return {"message": "Credential found", "data": cred, "statusCode": 200}
        return {"message": "Credential not found", "data": None, "statusCode": 404}
    
    @classmethod
    def getUserCredentials(cls, user_id):
        '''
        Method that takes in a id and returns a credentials that matches that id.
        '''
        creds = []
        for cred in cls.credentials:
            if cred["user"] == int(user_id):
                creds.append(cred)

        return {"message": "Found Credentials", "data": creds, "statusCode": 404}

    @classmethod
    def deleteCredential(cls, cred_id):
        '''
        deleteCredential method deletes a stored data of the credentials from the credentials list
        '''
        res = cls.getCredential(cred_id)
        if res["statusCode"] == 200:
            cls.credentials.remove(res['data'])
            return {
                "message": "Credential deleted successfully",
                "data": None,
                "statusCode": 200
            }
        else:
            return res
