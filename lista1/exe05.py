#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre
#a temperatura em graus Celsius.
#1. C = 5 * ((F-32) / 9).
f= float(input("Qual a temperatura em Fahrenheit? "))
conta= 5 * ((f-32) / 9)
print("Em Celsius são", conta, "°C")