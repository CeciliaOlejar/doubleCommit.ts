from logger_base import log

class Persona:
    def __init__(self, id_persona = None, nombre = None, apellido = None, email = None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        
    def __str__(self):
        return f'''
            Id Persona: {self._id_persona},
            Nombre: {self._nombre},
            Apellido: {self._apellido},
            Email: {self._email}
        '''
        
    @property
    def id_persona(self):
        return self._id_persona
    
    @id_persona.setter
    def id_persona(self, nombre):
        self._nombre = nombre
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def email(self):
        return self._email
    
    email.setter
    def email(self, email):
        self._email = email
        

if __name__ == "__main__":
    persona1 = Persona(1, "Mario", "Meza", "mario.meza@gmail.com")
    log.debug(persona1)
    persona2 = Persona(2, "Pepe", "Mujica")
    log.debug(persona2)
    persona1 = Persona(id_persona=1)
    log.debug(persona1)