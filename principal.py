import math

#declarando todas as variaveis e vetores globais
vetor = []
fa = []
fr = []
x1 = []
fax1 = []
facum = []
intervalo = []
desvioMedio = []
desvioSimples = []
media = 0
linhap = 0
op = 1

def inserindoValores(vetor, op):
    op = 1
    while op != 0:
        valor = input('insira um valor ou pressione 0 para finalizar: ')
        try:
            valor = int(valor)
            if valor == 0:
                op = 0
            else:
                vetor.append(valor)
        except ValueError:
            print('Valor inválido. Por favor, insira um número inteiro ou pressione 0 para finalizar.')
inserindoValores(vetor, op)
print('-'*50)
    

# vetor = [ 20, 29, 40, 31, 50, 32, 20,
#         49, 29, 31, 55, 60, 19, 17,
#         18, 18, 72, 38, 35, 38, 43,
#         20, 50, 57, 32, 30, 20, 21,
#         30, 32, 33, 31, 31, 34, 40,
#         19, 24, 25, 36, 25, 26, 28,
#         29, 29, 25, 29, 27, 33, 35]

n = len(vetor)
print(f'\nquantidade de numeros: {n}')
maior = max(vetor)
menor = min(vetor)

# Calculando o número de classes
k = int(math.sqrt(n))
print(f'classes: {k}')

# Calculando a amplitude
amplitude = (maior - menor) / k
print(f'amplitude: {amplitude}\n')

def criandoIntervalo(menor, amplitude): #criando o intervalo da tabela(amplitude)
    for i in range(k+1):
        if i == 0:
            intervalo.append(menor)
        else:
            intervalo.append(amplitude + intervalo[i-1])
criandoIntervalo(menor, amplitude)

def calculoFa(fa, intervalo, vetor): #calculando fa
    for i in range(k):
        fa.append(0)  # Inicializa a lista de frequência absoluta com zeros
    #calculando FA
    for i in range(n):
        for j in range(k):
            if intervalo[j] <= vetor[i] <= intervalo[j+1]:
                fa[j] += 1
                break 
calculoFa(fa, intervalo, vetor)
        
def valoresTabela(fa, fr, x1, fax1, facum): #calculando fr, x1, fax1, facum
    for c in range(k):
        fr.append(fa[c]/n) #calculando o FR
        x1.append((intervalo[c]+intervalo[c+1])/2) #calculando o X1
        fax1.append(fa[c]*x1[c]) #calculando o FA.x1
        if c == 0: #calculando o FACUM
            facum.append(fa[c])
        else:
            facum.append(fa[c] + facum[c-1])
valoresTabela(fa, fr, x1, fax1, facum)

#printando a tabela
print('    Amplitude         FA     FR      X1      FA.X1     FACUM')
for i in range(k):
    print(f'{round(intervalo[i],2):<5} |----  {round(intervalo[i+1],2):<5} | {fa[i]:<4} | {round(fr[i],2):<4} | {round(x1[i],2):<6} | {round(fax1[i],2):<7} | {facum[i]:<5}')

#calculando posição da mediana
pos_mediana = (n+1)/2
print(f'\nposição da mediana: {pos_mediana}')

#pegando posião da mediana
for c2 in range(len(facum)):
    if pos_mediana <= facum[c2]:
        linhap = c2
        break
print(f'linha principal: {linhap+1}º')

def calculoMedias(n, facum, linhap): #calculo da media e da mediana
    global media
    media = sum(fax1)/n #calculando media
    print(f'media: {round(media, 2)}')

    #calculando mediana
    if linhap == 0: facum[linhap-1] = 0 
    mediana = intervalo[linhap] + ((n/2) - facum[linhap-1]) / fa[linhap] * amplitude

    print(f'mediana: {round(mediana, 2)}')
calculoMedias(n, facum, linhap)

def calculoModas(intervalo, linhap, fa, amplitude): #calulo da moda king e moda czuber
    if linhap == 0: fa[linhap-1] = 0
    if linhap == k-1: fa.append(0)
    king = intervalo[linhap] + (fa[linhap+1] / (fa[linhap-1]+fa[linhap+1])) * amplitude #moda king
    print(f'moda king: {round(king, 2)}')

    delta_anterior = fa[linhap]-fa[linhap-1]
    delta_posterior = fa[linhap]-fa[linhap+1]
    czuber = intervalo[linhap] + ( delta_anterior / (delta_posterior+delta_anterior)) * amplitude #moda czuber

    print(f'moda czuber: {round(czuber, 2)}')#printando os resultados
calculoModas(intervalo, linhap, fa, amplitude)

def calculoDesvios(media, x1, desvioSimples, desvioMedio): #calculo do devio simples e medio
    for x in range(k):
        desvioSimples.append(x1[x] - media)#caculando e inserindo no vetor o desvio simples
        desvioMedio.append(desvioSimples[x]**2)#caculando e inserindo no vetor o desvio medio

    print('\ndevio simples     desvio medio')#printando a tabela de desvios
    for c in range(k):
        print(f'    {round(desvioSimples[c], 2):<8}   |   {round(desvioMedio[c], 2)}')
calculoDesvios(media, x1, desvioSimples, desvioMedio)

def variancia_e_DesvioPadrao(desvioMedio, n):#calculo da variancia e desvio padrao
    variancia = sum(desvioMedio)/(n-1)
    desvio_padrao = math.sqrt(variancia)
    print(f'\nvariancia: {round(variancia, 2)}\ndesvio padrão: {round(desvio_padrao, 2)}\n')#printando o resultado
variancia_e_DesvioPadrao(desvioMedio, n)
print('-'*50)