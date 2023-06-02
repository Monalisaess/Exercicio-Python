#As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se
#forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
#compradas, calcule e escreva o custo total da compra.
mac= int(input("Quantas maçãs comprou? "))
cont1= (mac*1.30)
cont2= (mac*1.0)
if mac < 12:
    print("Sua compra deu {:.2f}".format(cont1))
else:
    print("Sua compra deu {:.2f}".format(cont2))