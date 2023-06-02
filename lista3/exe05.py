#Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), personalizado
#com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo.
amigos = ["Dominique", "Matheus", "Julliano", "Wesley"]
for amigo in amigos:
    saudacao = f"Olá, {amigo}! Como vai você?"
    print(saudacao)
