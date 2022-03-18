class Casa:
    def __init__(self, lista_paredes):
        self.paredes = lista_paredes
    
    
    
    def dimensionesCasa(self):
        dimension = 0
        for pared in self.paredes:
            dimension = dimension + pared.dimension - pared.ventana.dimen
        
        return dimension
    
    
class Pared:
    def __init__(self, orientacion, dimension, dim_ventana):
        self.orientacion = orientacion
        self.dimension = dimension
        self.ventana = Ventana(self, dim_ventana)
        

class Ventana:
    def __init__(self, pared, ven_dim):
        self.pared = pared
        self.dimen = ven_dim
            
            

pared_norte = Pared("NORTE", 100, 0.5) 
pared_oeste = Pared("OESTE", 60, 1) 
pared_sur = Pared("SUR", 70, 2) 
pared_este = Pared("ESTE", 30, 1) 
    


casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
print(casa.dimensionesCasa())
