#Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganho= float(input("Quanto você ganha por hora? "))
horas= float(input("Quantas horas trabalhou este mês? "))
conta= ganho*horas
print("Você ganhou ", conta, "esse mês")