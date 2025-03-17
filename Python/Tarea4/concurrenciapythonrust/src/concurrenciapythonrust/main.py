from concurrenciapythonrustr import procesar_temperaturas  # Nombre correcto del módulo
import concurrent.futures
import time
import requests


def f_download_page(ciudad):
    
    '''
    Desc:  Funcion encargada de conectarse a la API y descargar una respuesta
    Arg: Recibe un vector con las ciudades a procesar
    Err : Realiza control de excepciones, cuando el api no da respuesta, captura error
    Return: Retonar la ciuidad y temperaturas en un vector
    Autor: Carlos Arroyave
    
    '''


    url = f"https://weather.siel.com.co/city/{ciudad}/temp/max"
    
    headers = {'Authorization': 'Bearer secret-token-1234'}
    
    try:
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        response.raise_for_status()
        response_data = response.json() *10
        return response_data, ciudad
    
    except Exception as e:
        print(f"Error en {ciudad}: {str(e)}")
        return None, ciudad

def f_concurrence(ciudades):
    '''
    Desc:   Funcion encargada de someter la concurrencia el API de temperatura
    Arg:    Recibe un vector con las ciudades a procesar
    Err :   Realiza control de excepciones, cuando el api no da respuesta, captura error
    Return: Retorna un vector con la ciudad , promedio y desviación estandar
    Autor:  Carlos Arroyave
    
    '''
    
    resultados = []
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futuros = {executor.submit(f_download_page, ciudad): ciudad for ciudad in ciudades}
        
        for futuro in concurrent.futures.as_completed(futuros):
            data_str, ciudad = futuro.result()
            
            
            if data_str :
               
                # Construir estructura que Rust espera: Vec<(f64, String)>, para ello vamos a eliminar los caracteres [] , puesto que convertimos la variable en un string
                data_str_t= str(data_str).replace('[','').replace(']','')
                datos_rust = [(ciudad, data_str_t)]  # Lista de tuplas
                
                
                try:
                    # Se hace el llamado función construidad en rust
                    resultado = procesar_temperaturas(datos_rust)
                    if resultado:
                        print(f"\nLa Ciudad es: {ciudad}")
                        print(f"Y su Promedio y Desviación Estandar son : {resultado[0]}")
                except Exception as e:
                    print(f"Error en Rust para {ciudad}: {str(e)}")
            else:
                print(f"Datos inválidos para {ciudad}")
    
    return resultados

if __name__ == "__main__":
    ciudades =[ "mumbai","beijing","cairo","moscow","sydney","new york","tokyo","paris","london" ]
    f_concurrence(ciudades)