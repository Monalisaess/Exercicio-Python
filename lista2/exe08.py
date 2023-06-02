#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em
#estoque e quantidade mínima em estoque de um produto. Calcular e escrever a
#quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).
#Se a quantidade em estoque for maior ou igual a quantidade média, escrever a
#mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.
estoque_atual= int(input("Quantidade atual em estoque: "))
maxima= int(input("Quantidade máxima em estoque: "))
minima= int(input("Quantidade mínima em estoque: "))
media = (maxima + minima)/2

if estoque_atual > media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")