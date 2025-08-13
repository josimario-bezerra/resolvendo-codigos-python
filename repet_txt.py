#Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

#Solicitar uma frase ou palavra
texto = input("Digite uma palavra ou uma frase: ")

#Solicitar um número
num = int(input("Digite um número inteiro: "))

#Repete a string de acordo com o número digitado
resultado = (texto + ', ') * num

#Exibir a string

print("O resultado é:", resultado)

