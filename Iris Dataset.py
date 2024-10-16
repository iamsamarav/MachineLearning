from sklearn.datasets import load_iris

base = load_iris()
print(base.data) #Retorno das medições
print(base.target) #Valores de classificação
print(base.target_names) #Nomes da classificação

entrada = base.data
saidas = base.target
rotulos = base.target

#Tamanho das matrizes

print(base.data.shape)
print(base.target.shape)

