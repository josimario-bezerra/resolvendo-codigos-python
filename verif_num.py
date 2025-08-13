#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.

#Solicitar o número
num = int(input('Digite o número: '))

#Verificar se o número é ímpar ou par
if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")