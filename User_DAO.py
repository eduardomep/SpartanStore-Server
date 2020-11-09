from User import User
class User_DAO:
    
    def __init__(self):
        self.users = []
        self.counter = 0
    def newUser(self,name,last_name,user_name,password,user_type):
        for user in self.users:
            if user.user_name == user_name:
                print('el nombre de usuario ya está en uso')
                return False
        new = User(self.counter,name,last_name,user_name,password,user_type)
        self.users.append(new)
        self.counter += 1
        return True
    def getPassword(self,user_name):
        for user in self.users:
            if user.user_name == user_name:
                print('El usuario existe y su contraseña es:' + user.password)
                return user.password
        print('el usuario no existe')
        return False
    def login(self,user_name,password):
        for user in self.users:
            if user.user_name == user_name and user.password == password:
                return True
        return False
    def getUserRole(self,user_name):
        for user in self.users:
            if user.user_name == user_name:
                return user.user_type
        return False



