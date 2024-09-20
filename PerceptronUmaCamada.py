#Execução do código de um perceptron de uma camada

import numpy as np

entradas = np.array([1,9,5])
pesos = np.array([0.8,0.1,0])

def soma(e,p):
    return e.dot(p)

soma = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0 

saida = stepFunction(soma)
print(saida)

