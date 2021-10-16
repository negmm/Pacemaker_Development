import os

#%% Verify user logins
def verify(username, password):
    login = False
    users = os.listdir("Users/")
    for s in range(len(users)): 
        users[s] = users[s].strip(".txt")
    if ((username in users) == False):
        return login
    name = "Users/" + username +".txt"
    file = open(name, "r")
    if (password == file.read()):
        login = True
    return login 

#%% Register a new user
def register(username, password):
    newUser = -1
    path = "Users/"
    numUsers = len(os.listdir(path))
    if numUsers < 10:
        users = os.listdir(path)
        for s in range(len(users)): 
            users[s] = users[s].strip(".txt")
        if (username in users):
            newUser = 0
        else:
            name = path + username +".txt"
            file = open(name, "w")
            file.write(password)
            file.close()
            newUser = 1
    return newUser
