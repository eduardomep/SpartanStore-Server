class User:
    def __init__(self,id,name,last_name,user_name,password,user_type):
        self.id = id 
        self.name = name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.user_type = user_type
    # def auth (self,user_name,password):
    #     if self.user_name == user_name and self.password == password:
    #         print("Bienvenido")
    #         return True
    #     print("Datos erroneos")
    #     return False
    # def get_password (self,user_name):
    #     if self.user_name == user_name:
    #         return True
    #     return False


