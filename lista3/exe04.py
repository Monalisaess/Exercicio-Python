#Faça um programa que receba um número e que calcule e mostre a tabuada desse número..
numero = int(input("Digite um número: "))
print("Tabuada do", numero)
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
