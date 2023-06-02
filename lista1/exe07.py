#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#1. o produto do dobro do primeiro com metade do segundo .
#2. a soma do triplo do primeiro com o terceiro.
#3. o terceiro elevado ao cubo.
num1= int(input("Digite seu número inteiro: ")) 
num2= int(input("Digite outro número inteiro: "))
num3= int(input("Digite um número real: "))
cont1= (num1*2)+(num2/2)
print("produto do dobro do primeiro com metade do segundo", cont1)
cont2= (num1*3)+num3
print("a soma do triplo do primeiro com o terceiro", cont2)
cont3=(num3**3)
print("terceiro elevado ao cubo", cont3)