from CursoEmVideo.PythonTestes.Úteis import Números

# Programa Principal
num = int(input('Digite um número: '))
fat = Números.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {Números.dobro(num)}')
