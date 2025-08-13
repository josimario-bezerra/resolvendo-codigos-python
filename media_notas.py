#Agora vamos calcular a média de três notas fornecidas na entrada do usuário.

#Solicitando notas
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

#Calculando a média
media = nota1 + nota2 + nota3 / 3

#Exibir o resultado
print(f"A média é: {media}.")