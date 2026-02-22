class Personaje:
    nombre = "Desconocido"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
    
    def atributos(self):
        print("Nombre: ", self.__nombre)
        print("Fuerza: ", self.__fuerza)
        print("Inteligencia: ", self.__inteligencia)
        print("Defensa: ", self.__defensa)
        print("Vida: ", self.__vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia  = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.__vida = 0
        print(self.nombre, "¡El personaje ha muerto!")
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.__nombre, "ataca a", enemigo.nombre, "y le causa", daño)
        print(enemigo.nombre, "tiene", enemigo.vida, "de vida restante.")
        if enemigo.esta_vivo():
            print("La vida de ", enemigo.nombre, "es de", enemigo.vida)
        else:
            enemigo.morir()
            
    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error, valores negativos no son permitidos")
        else:            
            self.__fuerza = fuerza

mi_personaje = Personaje("DK_GILBERT", 8, 6.5, 7, 100)
mi_enemigo = Personaje("Wolfplayer", 1, 1, 1, 100)
mi_personaje.atributos()
mi_personaje.subir_nivel(2, 1.5, 3)
