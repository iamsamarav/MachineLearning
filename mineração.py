import nltk 
nltk.download('rslp')

base = [('estou muito feliz', 'emoção positiva'),
        ('sou uma pessoa muito feliz', 'emoção positiva'),
        ('tudo bem comigo', 'emoção positiva'),
        ('alegria é o meu lema', 'emoção positiva'),
        ('comigo está tudo ok', 'emoção positiva'),
        ('muito bom ser amado', 'emoção positiva'),
        ('estou empolgado em começar', 'emoção positiva'),
        ('fui elogiado por meu trabalho', 'emoção positiva'),
        ('vencemos a partida', 'emoção positiva'),
        ('ganhei um presente', 'emoção positiva'),
        ('recebi uma promoção de cargo', 'emoção positiva'),
        ('estou bem, obrigada', 'emoção positiva'),
        ('o dia está muito bonito', 'emoção positiva'),
        ('estou bem, obrigado', 'emoção positiva'),
        ('me sinto satisfeito', 'emoção positiva'),
        ('fui aprovado', 'emoção positiva'),
        ('de bem com a vida', 'emoção positiva'),
        ('fui bem recebido em casa', 'emoção positiva'),
        ('estou com medo', 'emoção negativa'),
        ('estou com muito medo', 'emoção negativa'),
        ('estou um pouco triste', 'emoção negativa'),
        ('isto me deixou com raiva', 'emoção negativa'),
        ('fui demitida', 'emoção negativa'),
        ('esta comida está horrível', 'emoção negativa'),
        ('tenho pavor disso', 'emoção negativa'),
        ('de mal a pior', 'emoção negativa'),
        ('estou incomodado', 'emoção negativa'),
        ('estou sentindo dor', 'emoção negativa'),
        ('perdi a aposta', 'emoção negativa'),
        ('fui enganada', 'emoção negativa'),
        ('fiquei desmotivada com o resultado', 'emoção negativa'),
        ('que situação agoniante', 'emoção negativa'),
        ('estou doente', 'emoção negativa'),
        ('fui reprovado', 'emoção negativa')]

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

frases_reduzidas = reduzpalavras(base)


