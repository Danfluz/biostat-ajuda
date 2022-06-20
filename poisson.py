import math
##### DESCOMENTE PARA PODER PERGUNTAR INTERATIVAMENTE #####
# media = input('Informe a média (lambda)\nResposta: ')
# if ',' in media:
#     media = media.replace(',', '.')
# tempo = input('Informe o tempo (em horas)\nResposta: ')
# if ',' in tempo:
#     tempo = tempo.replace(',', '.')

def fatorial(numero): # Função fatorial
    resfatorial = 1
    for n in range(1, numero + 1):
        resfatorial *= n

    return resfatorial

def fpoisson(x):
    ppoisson = ((lambtempo ** x) * math.exp(-lambtempo)) / (fatorial(x))
    return ppoisson

#Lambda
media = '0.61' # E(X)
tempo = '1' # Horas

media = float(media)
tempo = float(tempo)
f_lambda = media / tempo
print('Calcular Poisson')
print('')
sinal = input('Maior que (>)\n'
              'Menor que (<)\n'
              'No Maximo (Max)\n'
              'No Minimo (Min)\n'
              # '"os dois"\n'
              'ou deixe em branco para exatidão\n\nResposta: ')
exato = False
maiorque = False
menorque = False
osdois = False
maximo = False
minimo = False

# if sinal.upper().startswith(('>', 'MAI')):
#     maiorque = True
if sinal.upper().startswith(('MIN', 'MÍN')):
    maiorque = True
    minimo = True
elif sinal.upper().startswith(('MAX', 'MÁX')):
    menorque = True
    maximo = True
elif sinal.upper().startswith(('<', 'MEN')):
    menorque = True

# elif sinal.upper().startswith(('2', 'DOIS', 'OS')):
#     osdois = True
elif sinal.upper().startswith(('=', 'EXA')):
    exato = True
else:
    exato = True

x = input('Calcular qual probabilidade? (X)\nResposta: ')
xis = x
tempo = int(input('Em quantas horas? (tempo)'))
if ',' in x:
    x = x.replace(',', '.')
x = int(x)


lambtempo = f_lambda * tempo
## poisson = ((lambda * tempo)^x * [exponencial de -lambda * tempo]) / x!
if exato == True:
    print('')
    print('Cálculo: ')
    print(f'P(X={x};t={tempo}) = (({f_lambda} x {tempo})^{x} x e^(-{f_lambda}x{tempo})) / {x}!')
    print('')
    print(f'P(X={x};t={tempo}) = ({lambtempo ** x} x {math.exp(-lambtempo)} / {fatorial(x)})')
    print('')
    # formpoisson = ((lambtempo ** x) * math.exp(-lambtempo)) / (fatorial(x))
    formpoisson = fpoisson(x)
    print(f'P(X={x};t={tempo}) = ', formpoisson)
    print('')
    if round(formpoisson, 2) > 0.009:
        print(f'Resposta: {round(formpoisson, 2)} ou {round(formpoisson, 2) * 100}% (arredondado)')
    elif round(formpoisson, 3) > 0.0009:
        print(f'Resposta: {round(formpoisson, 3)} ou {round(formpoisson, 3) * 100}% (arredondado)')
    elif round(formpoisson, 4) > 0.00009:
        print(f'Resposta: {round(formpoisson, 4)} ou {round(formpoisson, 4) * 100}% (arredondado)')
    else:
        print(f'Resposta: {formpoisson} ou {formpoisson * 100}%')

#Calcular como fazer isso, minuto 8.50 da aula de poisson

if menorque == True: # FUNCIONOU ISSO
    listamenor = []
    menorcalculo = []
    menorcalcdesenv = []
    if maximo == True:
        limite_ra = x+1
    else:
        limite_ra = x
    for ra in range(0,limite_ra):
        listamenor.append(fpoisson(ra))
        menorcalculo.append(f'P(X = {ra}) +')
        menorcalcdesenv.append(f'( (({f_lambda} x {tempo})^{ra} x e(-{f_lambda}x{tempo})) / {ra}! ) +')
        menorcalculo[-1] = menorcalculo[-1].strip(' +')
    menorcalcdesenv[-1] = menorcalcdesenv[-1].strip(' +')
    print('')
    print('Cálculo: ')
    print('')
    print(f'P(X={x};t={tempo}) = ',' + '.join(menorcalculo))
    print('')
    print(*menorcalcdesenv, f'= {sum(listamenor)}')
    print('')
    print(f'Resposta: {sum(listamenor)}')

if maiorque == True: # TESTANDO...
    listamaior = []
    maiorcalculo = []
    maiorcalcdesenv = []
    if minimo == True:
        limite_li = x

    for li in range(0,limite_li):
        listamaior.append(fpoisson(li))
        maiorcalculo.append(f'P(X = {li}) +')
        maiorcalcdesenv.append(f'( (({f_lambda} x {tempo})^{li} x e(-{f_lambda}x{tempo})) / {li}! ) +')
        maiorcalculo[-1] = maiorcalculo[-1].strip(' +')
    maiorcalcdesenv[-1] = maiorcalcdesenv[-1].strip(' +')
    print('')
    print('Cálculo: ')
    print('')
    print(f'P(X={x};t={tempo}) = 1 -',' + '.join(maiorcalculo))
    print('')
    print(f'P(X={x};t={tempo}) = ', *maiorcalcdesenv, f'= {sum(listamaior)}')
    print('')
    print(f'P(X={x};t={tempo}) = 1 - {sum(listamaior)}')
    print('')
    print(f'Resposta: {1-sum(listamaior)} ou {1-sum(listamaior):.2f}%      <-- (a porcentagem pode conter erros)')

    print('--')
    print('--')
    print(listamaior)
