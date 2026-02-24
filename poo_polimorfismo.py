class Cafe():
    def que_soy(self):
        print("Soy un café")

class Te():
    def que_soy(self):
        print("Soy un té")
    
    def definicion_bebida(self, bebida): 
        bebida.que_soy()


mi_cafe = Cafe()
mi_te = Te()
mi_te.definicion_bebida(mi_te)  #
