import math
import numpy as np
import matplotlib.pyplot as plt



def pf(x_n, c_k):
    return x_n ** c_k -1


# --- Datos de entrenamiento ---

#se puede reemplazar por pandas para leer un csv y capturar variables que son columnas del archivo
x_base = [0.1, 0.4, 0.5, 0.7, 0.9]
y_base = [0.2, 0.5, 0.6, 0.9, 1.1]

x = np.random.choice(x_base, size=100, replace=True)

#x = [0.1, 0.4, 0.5, 0.7, 0.9]
y = np.random.choice(y_base, size=100, replace=True)

# --- Definir centros ---
c = x_base


N = len(x)
K = 2

# --- Construir la matriz Phi ---
Pf = np.zeros((N, K))

for n in range(N):
    for k in range(K):
        Pf[n][k] = pf(x[n], k)
 

print (type(Pf))
print (Pf)
print (Pf.shape)

Pf_pinv = np.linalg.pinv(Pf)    

print (Pf_pinv)


#me falta multiplicar W por 

w = Pf_pinv @ y                   


w = np.linalg.pinv(Pf)  @ y 

# --- Predecir nuevos valores ---

x_test = np.linspace(0, 1, 100)

pf_test = np.zeros((len(x_test), K))
for n in range(len(x_test)):
    for k in range(K):
        pf_test[n][k] = pf(x_test[n], k)

yhat = pf_test @ w

# --- Graficar ---
plt.figure(figsize=(8, 5))
plt.plot(x_test, yhat, label='Modelo RBF (yhat)', color='blue')
plt.scatter(x, y, label='Datos originales', color='red')
plt.title("Regresión con funciones base")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

