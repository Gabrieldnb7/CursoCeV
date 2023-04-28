from math import cos, tan, sin, radians
ângulo = float(input('Digite um ângulo qualquer: '))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
seno = sin(radians(ângulo))
print(f'O ângulo {ângulo} possui como seno {seno:.2f}, cosseno {cosseno:.2f} e tangente {tangente:.2f}')