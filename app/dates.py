class Dates:
    def __init__(self, R_usuario, R_email, R_clave):
        self.R_usuario = R_usuario
        self.R_email = R_email
        self.R_clave = R_clave
        
    def get_usuario(self):
        return self.R_usuario
        
    def get_email(self):
        return self.R_email