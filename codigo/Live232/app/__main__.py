from .app import converte_C_para_F, converte_F_para_C


opcao = input(
    'Digite F para Fahrenheit\n'
    'Digite C para Celsius: '
)

temperatura = float(input('Forneça a temperatura: '))

match (opcao):
    case 'F':
        resultado = converte_C_para_F(temperatura)
        print(f'A temperatura convertida é: {resultado}')
    case 'C':
        resultado = converte_F_para_C(temperatura)
        print(f'A temperatura convertida é: {resultado}')
    case _:
        print('Digite F ou C. Tá errado!!!!')
