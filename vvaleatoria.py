def freq_rt(variavel, total):
	return (variavel / total) * 100

barra = False
todos = True
constante = None
valpoor = False

# Descobrir constante
pergconstante = input('A questão pede para descobrir a constante?\nResposta: ')
if pergconstante.upper().startswith('S'):
	possibilidades = int(input('Quantas possibilidades diferentes existem?\nResposta: '))
	numdict = {}

	for i in range(possibilidades):
		c = input(f'Valor da possibilidade {i + 1}: ')
		if '/' in c: # CONVERSOR DE FRAÇÕES
			barra = True
			frac = c.split('/')
			c = str(int(frac[0])/int(frac[1]))
		if c[0].isdigit() and barra is False:
			c = int(c[0]) * c[1]
		else:
			cc = c
		numdict[str(i+1)] = c # Se for usar 1,2,3,4,5...
		# numdict[str(i)] = c # Se for usar 0,1,2,3,4...


	total_c = ''.join(list(numdict.values())).count(cc)
	if cc.isalpha():
		cc = 1  # cuidado pode causar erros
	constante = float(cc) / float(total_c)
	constanteimpressa = f'{c} = {float(cc)}/{float(total_c)}'

	valportemp = ''
	valpoor = True
	listavalpor = []
	for valpor in numdict.values():
		if valportemp != '':
			valportemp = valpor.count(c) + valportemp
			listavalpor.append(valportemp)
		else:
			valportemp = valpor.count(c)
			listavalpor.append(valportemp)

	if barra == False:
		for kno, valu in numdict.items():
			numdict[kno] = len(valu) * constante
	else:
		pass

	numeros = numdict
	print('')
else:

	# Parte principal do programa

	numeros = {     # Valores se a tabela estiver explicita
		# X | p(X=xi)
		'2': '0.05',
		'3': '0.80',
		'4': '0.75',
		'5': '0.2',
		'6': '0.2',
		# '7': '0.1',
	}



pergunta = input('Calcular probabilidade de numero específico?\n(ou deixe em branco para ver os valores de esperança e variância)\nResposta: ')
if pergunta.upper() == 'S' or pergunta.upper() == 'SIM':
	todos = False
	pergunta = input('Calcular maior que X, menor que X, "os dois" ou exatidão?\nResposta: ')
	if pergunta.upper().startswith('MAI') or pergunta == '>':
		x = input('Digite o valor de X: ')
		if ',' in x:
			x = float(x.replace(',', '.'))
		else:
			x = float(x)

	if pergunta.upper().startswith('MEN') or pergunta == '<':
		x = input('Digite o valor de X: ')
		if ',' in x:
			x = float(x.replace(',', '.'))
		else:
			x = float(x)

	if pergunta.upper().startswith('EXA') or pergunta == '=':
		x = input('Digite o valor de X: ')
		if ',' in x:
			x = float(x.replace(',', '.'))
		else:
			x = float(x)

	if pergunta.upper().__contains__('DOIS') or pergunta == '2':
		x2 = 'não'
		y2 = 'não'
		x = input('Maior que: ')
		if x.startswith('<'):
			x2 = 'menor'
			x = x.strip('<')
		y = input('Menor que: ')
		if y.startswith('>'):
			y2 = 'maior'
			y = y.strip('>')
		if ',' in x:
			x = float(x.replace(',', '.'))
		else:
			x = float(x)

		if ',' in y:
			y = float(y.replace(',', '.'))
		else:
			y = float(y)


else:
	pass

esperanca = []
esperanca2 = []
for k, v in numeros.items():
	if todos == True:
		conn = float(k) * float(v)
		esperanca.append(round(conn, 2))
		conn2 = (float(k)**2) * float(v) # depois
		esperanca2.append(conn2) #depois


	if pergunta.upper().startswith('MAI') or pergunta == '>':
		if float(k) > x:
			conn = float(k) * float(v)
			esperanca.append(round(conn, 2))
			conn2 = (float(k) ** 2) * float(v)  # depois
			esperanca2.append(conn2)  # depois

	if pergunta.upper().startswith('MEN') or pergunta == '<':
		if float(k) < x:
			conn = float(k) * float(v)
			esperanca.append(round(conn, 2))
			conn2 = (float(k) ** 2) * float(v)  # depois
			esperanca2.append(conn2)  # depois

	if pergunta.upper().startswith('EXA') or pergunta == '=':
		if float(k) == float(x):
			conn = float(k) * float(v)
			esperanca.append(round(conn, 2))
			conn2 = (float(k) ** 2) * float(v)  # depois
			esperanca2.append(conn2)  # depois

	if pergunta.upper().__contains__('DOIS') or pergunta == '2':
		if x2 == 'menor':
			float(k) < float(x) and float(k) < float(y)
		if y2 == 'maior':
			float(k) > float(x) and float(k) > float(y)
		else:
			if float(k) > float(x) and float(k) < float(y):
				conn = float(k) * float(v)
				esperanca.append(round(conn, 2))
				conn2 = (float(k) ** 2) * float(v)  # depois
				esperanca2.append(conn2)  # depois

calcesp = []
calcesp2 = [] #depois
valespe = []
valespe2 = [] #depois
for ch, va in numeros.items():
	if todos == True:
		chva = f'({float(ch)} x {float(va)})'
		chva2 = f'({float(ch)}² x {float(va)})' #depois
		calcesp.append(chva)
		calcesp2.append(chva2) #depois
	if pergunta.upper().startswith('MAI') or pergunta == '>':
		if float(ch) > x:
			chva = f'P(X = {float(ch)})'
			chva2 = f'P(X = {float(ch)}²)' #depois
			calcesp.append(chva)
			calcesp2.append(chva2) #depois
			valespe.append(float(va))
			valespe2.append(float(va)) #depois
			sinal = '>'
	if pergunta.upper().startswith('MEN') or pergunta == '<':
		if float(ch) < x:
			chva = f'P(X = {float(ch)})'
			chva2 = f'P(X = {float(ch)}²)' #depois
			calcesp.append(chva)
			calcesp2.append(chva2) #depois
			valespe.append(float(va))
			valespe2.append(float(va)) #depois
			sinal = '<'
	if pergunta.upper().startswith('EXA') or pergunta == '=':
		if float(ch) == float(x):
			chva = f'P(X = {float(ch)})'
			chva2 = f'P(X = {float(ch)}²)' #depois
			calcesp.append(chva)
			calcesp2.append(chva2) #depois
			valespe.append(float(va))
			valespe2.append(float(va)) #depois
			sinal = '='
	if pergunta.upper().__contains__('DOIS') or pergunta == '2':
		if float(ch) > float(x) and float(ch) < float(y):
			chva = f'P(X = {float(ch)})'
			chva2 = f'P(X = {float(ch)}²)' #depois
			calcesp.append(chva)
			calcesp2.append(chva2) #depois
			valespe.append(float(va))
			valespe2.append(float(va)) #depois
			sinal = '<=>'

calcesp = ' + '.join(calcesp)
calcesp2 = ' + '.join(calcesp2)

probespecifico = []
probespecifico2 = [] #depois
if todos == True:
	valoresperanca = sum(esperanca)
	valoresperanca2 = sum(esperanca2) #depois
if todos == False:
	for vals in valespe:
		probespecifico.append(vals)

	for vals2 in valespe2: #depois
		probespecifico2.append(vals2)

valorespec = sum(probespecifico)
valorespec2 = sum(probespecifico2) #depois
vaespec = []
variespec = [] #depois
for nunm in probespecifico:
	vaespec.append(str(nunm))
vaespec2 = ' + '.join(vaespec)

for nunm2 in probespecifico2:
	variespec.append(str(nunm2))
variespec2 = ' + '.join(variespec) #depois

if todos == True:
	print('')
	if constante != None:
		print(f'Constante = {constanteimpressa} = {constante}')
		print('')
	print('Cálculo:')
	print('')
	print(f'E(X) = {calcesp} = {valoresperanca} ({valoresperanca:.2f})')
	print('')
	print(f'E(X²): P(X =) = {calcesp2} = {valoresperanca2} ({valoresperanca2:.2f})')
	print('')
	print(f'Var(X) = E(X²) - [E(X)]² = {valoresperanca2} - ({valoresperanca:.2f})² = {valoresperanca2} - {valoresperanca**2} = {valoresperanca2 - (valoresperanca**2)}')
	if valpoor == True:
		print('')
		print('----')
		print('')
		print('Distribuição acumulada:')
		for num in listavalpor:
			print(f'F(x) = {num}/{total_c}')
else:
	print('')
	print('Cálculo:')
	print(f'P(X {sinal} {x}) = {calcesp}')
	print(f'P(X {sinal} {x}) = {vaespec2} = {valorespec}')
	print(f'Resposta: {valorespec:.2f} ou {valorespec * 100:.2f}%')
	# print('')
	# print(f'Variancia: P(X {sinal} {x}) = {calcesp2}')
	# print(f'P(X {sinal} {x}) = {valespe2}')
