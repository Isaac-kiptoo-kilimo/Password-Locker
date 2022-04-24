import unittest
from credentials import Credentials
class User:

    users = [
        {
            "id": 1,
            "fullname": "Dalmas Ogembo",
            "username": "dalmasonto",
            "email": "dalmasogembo@gmail.com",
            "password": "password"
        },
        {
            "id": 2,
            "fullname": "Isaac Kiptoo",
            "username": "isaac",
            "email": "isaac@gmail.com",
            "password": "password"
        },

    ]

    def __init__(self,id,fullname,username,password,email):
        self.id=id
        self.fullname=fullname
        self.username=username
        self.pasaword=password
        self.email=email

        # pass

    @classmethod
    def createUser(cls, user):
        count = len(cls.users)
        if count > 0:
            id_ = cls.users[count - 1]['id'] + 1
            user["id"] = id_
        else:
            user["id"] = 1
        cls.users.append(user)
        return {"message": "User created successfully", "data": user, "statusCode": 201}

    @classmethod
    def deleteUser(cls, user_id):
        res = cls.getUser(user_id)
        if res["statusCode"] == 200:
            cls.users.remove(res['data'])
            return {
                "message": "User deleted successfully",
                "data": None,
                "statusCode": 200
            }
        else:
            return res

    @classmethod
    def authenticateUser(cls, credentials):
        if credentials['username'] and credentials['password']:
            for user in cls.users:
                if user['username'] == credentials['username']:
                    if user['password'] == credentials['password']:
                        cls.loggedInUser = user
                        return {"message": "User logged in successfully", "data": user, "statusCode": 200}
                    else:
                        return {"message": "User with this password not found", "data": None, "statusCode": 404}
            return {"message": "User with this credentials Not found", "data": None, "statusCode": 404}

    @classmethod
    def unAuthenticateUser(cls):
        cls.loggedInUser = None
        return {"message": "User logged out successfully", "data": None, "statusCode": 200}

    @classmethod
    def getUser(cls, user_id):
        for user in cls.users:
            if user["id"] == int(user_id):
                return {"message": "User found", "data": user, "statusCode": 200}
        return {"message": "User not found", "data": None, "statusCode": 404}

    @classmethod
    def getLoggedInUser(cls):
        if cls.loggedInUser:
            return {"message": "A user is logged in", "data": cls.loggedInUser, "statusCode": 200}
        return {"message": "There is no logged in User", "data": None, "statusCode": 403}

    @classmethod
    def getCredentials(cls):
        if cls.loggedInUser:
            creds = Credentials.getUserCredentials(cls.loggedInUser["id"])
            return {"message": "Found Credentials", "data": creds["data"], "statusCode": 200}
        else:
            return {"message": "No logged in user", "data": None, "statusCode": 404}

   
print(User)