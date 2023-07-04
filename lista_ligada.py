from estrutura_elementar import estrutura_elementar


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def set_proximo(self, no):
        self.proximo = no

    def get_proximo(self):
        return self.proximo


class LinkedList(estrutura_elementar):
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            novoNo.set_proximo(self.inicio)
            self.inicio = novoNo

    def inserir_fim(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            aux = self.inicio
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
            aux.set_proximo(novoNo)

    def esta_vazio(self) -> bool:
        if self.inicio is not None:
            return False
        else:
            return True

    def remove(self, item):
        if self.inicio == None:
            return None
        
        elif self.inicio.valor == item:
            self.inicio = self.inicio.get_proximo()

        else:
            aux = self.inicio
            
            while aux.get_proximo() is not None:
                if aux.get_proximo().valor == item:
                    aux.set_proximo(aux.get_proximo().get_proximo())
                
                else:    
                    aux = aux.get_proximo()
                


    def tamanho(self) -> int:
        if self.inicio is None:
            return 0
        else: 
            cont=1
            aux = self.inicio
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
                cont+=1
            return cont

    def limpa(self):
        self.inicio = None

    def procura(self, item) -> bool:
        
        if self.inicio == None:
            return False
        
        elif self.inicio.valor == item:
            return True
        
        else:
            aux = self.inicio
            while aux.get_proximo() is not None:
                if aux.get_proximo().valor == item:
                    return True
                else:
                    aux= aux.get_proximo()
                
        return False

    def indice_de(self, item):
        if self.inicio == None:
            return -1
        
        elif self.inicio.valor== item:
            return 0
        
        else:
            aux = self.inicio
            cont = 1
            while aux.get_proximo() is not None:
                if aux.get_proximo().valor == item:
                    return cont
                else:
                    aux = aux.get_proximo()
                    cont += 1

            return -1

    def recupera_indice(self, index):
        if self.inicio == None:
            return None
        elif index == 0:
            return self.inicio.valor
        else:
            aux = self.inicio
            cont = 0
            while aux is not None:
                if cont == index:
                    return aux.valor
                cont += 1
                aux = aux.get_proximo()
            
            return None