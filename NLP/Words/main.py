import unidecode

arquivo = open('input.txt','r')

arquivoT1 = arquivo.read().lower().replace(',',' ')

arquivoT2 = unidecode.unidecode(arquivoT1)

arrayTemp = arquivoT2.split()

vocabulario = list(set(arrayTemp))

vocabulario.sort()

saida = open('vocabulary.txt', 'a')

for word in vocabulario:
  saida.write(word + '\n')

arquivo.close()

saida.close()