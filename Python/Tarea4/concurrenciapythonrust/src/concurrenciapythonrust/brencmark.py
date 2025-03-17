from concurrenciapythonrustr import procesar_temperaturas
from concurrenciapythonrust.main import f_concurrence, f_download_page
import concurrent.futures
import time
import requests
import statistics
import json
from functools import wraps
from datetime import datetime


def f_concurrence_benchmark(ciudades):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futuros = {executor.submit(f_download_page, ciudad): ciudad for ciudad in ciudades}
        
        for futuro in concurrent.futures.as_completed(futuros):
            start_request = time.time()
            
            try:
                data_str, ciudad = futuro.result()
                request_time = time.time() - start_request
               
                
                if data_str:
                    data_str_t = str(data_str).replace('[','').replace(']','')
                    datos_rust = [(ciudad, data_str_t)]
                    
                    rust_start = time.time()
                    try:
                        resultado = procesar_temperaturas(datos_rust)
                        rust_time = time.time() - rust_start
                        print(f"n\CiudadProcesada: {ciudad}")
                        print(f"El tiempo que inicial es {start_request} para la ciudad: {ciudad} finalizó {rust_time}")
                    except Exception as e:
                        print(f"Errores en la invocacion de Rust: {str(e)}")
                else:
                    print(f"Datos invalidos para la ciudad : {ciudad}")
                    
            except Exception as e:
                request_time = time.time() - start_request
             
                print(f"request fallido: {ciudad} - {str(e)}")
    
    return rust_start , rust_time




def ejecutar_benchmark(ciudades,  benchmark_runs):
   
    # Main benchmark
    print("\nStarting benchmark...")
    all_results = []
    for i in range(benchmark_runs):
        print(f"\nBenchmark run {i+1}/{benchmark_runs}")
        start_time , end_start =  f_concurrence_benchmark(ciudades)
       
        
    

if __name__ == "__main__":
    ciudades =[ "mumbai","beijing","cairo","moscow","sydney","new york","tokyo","paris","london" ]
    iterations= 10
    ejecutar_benchmark (ciudades , iterations)
