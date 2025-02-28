from p_smallstatistic import m_smallstatistic
import concurrent.futures
import time
import requests





def f_download_page (ciudad):
    url = f"https://weather.siel.com.co/city/{ciudad}/temp/max"
    
    headers = {
      'Content-Type': 'application/json-patch+json',
      'Accept': 'application/json-patch+json',
      'Authorization': 'Bearer secret-token-1234',
    }
    
    response = requests.request("GET", url, headers=headers, verify=False)
    responseList = response.json()
    return responseList , url


ciudad =[ "mumbai","beijing","cairo","moscow","sydney","new york","tokyo","paris","london" ]

#ciudad =['cairo']

# for i in ciudad:


#     print(f_download_page(i))


#start_time = time.time()

#ThreadPods  -- concurrencia # IO dependencias
#ProcessPool  - Paralelismo . #CPU dependiente


def f_concurre (ciudad):
    with concurrent.futures.ThreadPoolExecutor() as executor:

        for i in ciudad:
            print(i)
            future  = executor.submit(f_download_page, i)
            
            print(future.result())



        #futures = [executor.submit(f_download_page, ciudad) for ciudad in ciudad]
     
        #for future in concurrent.futures.as_completed(futures):
         #   print(future.result())
          

def __main__():
    f_concurre(ciudad)
    va = m_smallstatistic.f_standard_Deviation([10, 50, 30, 40])
    print("El valor de la desviación estandar es: " , va)



if __name__ == "__main__":
    __main__()
    