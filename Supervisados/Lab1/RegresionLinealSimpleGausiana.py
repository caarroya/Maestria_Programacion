import math
import numpy as np
import matplotlib.pyplot as plt

# --- Función base: Gaussiana ---
def phi(x_n, c_k, sigma=0.1):
    return math.exp(-((x_n - c_k) ** 2) / (2 * sigma ** 2))



def pf(x_n, c_k):
    return x_n ** c_k -1


def sf(x_n, c_k):  
    return 1 / (1 + math.exp(- (x_n - c_k)))    



# --- Datos de entrenamiento ---
x = [0.1, 0.4, 0.5, 0.7, 0.9]
y = [0.2, 0.5, 0.6, 0.9, 1.1]

# --- Definir centros ---
c = [0.1, 0.4, 0.5, 0.7, 0.9]
#c = [0.0, 0.25, 0.5, 0.75, 1.0]  # 5 centros

N = len(x)
K = len(c)

# --- Construir la matriz Phi ---
Phi = np.zeros((N, K))

for n in range(N):
    for k in range(K):
        Phi[n][k] = phi(x[n], c[k], sigma=0.1)


Phi_pinv = np.linalg.pinv(Phi)     


#me falta multiplicar W por 

w = Phi_pinv @ y                   




# --- Predecir nuevos valores ---
  





x_test = np.linspace(0, 1, 100)

pf_test = np.zeros((len(x_test), K))
for n in range(len(x_test)):
    for k in range(K):
        pf_test[n][k] = pf(x_test[n], c[k])



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

