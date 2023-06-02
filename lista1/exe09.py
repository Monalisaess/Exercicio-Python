#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, utilizando as seguintes fórmulas:
#1. Para homens: (72.7*h) - 58
#2. Para mulheres: (62.1*h) - 44.7
alt=float(input("Qual sua altura? "))
gen=str(input("Homem ou Mulher? "))
cont1= (72.7*alt) - 58
cont2= (62.1*alt) - 44.7
if gen == 'Homem':
 print("Seu peso ideal é:", cont1)
elif gen == 'Mulher':
 print("Seu peso ideal é:", cont2)