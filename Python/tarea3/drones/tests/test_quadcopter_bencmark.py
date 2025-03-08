
from drones.drones.models.quadcopter import Quadcopter
from drones.drones.models.commands import Take_off, Forward, Land, Turn_left, Backward, Turn_right
import pytest

@pytest.fixture

def configure_drone():
    def setup(num_commands=10000):
        commands = [Take_off()]

        for i in range(num_commands):
            commands.append(Forward(10))
        commands.append(Land())
        return Quadcopter("benchmark_drone", 0, 0, commands)
    return setup

def test_comando_ejecucion_benchmark(configure_drone, benchmark):
    drone = configure_drone(10000)
    # Ejecutar todos los comandos usando benchmark
    benchmark(drone.follow_commands)  # Asumiendo que follow_commands está en Drone
    
    
# Benchmark para lanzar la funcion get_distance_to_base() de la clase Quadcopter
def test_calcular_distancia_benchmark(configure_drone, benchmark):
    drone = configure_drone(10000)
    drone.follow_commands()
    # Medir tiempo de cálculo de distancia
    distance = benchmark(drone.get_distance_to_base)
   

# Prueba de stress, vamos a lanzar 50000 comandos
def test_prueba_performancee(configure_drone, benchmark):
    drone = configure_drone(50000)
    benchmark(drone.follow_commands)
