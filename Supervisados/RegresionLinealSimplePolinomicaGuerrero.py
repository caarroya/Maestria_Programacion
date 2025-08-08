import math
import numpy as np
import matplotlib.pyplot as plt



def pf(x_n, c_k):
    return x_n ** c_k -1


# --- Datos de entrenamiento ---

#se puede reemplazar por pandas para leer un csv y capturar variables que son columnas del archivo
x_base = np.linspace(0, 1, 100)
y_base = 2 * np.pi * x_base + np.sin(x_base) + np.random.randn(100)

# Cross validation

alpha = 0.7
index_total = np.random.permutation(len(x_base))
# 70% de los datos para entrenamiento y 30% para test
x_train = x_base[index_total[:round(alpha * len(x_base))]]
y_train = y_base[index_total[:round(alpha * len(x_base))]]
x_test = x_base[index_total[round(alpha * len(x_base)):]]
y_test = y_base[index_total[round(alpha * len(x_base)):]]

#x = [0.1, 0.4, 0.5, 0.7, 0.9]
# y = np.random.choice(y_base, size=100, replace=True)

# --- Definir centros ---
#c = x_base


N = len(x_train)
K = 2

# --- Construir la matriz Phi ---
Pf = np.zeros((len(x_train), K))

for n in range(N):
    for k in range(K):
        Pf[n][k] = pf(x_train[n], k)        


w = np.linalg.pinv(Pf)  @ y_train


pf_test = np.zeros((len(x_test), K))
for n in range(len(x_test)):
    for k in range(K):
        pf_test[n][k] = pf(x_test[n], k)
        
pf_test2= np.zeros((len(x_base), K))
for n in range(len(x_base)):
    for k in range(K):
        pf_test2[n][k] = pf(x_base[n], k)

yhat = pf_test @ w
yhat2 = pf_test2 @ w

# --- Graficar ---
plt.figure(figsize=(8, 5))
plt.plot(x_base, yhat2, label='Modelo RBF (yhat)', color='blue')
plt.scatter(x_train, y_train, label='Datos originales', color='red')
plt.title("Regresión con funciones base")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

