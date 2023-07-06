from estrutura_elementar import estrutura_elementar



class No:
    def __init__(self, valor):
        self.fila()
        self.fila_prio()
        self.valor = valor
        self.proximo = None

    def set_proximo(self, no):
        self.proximo = no

    def get_proximo(self):
        return self.proximo

class fila(estrutura_elementar):
    def __init__(self):
        self.inicio = None
        self.fila = estrutura_elementar()
        self.fila_pri= estrutura_elementar()

    def enfila (self , n):
        if n >= 60:
            if self.fila_pri.inicio is None:
                self.fila_pri.inicio = No(n)
            else:
                novoNo = No(n)
                aux = self.fila_pri.inicio
                while aux.get_proximo() is not None:
                    aux = aux.get_proximo()
                aux.set_proximo(novoNo)
        
        else:
            if self.fila.inicio is None:
                self.fila.inicio = No(n)
            else:
                novoNo = No(n)
                aux = self.fila.inicio
                while aux.get_proximo() is not None:
                    aux = aux.get_proximo()
                aux.set_proximo(novoNo)            


    def desenfila(self) -> int :
        if self.fila_pri.inicio is not None:
            self.fila_pri.inicio = self.fila_pri.inicio.get_proximo()

        else:   
            if self.fila.inicio is not None:           
                self.fila.inicio = self.fila.inicio.get_proximo()


    def search (self , n):
        if self.inicio == None:
            return False
        
        elif self.inicio.valor == n:
            return True
        
        else:
            aux = self.inicio
            while aux.get_proximo() is not None:
                if aux.get_proximo().valor == n:
                    return True
                else:
                    aux= aux.get_proximo()
                
        return False
