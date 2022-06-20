################# ISSO É BERNOULLI ###################

totaltipos = '50'
tipo1 = '30' #Fracasso
tipo2 = '20' #Sucesso
fracasso = 0
sucesso = 1
if ',' in totaltipos:
    totaltipos = totaltipos.replace(',', '.')
totaltipos = float(totaltipos)
if ',' in tipo1:
    tipo1 = tipo1.replace(',', '.')
tipo1 = float(tipo1)
if ',' in tipo2:
    tipo2 = tipo2.replace(',', '.')
tipo2 = float(tipo2)

def probtipo(tipo, total_tipos=totaltipos): #Função de achar probabilidade do item
    return tipo / total_tipos

def fatorial(numero):
    resfatorial = 1
    for n in range(1, numero + 1):
        resfatorial *= n

    return resfatorial

def calcbinomial(ensaio):
    calcbi = (fatorial(n_max) / (fatorial(ensaio) * fatorial(nmenosx))) * (taxadesucesso ** ensaio) * (1 - taxadesucesso) ** nmenosx
    return calcbi

ptipo1 = probtipo(tipo1)
ptipo2 = probtipo(tipo2)

suc_fra = sucesso

media_p = suc_fra * probtipo(tipo2) # media_p = E(X)

variancia_x = ptipo1 * ptipo2 # tacerto


################## AGORA É BINOMIAL ##########################

#Opções gerais de escolha
exato = True
menor = False

n_ensaios = int(input('Quantas vezes vai lançar o ensaio? (N)\nResposta: '))

taxadesucesso = input('Informe a taxa de sucesso (%) (P): ') # Isso é o valor de P
if '%' in taxadesucesso:
    taxadesucesso = taxadesucesso.strip('%')
if ',' in taxadesucesso:
    taxadesucesso = taxadesucesso.replace(',', '.')
taxadesucesso = float(taxadesucesso)
taxadesucesso = taxadesucesso / 100

n_max = n_ensaios
npossibilidades = []
for ensaio in range(n_ensaios+1):
    npossibilidades.append(ensaio)

# calc_ensaio = X
calc_ensaio = int(input(f'Calcular a probabilidade de qual número? (X)\nOpções disponíveis: {npossibilidades}\nResposta: '))
opcoesensaio = calc_ensaio

# perg = input('Escolha o que calcular:\n\n1. Exatidão (=)\n2. Menor que (<)\n\nResposta: ')
# if perg.upper().startswith(('1','=', 'EXA')):
#     exato = True
# if perg.upper().startswith(('2','<', 'MEN')):
#     menor = True


nmenosx = n_max-calc_ensaio
if exato == True:
    probabinomial = calcbinomial(calc_ensaio)
    probabinomial_impresso = f'P(X = {n_max}) = ({n_max}! / {calc_ensaio}!) x ({n_max-calc_ensaio}!) x ({taxadesucesso}^{calc_ensaio}) x (1 - {taxadesucesso})^({n_max}-{calc_ensaio})'

# elif menor == True:
#     ensaiobinomial = []
#     calimpresso = []
#
#     for op in range(opcoesensaio+1):
#         ensaiobinomial.append(calcbinomial(op))
#         calimpresso.append(f'P(X = {n_max}) = ({n_max}! / {op}!) x ({n_max-op}!) x ({taxadesucesso}^{op}) x (1 - {taxadesucesso})^({n_max}-{op})')
#
#     calimpresso = ' + '.join(calimpresso)
#     if calimpresso.endswith(' + '):
#         calimpresso = calimpresso[:-3]
#
#     metadecalim = ' + '.join(ensaiobinomial)
#     if metadecalim.endswith(' + '):
#         metadecalim = metadecalim[:-3]

if exato == True:
    print('')
    print('Cálculo:')
    print('')
    print(f'{probabinomial_impresso} = {probabinomial:.7} (arredondado = {probabinomial:.2f})')
    print('')
    esperança = input('Para calcular a esperança e variancia, digite E. Aperte qualquer outra tecla para encerrar.\n')
    if esperança.upper() == 'E':
        print(f'Esperança: E(X) = n x p = {n_max} x {taxadesucesso} = {n_max * taxadesucesso} (arredondado = {n_max * taxadesucesso:.2f})')
        print(f'Variância: Var(X) = n x p (1-p) = {n_max} x {taxadesucesso} x (1-{taxadesucesso} = {(n_max * taxadesucesso) * (1 - taxadesucesso)})')

    else:
        pass


# Agora fazer a letra B (minuto 21)
#
# elif menor == True:
#     print('')
#     print('Cálculo:')
#     print('')
#     print(f'{calimpresso}')
#     print(f'{metadecalim}')
#     print(f'ensaiobinomial = {ensaiobinomial}')
#     print(f'Resposta: {sum(ensaiobinomial)}')