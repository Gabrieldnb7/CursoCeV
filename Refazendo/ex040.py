n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1+n2)/2
if média < 5.0:
    print(f'Sua média foi {média:.1f} e você está REPROVADO.')
elif 5.0 <= média < 7.0:
    print(f'Sua média foi {média:.1f} e você está de RECUPERAÇÃO.')
elif média >= 7.0:
    print(f'Sua média foi {média:.1f} e você está APROVADO.')
