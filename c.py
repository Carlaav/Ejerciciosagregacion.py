class Casa:
    def __init__(self, lista_paredes):
        self.paredes = lista_paredes
    
    
    def superfiiceDeParedesMenosCristal(self):
        suma = 0
        for pared in self.paredes:
            suma = suma + pared.dimension
        
        suma = suma - self.superficieAcristalada()
        return suma
    
    def superficieAcristalada(self):
        superficie = 0
        for pared in self.paredes:
            superficie = superficie + pared.superficieCristal()
        
        return superficie
    
    
class Pared:
    def __init__(self, orientacion, dimension):
        self.orientacion = orientacion
        self.dimension = dimension
        self.ventanas = []
        
    def superficieCristal(self):
        superficie = 0
        for ventana in self.ventanas:
            superficie = superficie + ventana.dimen
        
        return superficie
                
        

class Ventana:
    def __init__(self, pared, ven_dim, proteccion):
        self.pared = pared
        self.dimen = ven_dim
        
        self.pared.ventanas.append(self)
        
        if proteccion is None:
            raise Exception("Campo de proteccion obligatorio")
        else:
            self.proteccion = proteccion
        
class Proteccion:
    def __init__(self, proteccion):
        self.proteccion = proteccion
            
            

pared_norte = Pared("NORTE", 60)
pared_oeste = Pared("OESTEE", 80)
pared_sur = Pared("SUR", 20)
pared_este = Pared("ESTE", 70)
ventana_norte = Ventana(pared_norte, 0.5, "persiana")
ventana_oeste = Ventana(pared_oeste, 1, "persiana")
ventana_sur = Ventana(pared_sur, 2, "estor veneciano")
ventana_este = Ventana(pared_este, 1, "persiana")
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
print(casa.superficieAcristalada())
print(casa.superfiiceDeParedesMenosCristal())
