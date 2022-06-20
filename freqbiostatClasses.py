import math

# dados = '1 3 2 6 4 5 9 7 8 10'
# dados = '69 57 72 54 93 68 72 58 64 62 65 76 60 49 74 59 66 83 70 45 60 81 71 67 63 64 53 73 81 50 67 68 53 75 65 58 80 60 63 53'
# dados = '710 820 890 980 1100 720 820 890 987 1100 799 824 890 990 1102 800 872 900 999 1103 814 872 910 1000 1120 814 879 920 1100 1200'
# dados = '82 111 132 142 167 87 115 136 142 169 90 120 137 144 172 98 122 138 146 179 101 122 138 151 183 104 127 138 154 189 106 129 140 161 201 108 132 141 163 210'
# dados = '10 16.4 21.3 28 13.3 17.5 23 30.1 14 17.7 23 30.3 15 19 25.1 35 15.2 20.1 28 39.9'
# dados = '8 8.2 9.1 9.5 10 10 10 10.1 10.4 10.9 11 11.5 12 12 12 12.1 12.3 12.9 12.9 13 13 13 13 13.1 13.6 13.8 13.8 13.9 13.9 13.9'
dados = '164 140 170 166 180 149 170 167 159 170 166 172 147 162 149 131 160 158 151 180 171 148 148 140 173 158 164 158 160 167'

listaprov = dados.split(' ')
lista = []
for elemento in listaprov:
    lista.append(float(elemento))

lista.sort()
print('ROL: ', lista)
print('')
tototal = len(lista)
print('Total de itens: ', tototal)

amplgeral = lista[-1] - lista[0]
print('')
print('Amplitude total: ', amplgeral)
print('')

valog = f'{math.log10(tototal):.2f}'
cnst = 1 + 3.3 * float(valog)
if cnst.__round__() < cnst:
	cnst = cnst.__round__() + 0.6
cnst = cnst.__round__()
print('Regra de Sturges: ', cnst)
print('')
amplitude = amplgeral / cnst
if amplitude.__round__() < amplitude:
	amplitude = amplitude.__round__() + 0.6
amplitude = amplitude.__round__()
print('Amplitude: ', amplitude)
print('')

lista2 = []
lista2.append(lista[0])
itemtemp = 0

for item in lista:
	lista2.append(lista2[-1] + amplitude)
	if lista2[-1] >= lista[-1]:
		break
		
lista3 = []
distemp = 'z'
for dist in lista2:
	if distemp != 'z':
		lista3.append([distemp, dist])
		distemp = lista3[-1][-1]
	else:
		distemp = dist

print(f'Classes:\n'
	  f'\t[LI, LS]')
rngcontador = 1
for rng in lista3:
	print(f'{rngcontador}. {rng}')
	rngcontador = rngcontador+1
print('')
print('(LI = Limite Inferior , LS = Limite Superior)')

contador3 = 1
dicio = {}
valordicio = []
for li, ls in lista3:
	for elem in lista:
		if elem == lista[-1]:
			elem = elem - 0.0001
		if elem >= li and elem < ls:
			valordicio.append(elem)
	dicio[str(li)+' |- '+str(ls)] = len(valordicio)
	valordicio = []

print('')
print('--- FREQUENCIA ---')
print('')
for ke, va in dicio.items():
	print(f'[{ke}] = {va}')

print('')
print('--- FREQUENCIA RELATIVA ---')
print('')
for ke2, va2 in dicio.items():
	va2 = va2 / len(lista) * 100
	print(f'[{ke2}] = {va2:.2f}%')
print('')
print('--- FREQUENCIA ACUMULADA ---')
print('')
acurelativo = 0
for ke3, va3 in dicio.items():
	va3 = va3 / len(lista) * 100
	acurelativo = acurelativo + float(f'{va3:.0f}')
	if acurelativo > 100:
		acurelativo = 100
	print(f'[{ke3}] = {acurelativo:.0f}%')