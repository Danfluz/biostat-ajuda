acumulado = 0
v1 = 'xcv1'
v2 = 'xcv2'
v3 = 'xcv3'
v4 = 'xcv4'
v5 = 'xcv5'
v6 = 'xcv6'
v7 = 'xcv7'
v8 = 'xcv8'
v9 = 'xcv9'
v10 = 'xcv10'

varvalidas = []

def freq(variavel):
	return len(variavel)
	
def freq_rt(variavel, total):
	return (len(variavel) / total) * 100

def freq_acu(variavel, freqsanteriores):
	global acumulado
	acumulado = variavel + acumulado
	return acumulado

while True:
	try:
		n_var = int(input('Quantos tipos de variáveis diferentes existem?\nResposta: '))
	except ValueError:
		print('ERRO: Este campo aceita apenas números')
	else:
		break

contador = 1

while contador != n_var +1:
	if contador == 1:
		v1 = input(f'Digite o dado {contador}: ')
	if contador == 2:
		v2 = input(f'Digite o dado {contador}: ')
	if contador == 3:
		v3 = input(f'Digite o dado {contador}: ')
	if contador == 4:
		v4 = input(f'Digite o dado {contador}: ')
	if contador == 5:
		v5 = input(f'Digite o dado {contador}: ')
	if contador == 6:
		v6 = input(f'Digite o dado {contador}: ')
	if contador == 7:
		v7 = input(f'Digite o dado {contador}: ')
	if contador == 8:
		v8 = input(f'Digite o dado {contador}: ')
	if contador == 9:
		v9 = input(f'Digite o dado {contador}: ')
	if contador == 10:
		v10 = input(f'Digite o dado {contador}: ')
	
	contador = contador +1

if v1.isdigit():
	ordenar = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]
	ordenar.sort()
	v1 = ordenar[0]
	v2 = ordenar[1]
	v3 = ordenar[2]
	v4 = ordenar[3]
	v5 = ordenar[4]
	v6 = ordenar[5]
	v7 = ordenar[6]
	v8 = ordenar[7]
	v9 = ordenar[8]
	v10 = ordenar[9]

dados_brutos = input('Digite ou cole os dados brutos separados por espaços:\n  ')

listav1 = []
listav2 = []
listav3 = []
listav4 = []
listav5 = []
listav6 = []
listav7 = []
listav8 = []
listav9 = []
listav10 = []

vtodas = [listav1, listav2, listav3, listav4, listav5, listav6, listav7, listav8, listav9, listav10]

dadotemp = ''
for parte in dados_brutos:
	if parte != ' ':
		dadotemp = dadotemp + parte
	if dadotemp == v1:
		listav1.append(dadotemp)
		dadotemp = ''
	if dadotemp == v2:
		listav2.append(dadotemp)
		dadotemp = ''
	if dadotemp == v3:
		listav3.append(dadotemp)
		dadotemp = ''
	if dadotemp == v4:
		listav4.append(dadotemp)
		dadotemp = ''
	if dadotemp == v5:
		listav5.append(dadotemp)
		dadotemp = ''
	if dadotemp == v6:
		listav6.append(dadotemp)
		dadotemp = ''
	if dadotemp == v7:
		listav7.append(dadotemp)
		dadotemp = ''
	if dadotemp == v8:
		listav8.append(dadotemp)
		dadotemp = ''
	if dadotemp == v9:
		listav9.append(dadotemp)
		dadotemp = ''
	if dadotemp == v10:
		listav10.append(dadotemp)
		dadotemp = ''

	else:
		pass

vtot = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]

for padr in vtot:
	if 'xcv' in padr:
		pass
	else:
		varvalidas.append(padr)

print('')

n_total = len(listav1)+len(listav2)+len(listav3)+len(listav4)+len(listav5)+len(listav6)+len(listav7)+len(listav8)+len(listav9)+len(listav10)

print('--- FREQUENCIA ---')
print('')
for frequencia in vtodas:
	if freq(frequencia) <= 0:
		pass
	else:
		print(f'{frequencia[0]}: {freq(frequencia)}')
print('Total: ',n_total)
print('')

print('--- FREQUENCIA RELATIVA ---')
print('')
for frequencia in vtodas:
	if freq_rt(frequencia, n_total) <= 0:
		pass
	else:
		print(f'{frequencia[0]}: {freq_rt(frequencia, n_total)}')
print('Total: ', ((n_total / n_total) * 100))
print('')

print('--- FREQUENCIA ACUMULADA ---')
print('')
for frequencia in vtodas:
	jumbo = freq_acu(freq_rt(frequencia,n_total), acumulado)
	if jumbo <= 100.9:
		print(f'{frequencia[0]}: {jumbo}')
		if jumbo >= 99.99:
			acumulado = 0
			break
	else:
		pass
