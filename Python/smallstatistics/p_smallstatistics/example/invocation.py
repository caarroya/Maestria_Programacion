from p_smallstatistics import m_smallstatistics

#En este bloque puedes e diligenciar el valor de la tupla numerica con los datos que deseas calcular las funciones estadisticas , adicional el peso
v_data = (10 , 50 , 30 , 40)
v_weigt = (1 , 2 , 3, 4 )



def f_tupla_isNumber(v_data):
    for i in v_data:

        if not isinstance(i, (int, float)):
            return False
    
    return True



if f_tupla_isNumber(v_data) and f_tupla_isNumber(v_weigt) :
    
    v_Mediana = m_smallstatistics.f_Median(v_data)
    v_variance = m_smallstatistics.f_Variance(v_data)
    v_desEstandar = m_smallstatistics.f_standard_Deviation(v_data)
    v_Weighted_Mean = m_smallstatistics.f_Weighted_Mean(v_data, v_weigt)
    print ("El valor variaza es: " , v_variance)
    print ("El valor de la mediana es: " , v_Mediana)
    print ("El valor de la desviación estandar es: " , v_desEstandar)
    print ("El valor de la  Media Ponderada es: " ,v_Weighted_Mean)

else:

    print("La tupla contiene elementos NO numéricos.")