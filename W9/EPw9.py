import re
def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

  #texto lista contendo cada texto:
def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

  #lista de palavras:
def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

  #num de palavras:
def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

  #num de palavras diferentes:
def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
  sab = 0
  for i in range(6):
    a = float(as_a[i])
    b = float(as_b[i])
    sab = sab + (abs(a - b))
  return sab
def calcula_assinatura(texto):
  sentencas = separa_sentencas(texto)
  frases = []
  for s in sentencas:
    frases.extend(separa_frases(s))
  palavras = []
  for f in frases:
    palavras.extend(separa_palavras(f))
  npu = n_palavras_unicas(palavras)
  npd = n_palavras_diferentes(palavras)
  total = 0
  for p in palavras:
    total = total + len(p)
  wal = total / len(palavras)
  ttr = npd / len(palavras)
  hlr = npu / len(palavras)
  total = 0
  for s in sentencas:
    total = total + len(s)
  sal = total / len(sentencas) 
  sac = len(frases) / len(sentencas)
  total = 0 
  for f in frases:
    total = total + len(f)
  pal = total / len(frases)
  return [wal, ttr, hlr, sal, sac, pal]
    
def avalia_textos(textos, ass_cp):
  sabs = []
  for t in textos:
    ass_t = calcula_assinatura(t)
    sab = compara_assinatura(ass_t, ass_cp)
    sabs.append(sab)
  i = int(sabs.index(min(sabs)))
  return(i + 1)
  
  







assinatura = le_assinatura()
textos = le_textos()
infectado = avalia_textos(textos, assinatura)
print('O autor do texto',infectado,'está infectado com COH-PIAH')
