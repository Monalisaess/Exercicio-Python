#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
#ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
#tabela abaixo:
#Média de Aproveitamento Conceito
#Entre 9.0 e 10.0 A
#Entre 7.5 e 9.0 B
#Entre 6.0 e 7.5 C
#Entre 4.0 e 6.0 D
#Entre 4.0 e zero E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
#mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
#conceito for D ou E.
nota1= float(input("Digite sua primeira nota: "))
nota2= float(input("Digite sua segunda nota: "))
media= (nota1+nota2)/2
if media >= 9:
    print("Nota 1:", nota1)
    print("Nota 2:", nota2) 
    print("Sua média é", media)
    print("Conceito A")
    print("APROVADO!")
elif media >= 7.5:
    print("Nota 1:", nota1)
    print("Nota 2:", nota2) 
    print("Sua média é", media)
    print("Conceito B")
    print("APROVADO!")
elif media >= 6:
    print("Nota 1:", nota1)
    print("Nota 2:", nota2) 
    print("Sua média é", media)
    print("Conceito C")
    print("APROVADO!")
elif media >= 4:
    print("Nota 1:", nota1)
    print("Nota 2:", nota2) 
    print("Sua média é", media)
    print("Conceito D")
    print("REPROVADO!")
else:
    print("Nota 1:", nota1)
    print("Nota 2:", nota2) 
    print("Sua média é", media)
    print("Conceito E")
    print("REPROVADO!")