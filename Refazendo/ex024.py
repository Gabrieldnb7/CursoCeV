cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(f'A sua cidade começa com Santo? {cidade.upper()[:5] == "SANTO"}')