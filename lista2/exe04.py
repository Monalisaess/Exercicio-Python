#Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples
#e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que
#nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.
not1= float(input("Nota da primeira prova: "))
not2= float(input("Nota da segunda prova: "))
med= (not1+not2)/2
if med > 6:
    print("Sua média é", med, ", parabéns você passou!")
else: 
    print("Não foi dessa vez, sua média é", med, ", estude mais!")