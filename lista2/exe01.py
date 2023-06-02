#Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou
#menor que 10. O programa deve escrever a mensagem correspondente (maior ou
#menor) e informar o valor digitado pelo usuário.
num=float(input("Digite um número: "))
if num >=  10:
    print("O número", num, "é maior que dez.")
else:
    print("O número", num, " é menor que dez.")