r1 = int(input('Digite a medida do primeiro lado:'))
r2 = int(input('Digite a medida do segundo lado:'))
r3 = int(input('Digite a medida do terceiro lado:'))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos acima podem formar um triangulo!')
else:
    print('Os segmentos acima NÃO podem formar um triangulo')
