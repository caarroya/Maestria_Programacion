use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;
use rayon::prelude::*;

/// Desc: Función para calcular el promedio (versión compatible con PyO3)
/// Arg:  Recibe un vector de datos numericos, para calcularle el promedio 
/// Err: Hace control de error cuando recibe valores no numericos, vacios 
/// Autor: Carlos Arroyave
fn promedio(datos: &[f64]) -> Result<f64, PyErr> {
    if datos.is_empty() {
        return Err(PyValueError::new_err("Lista de temperaturas vacía"));
    }
    let suma: f64 = datos.iter().sum();
    Ok(suma / datos.len() as f64)
}

/// Desc: Función para calcular la desviación estándar (versión compatible con PyO3)
/// Arg:  Recibe un vector de datos numericos, para calcularle la desviación estandar  
/// Err: Hace control de error cuando recibe valores no numericos, vacios 
/// Invo :  Invoca la función promedio para calcular un valor dentro de la misma funcion
/// Autor: Carlos Arroyave
fn desviacion_estandar(datos: &[f64], promedio: f64) -> Result<f64, PyErr> {
    let varianza: f64 = datos
        .iter()
        .map(|&x| (x - promedio).powi(2))
        .sum::<f64>() 
        / datos.len() as f64;
    
    Ok(varianza.sqrt())
}

/// Desc : Función encarga de someter de manera paralela el calculo de temperaturas para cada ciudad
/// Arg: Recibe como parametros un vector de dos posiciones, prosicion uno :Nombre Ciudad , posición dos : Datos de temperatura
/// Err: manejo de errores cuando el vector no contiene datos
///Invo : Invoca dos funciones adiconales :  Promedio y Desviación Estandar, adiciona
/// Adicional se comporta como una pyfunction, para integrarse con python
/// Autor: Carlos Arroyave
#[pyfunction]
pub fn procesar_temperaturas(data: Vec<(String, String)>) -> PyResult<Vec<(String, f64, f64)>> {
    data.into_par_iter()
        .map(|(city_id, temp_str)| {  
            // Parsear la cadena de temperaturas a Vec<f64>
            let temps: Vec<f64> = temp_str
                .split(',')
                .map(|s| s.trim().parse::<f64>()
                    .map_err(|e| PyValueError::new_err(format!("Error parseando número: {}", e)))
                )
                .collect::<Result<Vec<_>, _>>()?;
            
            // Validar lista no vacía
            if temps.is_empty() {
                return Err(PyValueError::new_err(format!(
                    "No hay temperaturas para la ciudad {}",
                    city_id
                )));
            }
            
            // Calcular estadísticas
            let avg = promedio(&temps)?;
            let std_dev = desviacion_estandar(&temps, avg)?;
            
            // Convertir ID de ciudad a String
            Ok((city_id.to_string(), avg, std_dev))
        })
        .collect()
}


/// Desc : Modulo  encargado  de someter de manera paralela el calculo de temperaturas para cada ciudad
/// Arg: N/A
/// Err: N/A
/// Invo : Invoca el pyFunction 
/// Autor: Carlos Arroyave


#[pymodule]
fn concurrenciapythonrustr(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(procesar_temperaturas, m)?)?;
    Ok(())
}


/// La siguiente  corresponde a las funciones para hacer el test del  modulo. 

#[cfg(test)]
mod tests {
    use super::*;
    use approx::assert_relative_eq;

    #[test]
    fn test_calculos_basicos() {
        let datos = vec![1.0, 2.0, 3.0, 4.0, 5.0];
        let (prom) = promedio(&datos).unwrap();
        let (dev) = desviacion_estandar(&datos,  prom).unwrap();

        
        assert_relative_eq!(prom, 3.0, epsilon = 1e-4);
        assert_relative_eq!(dev, (2.0_f64).sqrt(), epsilon = 1e-4);
    }

    #[test]
    fn test_lista_vacia() {
        let datos = vec![];
        let resultado = promedio(&datos);
        assert!(resultado.is_err());
    }

    #[test]
    fn test_un_elemento() {
        let datos = vec![5.0];
        let (prom) = promedio(&datos).unwrap();
        let (dev) = desviacion_estandar(&datos,  prom).unwrap();

        assert_relative_eq!(prom, 5.0);
        assert_relative_eq!(dev, 0.0);
    }
}