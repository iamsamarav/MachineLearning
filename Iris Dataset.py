from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

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

#Teste com o for alterando o valor de n_neighbors

valores_k = {}
k = 1
while k < 25:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(etreino, streino)
    previsores_k = knn.predict(eteste)
    acertos = metrics.accuracy_score(steste, previsores_k)
    valores_k[k] = acertos
    k +=1
    
plt.plot(list(valores_k.keys()),list(valores_k.values()))
plt.xlabel('Valores de k')
plt.ylabel('Performance')
plt.show()

#Aplicando Regressão Logística

#Previsões categóricas

regl = LogisticRegression()
regl.fit(etreino, streino)
reg = regl.predict([[6.2,3.4,5.4,2.3]]) #Retorna o resultado mais provável
regproba = regl.predict_proba([[6.2,3.4,5.4,2.3]]) #Retorna todas as probabilidades
previsor_regl = regl.predict(eteste)
margem_acertos_regl = metrics.accuracy_score(steste, previsor_regl)