from modules import EmpDomestica as emp

class Horista(emp.EmpDomestica):

    def __init__(self, nome, tel, valorPorHora, horasTrabalhadas):
        super().__init__(nome, tel)
        self._valorPorHora = valorPorHora
        self._horasTrabalhadas = horasTrabalhadas

    def getSalario(self, valor, horas):
        return valor * horas