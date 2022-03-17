class ciudades:
    def __init__(self,ciudad,nombre,nombretrabajador,edificios):
        self.ciudades = ciudad
        self.empresas=self.empresa(nombre,nombretrabajador,edificios)
        
    class empresa:
        def __init__(self,nombre,nombretrabajador,edificios):
            self.nombrempresa=nombre
            self.trabajador=[self.empleados(nombretrabajador)]
            self.edificios=[self.edificio(edificios)]
             
        class empleados:
            def __init__(self,nombre):
                self.nombre=nombre
                
        class edificio:
            def __init__(self,nombredificio):
                self.edificio=nombredificio
        

def destruir_ciduad(destruir, lista_ciudades):
    for i in range(len(lista_ciudades)):
        if destruir == lista_ciudades[i].nombre:
            del lista_ciudades[i]
        
listaCuidades = [ciudades("NY", "Yahoo", "Pepe", "Edificio A"), ciudades("LA", "Google", "Ramon", "Edificio B")]