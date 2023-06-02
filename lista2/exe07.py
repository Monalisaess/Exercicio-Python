#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
#calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também
#testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
#senão escrever a mensagem 'Saldo Negativo'.
numero_conta = int(input("Digite o número da conta do cliente: "))
saldo = float(input("Digite o saldo da conta: "))
debito = float(input("Digite o débito da conta: "))
credito = float(input("Digite o crédito da conta: "))
saldo_atual = saldo - debito + credito
if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")

