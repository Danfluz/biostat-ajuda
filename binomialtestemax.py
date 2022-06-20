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

ptipo1 = probtipo(tipo1)
ptipo2 = probtipo(tipo2)

suc_fra = sucesso

media_p = suc_fra * probtipo(tipo2) # media_p = E(X)

variancia_x = ptipo1 * ptipo2 # tacerto


################## AGORA É BINOMIAL ##########################

nomaximo = True
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

nmenosx = n_max-calc_ensaio
if nomaximo == True:
    listamax = []
    for chn in npossibilidades:
        nmenosx2 = n_max - chn
        if chn < calc_ensaio+0.1:
            chn2 = (fatorial(n_max) / (fatorial(chn) * fatorial(nmenosx2))) * (taxadesucesso ** chn) * (1 - taxadesucesso) ** nmenosx2
            listamax.append(chn2)
            print(f'p({chn}) = {chn2}')
        else:
            pass

probabinomial = ( fatorial(n_max) / ( fatorial(calc_ensaio) * fatorial(nmenosx) ) ) * (taxadesucesso**calc_ensaio) * (1-taxadesucesso)**nmenosx
probabinomial_impresso = f'P(X = {n_max}) = ({n_max}! / {calc_ensaio}!) x ({n_max-calc_ensaio}!) x ({taxadesucesso}^{calc_ensaio}) x (1 - {taxadesucesso})^({n_max}-{calc_ensaio})'

print('')
print('Cálculo:')
print('')
print(f'{probabinomial_impresso} = {probabinomial:.7} (arredondado = {probabinomial:.2f})')
print('')
esperança = input('Para calcular a esperança e variancia, digite E. Aperte qualquer outra tecla para encerrar.\n')
if esperança.upper() == 'E':
    print(f'Esperança: E(X) = n x p = {n_max} x {taxadesucesso} = {n_max*taxadesucesso} (arredondado = {n_max*taxadesucesso:.2f})')
    print(f'Variância: Var(X) = n x p (1-p) = {n_max} x {taxadesucesso} x (1-{taxadesucesso} = {(n_max*taxadesucesso) * (1-taxadesucesso)})')
else:
    pass