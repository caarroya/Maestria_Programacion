from p_smallstatistic import m_smallstatistic
import concurrent.futures
import time
import requests



def f_download_page(ciudad):
    
    url = f"https://weather.siel.com.co/city/{ciudad}/temp/max"
    
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer secret-token-1234',
    }
    
    try:
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        response.raise_for_status()
        response_data = response.json() *10
        return response_data, ciudad
    
    except Exception as e:
        print(f"Error descargando {ciudad}: {str(e)}")
        return [], ciudad
   
def f_parallel (datos):
    if datos == None or len(datos) == 0:
        print(f"Error en la ejecucion y no logramos procesar la informacion y el dataset estaba vacio")
        return None
    
    try:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            future  = executor.submit(m_smallstatistic.f_standard_Deviation, datos)
            Avg_future = executor.submit(m_smallstatistic.f_average, datos)

            
            return future.result(), Avg_future.result()    
    except Exception as e:
        print(e)
        print(f"Error en la ejecucion de paralelismo y no logramos procesar la informacion")
        return None


def f_concurrence (ciudades):
    try:
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor() as executor:  
            future  = {executor.submit(f_download_page, ciudad):  ciudad for ciudad in ciudades}
            for future in concurrent.futures.as_completed(future):
                datos , ciudad = future.result()

                ciudad=ciudad.upper()

                if datos != None and len(datos) > 0:
                    desviacion = f_parallel(datos)
                    f_avg1 = desviacion[1]
                    print(f"La desviacion estandar de la ciudad de  {ciudad} es: {desviacion[0]}")
                    print(f"El promedio de temperatura de los ultimos diez años en la ciudad de  {ciudad} es: {f_avg1[0]}")
                    print(f"La maxima temperatura de los ultimos diez años en la ciudad de  {ciudad} es: {f_avg1[1]}")
                    print(f"La minima temperaturan de los ultimos diez años en la ciudad de  {ciudad} es: {f_avg1[2]}")
                else:
                    print(f"No teniamos datos para la ciudad {ciudad}")
             
    except Exception as e:
        print(e)
        print(f"Error en la ejecucion y no logramos procesar la informacion de la ciudad")
    
  
if __name__ == "__main__":
    ciudad =[ "mumbai","beijing","cairo","moscow","sydney","new york","tokyo","paris","london" ]
    for i in range(1000):
        resultado =  f_concurrence(ciudad)
    
    #resultado =  f_concurrence(ciudad)


