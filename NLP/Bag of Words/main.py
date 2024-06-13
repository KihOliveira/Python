import os
import unidecode

#Funcoes
def att_VCole(vocabCollection):
  print(vocabCollection)
  saida = open('vocabCole.txt', 'a')
  for word in vocabCollection:
    saida.write(word + '\n')

def create_specific_vocab(file):
    arrayWords = file.read().lower().replace(',', '').replace('.', '').replace('"', '').replace('!', '').replace('?', '')
    vocabulario = unidecode.unidecode(arrayWords)
    vocabulario = vocabulario.split()
    vocabulario = list(set(vocabulario))
    vocabulario.sort()
    return vocabulario

def generateVocabCole(file_path):
  vocabCollection = []
  for file in os.listdir(): 
    if file.endswith(".txt") and file != 'vocabCole.txt': 
        file_path = f"{current_path}/{file}"
        file = open(file_path, "r")
        specificVocab = create_specific_vocab(file)
        vocabCollection = [*vocabCollection,*specificVocab]
        vocabCollection = list(set(vocabCollection))
        vocabCollection.sort()
  return vocabCollection

def create_bow(file):
  BoW = []
  vocabCollection = open('vocabCole.txt', 'r')
  vocabCollection = vocabCollection.read()
  vocabEspecifico = create_specific_vocab(file)
  print(vocabEspecifico)
  for word in vocabCollection:
        count = 0
        if word in vocabEspecifico:
          count = 1
        BoW.append(count)
  return BoW

def generateBoW(file_path):
  for file in os.listdir(): 
    if file.endswith(".txt") and file != 'vocabCole.txt': 
      file_path = f"{current_path}/{file}"
      file = open(file_path, "r")
      BoWTemp = create_bow(file)
      print(BoWTemp)


#Main

current_path = os.getcwd()
os.chdir(current_path)

att_VCole(generateVocabCole(current_path))
generateBoW(current_path)

