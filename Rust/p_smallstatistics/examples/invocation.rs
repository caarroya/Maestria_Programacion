use p_smallstatistics::f_media;
use p_smallstatistics::f_median;
use p_smallstatistics::f_standard_desviation;



fn main() {
    let datos = vec![10.0, 70.0, 40.0, 30.0, 50.0, 60.0, 20.0, 80.0, 100.0 , 110.0 ];
    //let datos = vec![];
    if datos.is_empty() {
        panic!("El arreglo de datos no puede estar vacío.");
    }
    
    let media = f_media(&datos);
    println!("El valor de la media es {}", media);  

    let mediana = f_median(&datos);
    println!("El valor de la mediana es {}", mediana);  

    // Desviación estándar poblacional se invoca la funcion pasando 
    let desviacion_poblacional = f_standard_desviation(&datos, false);
    println!("Este es el valor de la desviación poblacional {}", desviacion_poblacional);
        
        // Desviación estándar muestral
    let desviacion_muestral = f_standard_desviation(&datos, true);
    println!("El valor de la desviación muestral es : {} ", desviacion_muestral);
    
}