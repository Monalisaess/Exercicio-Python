#Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até
#agora.
# Lista para armazenar os usuários cadastrados
usuarios = []

# Loop para cadastrar usuários
while True:
    # Solicita os dados do usuário
    nome = input("Digite o nome do usuário (ou 'sair' para encerrar): ")
    
    # Verifica se o usuário deseja sair do cadastro
    if nome.lower() == "sair":
        break
    
    idade = input("Digite a idade do usuário: ")
    email = input("Digite o email do usuário: ")
    
    # Cria um dicionário com os dados do usuário
    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }
    
    # Adiciona o usuário à lista de usuários cadastrados
    usuarios.append(usuario)
    
# Exibe os usuários cadastrados
print("\nUsuários cadastrados:")
for usuario in usuarios:
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Email: {usuario['email']}")
    print("-" * 20)
