# Calculadora Simples
num1 = 0
num2 = 0
resultado = 0
operaçao = 0

# Introdução
print('>Bem vindo a calculadora!<')
num1 = int(input('Por favor, Digite o primeiro número: '))
num2 = int(input('Por favor, Digite o segundo número: '))
operaçao = input('Selecione a operação: ')

# Colocando Operações
if operaçao == '+':
    resultado = num1 + num2
elif operaçao == '-':
    resultado = num1 - num2
elif operaçao == '*':
    resultado = num1 * num2
elif operaçao == '/':
    resultado = num1 / num2
else:
    resultado == 'Operação invalida'

# Resultado
print(str(num1) + '' + str(operaçao) + '' + str(num2) + '=' + str(resultado))
