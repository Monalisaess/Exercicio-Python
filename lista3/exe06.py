#Seja criativo ao desenvolver este programa.
#a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
#b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome
#personalizado.
#c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos
#convites. Imprima o nome das pessoas que não poderão comparecer.
#d. Modifique sua lista, substitua os desistentes por novos convidados.
#e. Exiba um novo convite para cada pessoa que continua presente em sua lista.
convidados = ["Doja Cat", "Melanie Martinez", "Kali Uchis", "Hirai Momo", "Abel Tesfaye"]

enviados = []
mensagem = "Olá, {nome}! Você está convidado(a) para um jantar em minha casa. Será uma noite incrível! Espero vê-lo(a) lá."

for convidado in convidados:
    convite = mensagem.format(nome=convidado)
    enviados.append(convite)
    print("Convite enviado para:", convidado)

desistente = "Doja Cat"

convidados.remove(desistente)
print("Infelizmente,", desistente, "não poderá comparecer ao jantar.")

novos = ["Lily Collins", "Zendaya"]

convidados.extend(novos)

print("\nConvites para os convidados restantes:")
for convidado in convidados:
    if convidado not in novos:
        print(enviados[convidados.index(convidado)])
