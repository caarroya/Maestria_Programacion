
# calcular una regresion y= mx + b

# calcular una regresion. y = mx^2  + mx + b



def calcular_promedio (valores):
    return  sum(valores)/len(valores)


def calcular_pendiente( x ,y):
    n = len(x)

    promedio_x = calcular_promedio(x)
    promedio_y = calcular_promedio(y)

    numerador = 0
    denominador= 0

    for i in range(n):
        numerador += (x[i] - promedio_x)* (y[i] - promedio_y)
        denominador += (x[i] - promedio_x)**2 

    m = numerador/denominador

    return m

def calculo_interseccion ( x , y ,m):
    interseccion_x= calcular_promedio (x)
    interseccion_y = calcular_promedio(y)

    b= interseccion_y - m*interseccion_x

    return b



def entrenar_regresion_lineal(x, y):
    m = calcular_pendiente(x, y)
    b = calculo_interseccion(x, y, m)
    return m, b


def predecir (x , m , b):
    return [m * xi + b for xi in x]



# --- Ejemplo de uso ---
# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

m, b = entrenar_regresion_lineal(x, y)

print(f"Pendiente (m): {m}")
print(f"Interseccion (b): {b}")


x_nuevos = [6, 7, 8]
y_predichos = predecir(x_nuevos, m, b)
print("Predicciones:", y_predichos)
