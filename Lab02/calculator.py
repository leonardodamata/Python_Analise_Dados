## Calculadora em Python

print('**************************** Python Calculator ****************************\n')

print('Selecione o número da operação desejada:\n')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão\n')

opcao = input('Digite sua opção:(1/2/3/4):')
sinal = '0'
teste = '0'
total = 0
while  teste == '0':
    if opcao > '4':
        print('\nOpção inválida! \n')
        opcao = input('Digite sua opção:(1/2/3/4):')
    else:
        teste = '1'

primeiroNumero = input('\nDigite o primeiro número: ')

segundoNumero = input('\nDigite o segundo número:')

mensagem = '0'

if opcao == '1':
    sinal = '+'
    total = int(primeiroNumero) + int(segundoNumero)
elif opcao == '2':
    sinal = '-'
    total = int(primeiroNumero) - int(segundoNumero)
elif opcao == '3':
    sinal = '*'
    total = int(primeiroNumero) * int(segundoNumero)
elif opcao == '4':
    sinal = '/'
    total = int(primeiroNumero) / int(segundoNumero)

mensagem = '\nO resultado de '+ primeiroNumero+ ' ' + sinal+ ' ' + segundoNumero+ ' = ' + str(total)

print(mensagem)
