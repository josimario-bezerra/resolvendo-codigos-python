# Vamos testar se uma palavra é um palíndromo.

#Solicitar palavra
palavra = input("Digite uma palavra: ").strip().lower()

#Invertendo a palavra usando slincing [::-1]
invertida = palavra[::-1]

#Verificando se a palavra é um palíndromo
if palavra == invertida:
    print(f"A palavra {palavra} é um palíndromo.")

else:
    print(f"A palavra {palavra} não é um palíndromo.")    