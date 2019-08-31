# Conversao de um numero em base decimal para uma base qualquer especificada
# Entrada:  A porcao inteira do numero, Porcao fracionaria do numero, a base
#          em que o numero deve ser convertido e com quantas casas decimais de
#          precisao
# Saida: lista num que contem os digitos antes da virgula, lista posvirgula 
#        que contem os digitos depois da virgula
def convertBX(num,bSaida):
    saidanum = []

    while num >= bSaida:
        saidanum.append(num % bSaida) 
        num = num // bSaida 
    
    saidanum.append(num % bSaida)
    saidanum.reverse()
    
    return saidanum

# Conversao de um numero em uma base qualquer para o numero em base decimal ###
# Entrada: A porcao inteira do numero, Porcao fracionaria do numero, a base de
#          em que ambas porcoes do numero se encontra
# Saida: Tupla contendo respectivamente a porcao inteira  e a porcao 
#        fracionaria de entrada em base decimal 
def convertB10(num,bEntrada):
  soma = 0     
  
  for i in range(len(num)):
    soma += num[i] * bEntrada **(len(num) - i - 1) 
    
  return soma

# Dada uma palavra de tamanho lenPalavra calcula a quantidade de bits de pari-
# dade necessarios para criar um bloco de codigo de hamming
# Entrada: O tamanho da palavra a ser utilizada
# Saida: Quantidade de bits de paridade necessario para transmitir a palavra
# utilizando codigo de hamming.
def tamHamming(lenPalavra):
    lenParidade = 0
    
    # Proposito - incrementar o tamanho ate a desigualdade ser falsa
    # 2 ** p >= d + p + 1 tem q ser verdade
    while(2**(lenParidade) < lenParidade + lenPalavra + 1):
        lenParidade = lenParidade + 1
        
    
    return lenParidade

# Verifica paridade de uma lista de digitos binarios. Pode verificar paridade 
# par ou paridade impar
# Entrada: Uma lista chamada palavra contendo os digitos binarios, valor bina-
# rio tipoParidade que indica 0 para paridade par, e 1 para paridade impar
def checkParidade(palavra,tipoParidade):
    paridade = 0
    
    
    for i in range(len(palavra)):
        if palavra[i] == 1:
            paridade = paridade + 1
    
    return ((paridade+tipoParidade)%2)



# Entra com a palavra a ser enviada e cria o quadro a ser transmitido utilizan-
# do codigo de hamming.
# Entrada: Palavra de n bits, valor binario que indica 0 para utilizar paridade
# par e 1 para paridade impar.
# Saida: A palavra pronta para ser transmitida em codigo de hamming
def criaBlocoHamming(palavra,tipoParidade):
    lenParidade = tamHamming(len(palavra))  # Tamanho dos bits de correcao
    tamSaida = lenParidade + len(palavra)  # Tamanho da saida com bit de correcao
    contParidade = 0  # Contador de bits de paridade ja inserido
    contPalavra = 0  # Contador de bits de palavra ja inserida
    saida = []  # Tupla contendo lista de bits de saida
    pos = []  # Tupla contendo lista de valores binarios correspondente a cada posicao
    i = 0  # Contador para preencher o vetor/lista posicao em binario
    
    # Preenchendo saida com o valor de cada posicao em binario
    while i < tamSaida:
        # Converte a posicao atual para o valor em binario
        indB2 = convertBX(i+1,2)
        
        # Insere 0's para garantir que a palavra vai ser do tamanho lenParidade
        while len(indB2) < lenParidade:
            indB2.insert(0,0)
        
        # Insercao em lista de saida e lista de posicao
        saida.append(indB2)
        pos.append(indB2)
        
        # Verifica se a soma do valor binario da posicao eh 1
        checkTipo = sum(saida[i])
        
        # Se nao for 1, eh posicao de bit de palavra, faz a insercao do bit
        if checkTipo != 1:
            saida[i] = palavra[contPalavra]
            contPalavra = contPalavra + 1            
        
        i = i+1
    
    
    # Como todos bits de palavra ja estao na palavra, pode calcular os bits de paridade
    i = 0
    listVer = []
    
    # Percorre ate todos bits de paridade serem definidos
    while contParidade < lenParidade:
        checkTipo = sum(pos[i])  # Se for 1 - eh bit paridade, se nao, eh bit palavra
        
        # Se for bit de paridade, realiza o calculo e insercao de paridade par
        if checkTipo == 1:
            # Pega a posicao do bit 1 na posicao do bit paridade
            indice = pos[i].index(1)  
           
            # Pega todos bits de palavra com posicao binaria no indice == 1
            for j in range(len(pos)):
               if pos[j][indice] == 1 and j != i:
                    # Cria uma lista de digitos para calcular a paridade
                   listVer.append(saida[j])
            
            # Insere o bit de paridade calculado na lista de saida
            saida[i] = checkParidade(listVer,tipoParidade)
            contParidade = contParidade + 1
            listVer.clear()
            
        i = i+1
        
    return saida

# Dado um bloco codificado com codigo de hamming, verificar e corrigir erro
# introduzido pela transmissao.
# Entrada: Bloco transmitido, quantidade de bits de palavra, quantidade de bits
# de paridade, o tipo de paridade utilizado (0 - par, 1 - impar)
# Saida: O codigo corrigido. A correcao so funciona para um erro. De qualquer
# forma o usuario vai ser informado que ouve um erro.
def verCodHamming(bloco,lenPalavra,lenParidade,tipoParidade):
    # Percorre ate todos bits de paridade serem definidos
    contParidade = 0
    pos = []
    listVer = []
    res = []
    
    # Criacao do vetor com valor binario das posicoes    
    for i in range(lenPalavra+lenParidade):
        # Converte a posicao atual para o valor em binario
        indB2 = convertBX(i+1,2)
        
        # Insere 0's para garantir que a palavra vai ser do tamanho lenParidade
        while len(indB2) < lenParidade:
            indB2.insert(0,0)
        
        # Insercao em lista de saida e lista de posicao
        pos.append(indB2)
    
    i = 0
    
    # Verificacao de bits de paridade para ver se codigo chegou certo
    while contParidade < lenParidade:
        checkTipo = sum(pos[i])  # Se for 1 - eh bit paridade, se nao, eh bit palavra
        
        # Se for bit de paridade, realiza o calculo de paridade utilizando bits de palavra e bits de paridade
        if checkTipo == 1:
            # Pega a posicao do bit 1 na posicao do bit paridade
            indice = pos[i].index(1)  
           
            # Pega todos bits de palavra com posicao binaria no indice == 1 incluindo o proprio bit de paridade
            for j in range(len(pos)):
               if pos[j][indice] == 1:
                    # Cria uma lista de digitos para calcular a paridade
                   listVer.append(bloco[j])
            
            # Insere o bit de paridade calculado na lista de posicao de erro
            res.append(checkParidade(listVer,tipoParidade))
            contParidade = contParidade + 1
            listVer.clear()
            
        i = i+1
    
    # Inverte a posicao e transforma valor binario para base 10 para identificar posicao de erro
    res.reverse()
    pos = convertB10(res,2)
    
    # Se a posicao for maior que 0, entao ouve erro, e com indice 0 esta na posicao pos-1
    if pos > 0:
        print("Posicao do erro (indice 0): ", (pos-1))
        bloco[pos-1] = (bloco[pos-1]+1)%2
        
    return bloco

# Palavra a ser transmitida
palavra = [1,0,1,1,0]
print("Palavra a ser transmitida: ", *palavra)

# Tipo de paridade: 0 - Par // 1 - Impar
tipoParidade = 1

# Criando o quadro em codigo de hamming com paridade par a partir da palavra 
quadro = criaBlocoHamming(palavra,tipoParidade)
#101101110
print("Quadro a ser enviado: ",*quadro)

# Inserindo erro na palavra
posErro = 6
quadro[posErro] = 0
print("Erro introduzido na pos: ",posErro)
print("Quadro com erro: ", *quadro)

# Verificao de erro e tentativa de correcao - correcao funciona apenas para um 
# unico erro
x = verCodHamming(quadro,len(palavra),tamHamming(len(palavra)),1)
print("Quadro recebido: ",*x)