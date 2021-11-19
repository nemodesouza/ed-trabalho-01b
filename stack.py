from element import Element

class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0


    @property
    def top(self):
        return self.__top
    
    @top.setter
    def top(self, top):
        self.__top = top

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size):
        self.__size = size
    

    #Insere elemento na pilha
    def push(self, element):
        elem = Element(element)
        elem.prev = self.top
        self.top = elem
        self.size += 1


    #Remove o elemento do topo da pilha
    def pop(self):
        if self.size > 0:
            elem = self.top
            self.top = self.top.prev
            self.size -= 1

            return elem.data
        
        raise IndexError("A pilha está vazia!")



    #Retorna o topo da pilha
    def peek (self):
        if self.size > 0:                        
            return self.top.data
        
        raise IndexError("A pilha está vazia!")

    #Retorna o tamanho da pilha
    def __len__(self):
        return self.size

    #Representação da pilha
    def __repr__(self):
        repr = ""
        pointer = self.top
        while(pointer):
            repr = repr + str(pointer.data) + "\n"
            pointer = pointer.prev
        
        return repr

    #Representação em string
    def __str__(self):
        return self.__repr__()


################################################################
#
#Área de testes
#
# ##############################################################


if __name__ == "__main__":

    print (">>> Criação da pilha")
    pilha = Stack()
    print (">>> Criação OK")
    print ("")
    print ("")

    print (">>> Tamanho da pilha")
    len(pilha)
    print (">>> OK")
    print ("")
    print ("")

    print (">>> Print da pilha...")
    print(pilha)
    print (">>> Print OK")
    print ("")
    print ("")

    print (">>> Inserindo o valor 7...")
    pilha.push(7)
    print (">>> Inserido!")
    print ("")
    print ("")

    print (">>> Inserindo o float 3.4...")
    pilha.push(3.4)
    print (">>> Inserido!")
    print ("")
    print ("")

    print (">>> Inserindo o booleano False...")
    pilha.push(False)
    print (">>> Inserido!")
    print ("")
    print ("")

    print (">>> Inserindo o valor 1994...")
    pilha.push(1994)
    print (">>> Inserido!")
    print ("")
    print ("")

    print (">>> Inserindo str Topo...")
    pilha.push("Topo")
    print (">>> Inserido!")
    print ("")
    print ("")

    print (">>> Print da pilha...")
    print(pilha)
    print (">>> Print OK")
    print ("")
    print ("")

    print (">>> Espiar o Topo...")
    print(pilha.peek())
    print (">>> OK!")
    print ("")
    print ("")

    print (">>> Removendo elemento...")
    print(pilha.pop())
    print (">>> Removido!")
    print ("")
    print ("")

    print (">>> Removendo elemento...")
    print(pilha.pop())
    print (">>> Removido!")
    print ("")
    print ("")

    print (">>> Removendo elemento...")
    print(pilha.pop())
    print (">>> Removido!")
    print ("")
    print ("")

    print (">>> Espiar o Topo...")
    print(pilha.peek())
    print (">>> OK!")
    print ("")
    print ("")

    print (">>> Removendo elemento...")
    print(pilha.pop())
    print (">>> Removido!")
    print ("")
    print ("")

    print (">>> Removendo elemento...")
    print(pilha.pop())
    print (">>> Removido!")
    print ("")
    print ("")

    #Dispara o erro
    print (">>> Removendo elemento...")
    pilha.pop()    
    print ("")
    print ("")

    #Não funciona daqui pra frente, por causa do erro
    print (">>> Inserindo str Navegador...")
    pilha.push("Navegador")
    print (">>> Inserido!")
    print ("")
    print ("")

    print (">>> Inserindo valor 1984...")
    pilha.push(1984)
    print (">>> Inserido!")
    print ("")
    print ("")

    print (">>> Espiar o Topo...")
    print(pilha.peek())
    print (">>> OK!")
    print ("")
    print ("")

    print (">>> Print da pilha...")
    print(pilha)
    print (">>> Print OK")
    print ("")
    print ("")