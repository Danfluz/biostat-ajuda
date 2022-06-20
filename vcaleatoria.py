possibilidades = int(input('Quantas possibilidades diferentes existem?\nResposta: '))
numdict = {}

for i in range(possibilidades):
    c = input(f'Valor da possibilidade {i+1}: ')
    if c[0].isdigit():
        c = int(c[0]) * c[1]
    else:
        cc = c
    numdict[str(i+1)] = c

total_c = ''.join(list(numdict.values())).count(cc)
if cc.isalpha():
    cc = 1 #cuidado pode causar erros
constante = float(cc) / float(total_c)
constanteimpressa = f'{c} = {float(cc)}/{float(total_c)}'

valportemp = ''
listavalpor = []
for valpor in numdict.values():
    if valportemp != '':
        valportemp = valpor.count(c) + valportemp
        listavalpor.append(valportemp)
    else:
        valportemp = valpor.count(c)
        listavalpor.append(valportemp)

print('')
print(' + '.join(numdict.values()), '= 1')
print(constanteimpressa)
print(constante)
print('')
print('Distribuição acumulada:')
for num in listavalpor:
    print(f'F(x) = {num}/{total_c}')
