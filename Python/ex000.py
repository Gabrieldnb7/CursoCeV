nome = str(input('Digite o seu primeiro nome: '))
separado = nome.split()
if len(separado[0]) <= 4:
    print(f'{nome} Seu nome tem {len(separado[0])} e é um nome curto')
if len(separado[0]) == 5 or len(separado[0]) == 6:
    print(f'{nome} seu nome tem {len(separado[0])} letras, o tamanho normal')
if len(separado[0]) > 6:
    print(f'{nome} seu nome é tem {len(separado[0])} letras e é um nome grande')