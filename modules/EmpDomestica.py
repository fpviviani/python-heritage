from abc import ABC, abstractmethod

class EmpDomestica(ABC):

    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone
    
    def getTelefone(self):
        return self._telefone

    def getNome(self):
        return self._nome

    @abstractmethod
    def getSalario(self, classe, valor, dias):
        pass