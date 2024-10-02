import nltk 
from base import base
nltk.download('popular')

stopwords = nltk.corpus.stopwords.words('portuguese') #Palavras irrelevantes

def removestopwords(texto):
    frases = []
    for (palavras, emocao) in texto:
        removesw =  [p for p in palavras.split()]
        frases.append((removesw, emocao))
    return frases

def reduzpalavras(texto): #Faz-se a remoção do sufixo extraindo o radical da palavra
    steemer = nltk.stem.RSLPStemmer()
    frases_redux = []
    for (palavras, emocao) in texto:
        reduzidas = [str(steemer.stem(p)) for p in palavras.split() if p not in stopwords]
        frases_redux.append((reduzidas, emocao))
    return frases_redux


