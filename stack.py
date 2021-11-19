from element import Element

class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0


    #Insere elemento na pilha
    def push(self, element):
        elem = Element(element)
        elem.__prev = self.__top
        self.__top = elem
        self.__size += 1


    #Remove o elemento do topo da pilha
    def pop(self):
        elem = self.__top
        self.__top = self.__top.__prev
        return elem


    #Retorna o topo da pilha
    def peek (self):
        pass

    #Retorna o tamanho da pilha
    def __len__(self):
        return self.__size

    #Representação da pilha
    def __repr__(self):
        repr = ""
        pointer = self.__top
        while(pointer):
            repr = repr + str(pointer.data) + "\n"
            pointer = pointer.__prev
        
        return repr

    #Representação em string
    def __str__(self):
        return self.__repr__()


    
