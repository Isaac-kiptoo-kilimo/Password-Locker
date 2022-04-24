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
        count = len(cls.credentials)
        if count > 0:
            id_ = cls.credentials[count - 1]['id'] + 1
            credential["id"] = id_
        else:
            credential["id"] = 1
        cls.credentials.append(credential)
        return {"message": "Credential created successfully", "data": credential, "statusCode": 201}

    @classmethod
    def getCredential(cls, cred_id):
        for cred in cls.credentials:
            if cred["id"] == int(cred_id):
                return {"message": "Credential found", "data": cred, "statusCode": 200}
        return {"message": "Credential not found", "data": None, "statusCode": 404}
    
    @classmethod
    def getUserCredentials(cls, user_id):
        creds = []
        for cred in cls.credentials:
            if cred["user"] == int(user_id):
                creds.append(cred)

        return {"message": "Found Credentials", "data": creds, "statusCode": 404}

    @classmethod
    def deleteCredential(cls, cred_id):
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
