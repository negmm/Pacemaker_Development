class PacemakerUser:
    
    totalUsers = 0
    
    def __init__(self, username, password):
        self.u = username
        self.p = password

    
    #Getters
    def gettotalUsers(self):
        return totalUsers
    def getUsername(self):
        return self.u
    def getPassword(self):
        return self.p
