from math import hypot
catetoad = float(input('Digite o valor do cateto adjacente: '))
catetoop = float(input('Digite o valor do cateto oposto: '))
hipotenusa = hypot(catetoad, catetoop)
# OU usar a fórmula
# hipotenusa = (catetoop**2 + catetoad**2) ** (0.5) -> raiz quadrada dos catetos elevados ao quadrado
print(f'Possuindo {catetoop} e {catetoad} como catetos, a hipotenusa é {hipotenusa:.2f}')
