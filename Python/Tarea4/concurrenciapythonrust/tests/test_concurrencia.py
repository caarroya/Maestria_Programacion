import pytest
from unittest.mock import Mock, patch
from concurrenciapythonrustr import procesar_temperaturas
from src.concurrenciapythonrust.main import f_concurrence,f_download_page
import requests


#Se utilizará un mock para dos ciudades y hacer las pruebas unitarias
@pytest.fixture
def mock_ciudades():
    return ["beijing", "london"]

# Pruebas para simular la descarga existosa, para ello usaremos mocks
@patch('requests.get')
def test_descarga_existosa(mock_get, monkeypatch):
    """Prueba una descarga exitosa"""
    # Configurar mock
    mock_response = Mock()
    mock_response.json.return_value = [25.5, 30.0]
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    # Ejecutar
    data, ciudad = f_download_page("beijing")
    
    # Verificar
    assert ciudad == "beijing"
    assert data == [25.5, 30.0] * 10
    mock_get.assert_called_once_with(
        "https://weather.siel.com.co/city/beijing/temp/max",
        headers={'Authorization': 'Bearer secret-token-1234'},
        verify=False,
        timeout=10
    )

@patch('requests.get')
def test_descarga_fallida(mock_get):
    """Prueba manejo de errores HTTP"""
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
    mock_get.return_value = mock_response

    data, ciudad = f_download_page("unknown_city")
    
    assert ciudad == "unknown_city"
    assert data is None

# Prueba de transformación de datos

def test_promedio_datos():
    """Prueba la conversión de datos para Rust"""
    raw_data = ['beijing' , [30.0, 30.0]] 
    expected_output = ('beijing' , 30.0, 0 )
    
    data_str, ciudad = f_download_page("beijing")
    data_str_t = str(data_str).replace('[','').replace(']','')
    
    assert data_str_t == expected_output

# Ejecutar pruebas
if __name__ == "__main__":
    pytest.main(["-v", "--cov=your_module", "--cov-report=html"])