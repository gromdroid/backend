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
        return Persister.savePassword(temp,email) #change to hashed
    else:
        return 400

def changePassword(id, oldPassword, newPassword):
    return Persister.changePassword(id, oldPassword, newPassword)

def checkPoints(email):
    return Persister.checkPoints(email)

def addPoints(email):
    return Persister.addPoints(email)


def substractPoint(email):
    return Persister.substractPoint(email)


def resetStampCard(email):
    return Persister.resetStampCard(email)


