from Database import Persister

def getPerson(person_id):
    return Persister.getPerson(person_id)

def getUserByEmail(emailLogin):
    return Persister.getUserWithEmail(emailLogin)

def getEmail(emailLogin):
    return Persister.getEmail(emailLogin)

def getPassword(email):
    return Persister.getPassword(email)


def saveNewPassword(temp,email):
    if Persister.checkEmailExistance(email):
        return Persister.savePassword(temp,email)
    else:
        return 400

def checkPoints():
    pass