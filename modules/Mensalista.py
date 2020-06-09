from modules import EmpDomestica as emp

class Mensalista(emp.EmpDomestica):

    def __init__(self, nome, tel, valorMensal):
        super().__init__(nome, tel)
        self._valorMensal = valorMensal

    def getSalario(self):
        return self._valorMensal