from modules import EmpDomestica as emp

class Diarista(emp.EmpDomestica):

    def __init__(self, nome, tel, valorPorDia, diasTrabalhados):
        super().__init__(nome, tel)
        self._valorPorDia = valorPorDia
        self._diasTrabalhados = diasTrabalhados
    
    def getSalario(self, valor, dias):
        return valor * dias