
from drones.drones.models.quadcopter import Quadcopter
from drones.drones.models.commands import  Take_off, Land, Forward, Turn_left, Backward, Turn_right

def test_estado_inicial():
    drone = Quadcopter("test_drone", 0, 0, [])
    assert drone.id == "QC:test_drone"
    assert drone.x == 0
    assert drone.y == 0
  
def test_despegue_aterrizaje():
    drone = Quadcopter("QC:test_drone", 0, 0, [Take_off(), Land()])
    drone.follow_commands()
    assert len(drone.commands) == 2  # Todos los comandos ejecutados

def test_comandos_posicion():
    drone = Quadcopter("QC:test_drone", 0, 0, [Turn_left(), Turn_right(), Forward(5), Backward(5)])
    assert drone.x == 0
    assert drone.y == 0
    drone.get_position()
   

def test_distancia():
    drone = Quadcopter("QC:test_drone", 0, 0, [Turn_left(), Turn_right(), Forward(5), Backward(5)])
    assert drone.x == 0
    assert drone.y == 0
    drone.get_distance_to_base()
