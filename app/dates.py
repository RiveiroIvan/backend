class Dates:
    def __init__(self, nombre,apellido, email, DNI ):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.DNI = DNI
        
        
    def get_nombre(self):
        return self.nombre
        
    def get_apellido(self):
        return self.apellido
