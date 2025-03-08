from drones.drones.models.commands import Take_off, Land, Forward, Turn_left, Backward, Turn_right
from drones.drones.models.quadcopter import Quadcopter




def test_recursividad_all_metodos():
    # este test tiene como proposito probar que el drone no caiga en recursividad en ningun metodo
    drone = Quadcopter("safe_drone", 0, 0, [Take_off(),  Turn_left(), Forward(5), Backward(5), Turn_right(),  Land()])
    drone.follow_commands()
   

def test_dangerous_command_sequence():
    # este test tiene como proposito probar la recursividad del metodo follow_commands 
    comand = [Take_off()]

    for _ in range(1000):  
        comand.append(Forward(1))
    comand.append(Land())
    
    drone = Quadcopter("stress_drone", 0, 0, comand)
    drone.follow_commands()  
    #vamos a enviarle muchos comandos, para saturar el dron 
    assert drone.x == 0 


def test_take_off_command():
    drone = Quadcopter("testtake", 0, 0, [Take_off()])
    command = Take_off()
    command.execute(drone)
    assert drone.direction == "N"  


# Acá estamos probando la clase Turn_left del moddulo commands.py
def test_turn_left_command():
    drone = Quadcopter("testTurnLe", 1, 0, [Turn_left()])
    command = Turn_left()
    command.execute(drone)
    assert drone.direction == "N" 


# Acá estamos probando la clase Forward del moddulo commands.py


def test_forward_command():
    drone = Quadcopter("testForward", 0, 0, [Take_off()])
    drone.follow_commands()
    command = Forward()
    command.execute(drone)
    assert drone.x == 1
    assert drone.y == 0



# Acá estamos probando la clase Backward del moddulo commands.py y nos permite hacer colisionar los drones
def test_backward_command():
    drone = Quadcopter("testBack", 2, 2, [Land()])
    drone.follow_commands()
    command = Backward()
    command.execute(drone)
    #assert drone.x == 5
    #assert drone.y == 1

# Acá estamos probando la clase Turn_right del moddulo commands.py 
def test_turn_right_command():
    drone = Quadcopter("testTurnR", 0, 0, [Turn_right()])
    drone.follow_commands()
    command = Turn_right()
    command.execute(drone)
    assert drone.direction == "N" 
    assert drone.x == 0
    assert drone.y == 0


def test_land_command():
    drone = Quadcopter("testLand", 0, 0, [Take_off(), Land()])
    drone.follow_commands()
    command = Land()
    command.execute(drone)
    assert drone.x == 0
    assert drone.y == 0
    assert drone.flying == False
    assert drone.battery == 0
    assert drone.direction == "N"
    assert drone.speed == 1
    assert drone.delta_battery == 5
    assert drone.id == "QC:testLand"
