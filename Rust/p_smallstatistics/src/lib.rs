
pub fn f_media(datos: &[f64]) -> f64 {
    let v_lengths = datos.len() as f64;
    datos.iter().sum::<f64>() / v_lengths
}

pub fn f_variance(datos: &[f64], es_muestra: bool) -> f64 {
    let media = f_media(datos);
    let v_lengths = datos.len() as f64;
    
    let suma_cuadrados: f64 = datos.iter()
        .map(|&x| (x - media).powi(2))
        .sum();
    
    if es_muestra {
        suma_cuadrados / (v_lengths - 1.0)
    } else {
        suma_cuadrados / v_lengths
    }
}




pub fn f_median(datos: &[f64]) -> f64 {
    
    // Se ordenan los datos para calcula la media
    let mut data_sort = datos.to_vec(); // Creamos una copia mutable
    data_sort.sort_by(|a, b| a.partial_cmp(b).unwrap()); // Ordenamos

    let v_length = data_sort.len();

    // Calculamos la mediana
    if v_length % 2 == 1 {
        // Si la longitud es impar, la mediana es el valor central
        let pos = v_length / 2;
        data_sort[pos]
    } else {
        // Si la longitud es par, la mediana es el promedio de los dos valores centrales
        let pos1 = v_length / 2 - 1;
        let pos2 = v_length / 2;
        (data_sort[pos1] + data_sort[pos2]) / 2.0
    }
}


pub fn f_standard_desviation(datos: &[f64], es_muestra: bool) -> f64 {
    f_variance(datos, es_muestra).sqrt()
}
