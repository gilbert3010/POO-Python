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
        self.inteligencia = self.inteligencia + inteligencia
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

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: 1. Colmillo de Acero (daño 150), 2. Colmillo Sagrado (daño 100): "))
        if opcion == 1:
            self.espada = "Colmillo de Acero"
            self.fuerza = self.fuerza + 150
        elif opcion == 2:
            self.espada = "Colmillo Sagrado"
            self.fuerza = 100
        else:
            print("Opción no válida")
    
    def atributos(self):
        super().atributos()
        print("Espada: ", self.espada)
    
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

class Sacerdote(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma_sagrada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arma_sagrada = arma_sagrada
    
    def atributos(self):
        super().atributos()
        print("Arma Sagrada: ", self.arma_sagrada)
    
    def daño(self, enemigo):
        return self.inteligencia * self.arma_sagrada - enemigo.defensa

# Instancias fuera de las clases
perosonaje_1 = Personaje("Inuyasha", 10, 8, 7, 100)
perosonaje_2 = Sacerdote("Kagome", 5, 15, 6, 80, 20)

def combate(jugador1, jugador2):
    turno = 0
    while jugador1.esta_vivo() and jugador2.esta_vivo():
        print("\nTurno", turno)
        print("Accion de:", jugador1.nombre, ":", sep="")
        jugador1.atacar(jugador2)
        print("\nTurno", turno)
        print("Accion de:", jugador2.nombre, ":", sep="")
        jugador2.atacar(jugador1)
        turno = turno + 1
        if jugador1.esta_vivo():
            print("\nHa ganado", jugador1.nombre)
        elif jugador2.esta_vivo():
            print("\nHa ganado", jugador2.nombre)
        else:
            print("\nEmpate")
        
combate(perosonaje_1, perosonaje_2)




