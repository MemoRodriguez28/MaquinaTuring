class Cinta:
    simbolo_enblanco = " "
    def __init__(self, cadena_cinta = ""):
        self.cinta = dict((enumerate(cadena_cinta)))
    
    def cadena(self):
        cadena = ""
        indice_min = min(self.cinta.keys())
        indice_max = max(self.cinta.keys())
        for i in range(indice_min, indice_max):
            cadena += self.cinta[i]
        return cadena

    def __getitem__(self, indice):
        if indice in self.cinta:
            return self.cinta[indice]
    
    def __setitem__(self, pos, car):
        self.cinta[pos] = car

class MT:
    def __init__(self, cinta ="", simbolo_enblanco = " ", q0 = "", qfinales = None, funcionTransicion = None):
        self.cinta = Cinta(cinta)
        self.posCabeza = 0
        self.simbolo_enblanco = simbolo_enblanco
        self.estadoActual = q0
        
        if qfinales == None:
            self.qfinales = set()
        else:
            self.qfinales = set(qfinales)
        
        if funcionTransicion == None:
            self.funcionTransacion = dict()
        else:
            self.funcionTransacion = funcionTransicion
    
    def getCinta(self):
        return self.cinta.cadena()
    
    def step(self):
        #Leer => escribir => mover
        carDebajoCabeza = self.cinta[self.posCabeza] #Leer
        # t(estado, simbolo/car) = (car, pos, estado)
        # t(q0, 0 ) = (1, R, q0)
        # t(q0, 1 ) = (0, R, q0)
        # t(q0, _ ) = (_, _, qf)
        x = (self.estadoActual, carDebajoCabeza) #(q0, 1)
        
        if x in self.funcionTransacion:
            y = self.funcionTransacion[x]
            self.cinta[self.posCabeza] = y[0] #Escribir
            
            #Mover
            if y[1] == 'R':
                self.posCabeza += 1 #self.posCabeza = self.posCabeza + 1
            elif y[1] == 'L':
                self.posCabeza -= 1 #self.posCabeza = self.posCabeza - 1
            
            #Pasar al siguiente estado
            self.estadoActual = y[2]
            
            
    def final(self):
        if self.estadoActual in self.qfinales: #Si es el estado final aqui termina
            return True
        else: 
            return False
