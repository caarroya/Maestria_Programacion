import math 
from collections import Counter

'''
Es funcion se encarga de retornar 3 valores , la sumatoria de todos los elementos de la tupla entrada, la longitud y la tupla ordena
'''
def f_sumarize (v_data):
    v_data_sort = sorted(v_data)
    v_adds = 0 
    v_lengths=len(v_data)
    for i in v_data:
        v_adds += i       
    return v_adds , v_lengths , v_data_sort

'''
En este funcion calculamos la varianza, la cual consiste en calcular la suma de los cuadrados.
Adicional invoca la funcion de sumarizacion 
Retorna la Varianza 
'''

def f_Variance(v_data):
    v_outs , v_len, v_data_sort = f_sumarize(v_data)
    v_means =  v_outs / v_len
    v_sum_of_squares = (1/v_len)*sum((x - v_means)** 2 for x in v_data_sort)
    return v_sum_of_squares


'''
Funcion encargada de capturar la mediana
'''
def f_Median(v_data):
    
    v_outs , v_len , v_data_sort = f_sumarize(v_data)
    # Si el número de datos es impar
    if v_len % 2 == 1:
        v_Median = v_data_sort[v_len // 2]
    else:
        # Si el número de datos es par
        v_Median = (v_data_sort[v_len // 2 - 1] + v_data_sort[v_len // 2]) / 2
    
    return v_Median

'''
Funcion encargada de calcular la desviación estandar, para este caso se utiliza la funcion sqrt del modulo math de python
para calcular la raiz cuadrada
'''
def f_standard_Deviation (v_data):
    v_variance = f_Variance(v_data)
    v_standar_Des = math.sqrt(v_variance)
    return v_standar_Des


def f_Weighted_Mean(v_data, v_weight):
    '''
    La media pondera es la sumatoria de multiplicar cada elemento de la tupla por el peso de cada elemento , todo divido entre la sumatoria de los pesos
    '''
    # Verificar que las listas de valores y pesos tengan la misma longitud
    if len(v_data) != len(v_weight):
        raise ValueError("La lista de valores y pesos deben tener la misma longitud.")
    #Se calcula el numerador, multiplicando posicion de la tupla por el peso
    v_nume = sum(x * w for x, w in zip(v_data, v_weight))
    #Se calcula el denominador
    v_deno = sum(v_weight)
    #Se calcula la Media Ponderar
    v_Weighted_Mean = v_nume / v_deno
    return v_Weighted_Mean


'''
Esta funcion se utiliza para calcular la moda, se hace uso del paquete collect y del modulo Counter, para contar la cantidad de objetos en la tupla
'''

def f_Mode(v_data):
    v_count = Counter(v_data)
    v_max_frecuency = max(v_count.values())
    v_modas = [valor for valor, frecuencia in v_count.items() if frecuencia == v_max_frecuency]
    if v_max_frecuency == 1:
        return "No hay moda"
    else:
        return v_modas

