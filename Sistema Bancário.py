from datetime import datetime
import pytz


def data_hora_operacao():
    fuso_br = pytz.timezone('Brazil/East')
    horario_br = datetime.now(fuso_br)
    return horario_br.strftime('%d/%m/%Y %H:%M:%S')


saldo = cont = 0
extrato = []
limite = -200
limite_saque_diario = 1

print(f'{" SISTEMA BANCÁRIO V1 ":*^63}')
print()
while True:
    print('Qual operação você deseja realizar?\n'
          '1 - Depósito\n'
          '2 - Saque\n'
          '3 - Extrato\n'
          '4 - Finalizar Operação\n')

    opcao = int(input('Digite a opção: '))
    print('-'*63)
    if opcao == 1:
        deposito = float(input('Digite o valor do depósito: R$'))
        data_hora = data_hora_operacao()
        saldo += deposito
        extrato.append((f'R${deposito:,.2f}', data_hora, f'R${saldo:,.2f}'))
        print('-' * 63)

    if opcao == 2:
        saque = float(input('Digite o valor do saque: R$'))
        if limite_saque_diario <= 3:
            if saldo - saque >= limite:
                data_hora = data_hora_operacao()
                saldo -= saque
                extrato.append((f'R$-{saque}', data_hora, f'R${saldo:,.2f}'))
                limite_saque_diario += 1
            else:
                print(f'Saldo insuficiente. O seu saldo é de R${saldo:,.2f}')
            print('-' * 63)
        else:
            print('Você atingiu o limite de três saques diários.')

    if opcao == 3:
        print(f'{"EXTRATO BANCÁRIO":^63}')
        print(f'{"Valor":^21}|{"Data/Hora":^21}|{"saldo":^21}')
        for c in extrato:
            for v in c:
                cont += 1
                print(f'{v:^21}', end=f'{"|" if cont < 3 else ""}')
            cont = 0
            print(end='\n')
        print(f'\n'
              f'Seu saldo é de R${saldo:,.2f}')
        print('-' * 63)

    if opcao == 4:
        print('Operação finaizada com sucesso!!!')
        break

