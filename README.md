# codigo-hamming
Implementação da lógica de envio de palavras com detecção e correção de erro utilizando código de hamming. 

# Estrutura básica do programa
A lógica básica do programa é implementada através de três funções. A primeira é utilizado para calcular a quantidade de bits de paridade necessário para realizar a transmissão da palavra com identificação de erros. 

A segunda função chamada de criaBlocoHamming é utilizada para dado uma palavra, criar um bloco a ser transmitindo codificado com código de hamming permitindo paridade par ou ímpar. 

A terceira função é chamada de verCodHamming e a sua função é verificar se o bloco chegou corretamente. Para isto é necessário informar a quantidade de bits de dados, bits de paridade e tipo de paridade utilizada para codificar a palavra. 
