from funcoes_cpf import *

while True:
    print(30*'=')
    print('VERIFICADOR/GERADOR DE CPF'.center(30))
    print(30*'=')
    print('selecione uma das opçoes abaixo:')
    print('[ 1 ] Verificar cpf.')
    print('[ 2 ] Gerar cpf aleatório.')
    print('[ 3 ] Sair')

    print()
    opcao = input('Sua opçao:')
    print()

    if opcao == '1':
        cpf=input('Digite o CPF a ser validado:')
        validar_cpf(cpf)
        
    elif opcao == '2':
        gerar_cpf()
        print()

    elif opcao == '3':
        print('Saindo do programa...')
        break

    else:
        print('opçao inválida.')
print()