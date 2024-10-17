from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

base = load_iris()
print(base.data) #Retorno das medições
print(base.target) #Valores de classificação
print(base.target_names) #Nomes da classificação

entrada = base.data
saidas = base.target
rotulos = base.target_names

#Tamanho das matrizes

print(base.data.shape)
print(base.target.shape)

#Aplicando o modelo KNN -> Proximidade de K

knn = KNeighborsClassifier(n_neighbors=1) #Proximidade de um número quanto a amostra vizinha
knn.fit(entrada, saidas) #Alimenta o processador
especie = knn.predict([[5.9,3,5.1,1.8]])[0] #Previsão
print(especie)
rotulos[especie]

#Aplicando treino e teste

etreino, eteste, streino, steste = train_test_split(entrada, saidas, test_size = 0.25)

knn.fit(etreino, streino)
previsor = knn.predict(eteste)

#Metricas avaliativos de um rede neural

margem_acertos = metrics.accuracy_score(steste, previsor)



