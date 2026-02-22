class Personaje:
    nombre = "Desconocido"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print("Nombre: ", self.nombre)
        print("Fuerza: ", self.fuerza)
        print("Inteligencia: ", self.inteligencia)
        print("Defensa: ", self.defensa)
        print("Vida: ", self.vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia  = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "¡El personaje ha muerto!")
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ataca a", enemigo.nombre, "y le causa", daño)
        print(enemigo.nombre, "tiene", enemigo.vida, "de vida restante.")
        if enemigo.esta_vivo():
            print("La vida de ", enemigo.nombre, "es de", enemigo.vida)
        else:
            enemigo.morir()

mi_personaje = Personaje("DK_GILBERT", 8, 6.5, 7, 100)
mi_enemigo = Personaje("Kevin", 2, 2, 2, 8)
mi_personaje.subir_nivel(2, 1.5, 3)
mi_personaje.atributos()
print(mi_personaje.atacar(mi_enemigo))
mi_enemigo.atributos()
