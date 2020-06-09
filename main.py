from modules import Horista as h
from modules import Diarista as d
from modules import Mensalista as m

nome = input("\nDigite o nome da horista: " )
telefone = input("Digite o telefone da horista: " )
horista = h.Horista(nome, telefone, 10, 160)

nome = input("\nDigite o nome da diarista: " )
telefone = input("Digite o telefone da diarista: " )
diarista = d.Diarista(nome, telefone, 20, 55)

nome = input("\nDigite o nome da mensalista: " )
telefone = input("Digite o telefone da mensalista: " )
mensalista = m.Mensalista(nome, telefone, 1000)

print("\n------------------------------------")

salarioHorista = horista.getSalario(horista._valorPorHora, horista._horasTrabalhadas)
print("Dados da Horista:\n Nome: {}\n Telefone: {}\n Salário: {}".format(horista._nome, horista._telefone, salarioHorista))

salarioDiarista = diarista.getSalario(diarista._valorPorDia, diarista._diasTrabalhados)
print("\nDados da Diarista:\n Nome: {}\n Telefone: {}\n Salário: {}".format(diarista._nome, diarista._telefone, salarioDiarista))

salarioMensalista = mensalista.getSalario()
print("\nDados da Mensalista:\n Nome: {}\n Telefone: {}\n Salário: {}".format(mensalista._nome, mensalista._telefone, salarioMensalista))

print("\n------------------------------------")

menor = salarioHorista
if (salarioDiarista < menor):
    menor = salarioDiarista
if (salarioMensalista < menor):
    menor = salarioMensalista

print("A doméstica mais barata para a república é a: \n")
if (menor == salarioHorista):
    print(" Nome: {}\n Telefone: {}\n Salário: {}".format(horista._nome, horista._telefone, salarioHorista))
elif (menor == salarioDiarista):
    print(" Nome: {}\n Telefone: {}\n Salário: {}".format(diarista._nome, diarista._telefone, salarioDiarista))
else:
    print(" Nome: {}\n Telefone: {}\n Salário: {}".format(mensalista._nome, mensalista._telefone, salarioMensalista))

print("\n")
