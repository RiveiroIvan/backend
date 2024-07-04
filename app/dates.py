class Dates:
    def __init__(self, nombre,apellido, email, DNI, padron):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.DNI = DNI
        self.padron = padron
        
    def get_nombre(self):
        return self.nombre
        
    def get_apellido(self):
        return self.apellido
    
    def get_padron(self):
        return self.padron
