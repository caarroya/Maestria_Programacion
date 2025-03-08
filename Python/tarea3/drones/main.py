from drones.models.quadcopter import Quadcopter
from drones.models.commands import Forward, Backward, Turn_left, Take_off, Land, Turn_right


def main():
    drones = []
    drones.append(Quadcopter("raptor", 0, 0, [Take_off(), Forward(5), Turn_left(), Forward(5), Turn_left(), Forward(5), Turn_left(), Forward(5), Turn_left(), Backward(5), Turn_right(), Forward(5), Turn_right(), Forward(5), Turn_right(), Forward(5), Turn_right(), Backward(5), Land()]))
    for drone in drones:
        drone.follow_commands()


if __name__ == "__main__":

    main()
