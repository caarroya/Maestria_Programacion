
from abc import ABC, abstractmethod


class Drone(ABC):
    # position of the drone
    def __init__(self, id, x, y, commands):
        self.id = id
        self.x = x
        self.y = y
        self.battery = 100
        self.delta_battery = 5
        self.speed = 1
        self.direction = "N"
        self.flying = False
        self.commands = commands
    
    @abstractmethod
    def execute(self, command):
        pass

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def get_distance_to_base(self):
        pass

    @abstractmethod
    def report(self, message):
        pass

    def consume_battery(self):
        self.battery -= self.delta_battery
        if self.battery < 0:
            self.battery = 0
            self.report("Battery empty - landing")
            return True
        return False

    def follow_commands(self):
        for command in self.commands:
            self.execute(command)
            if self.battery == 0:
                self.report("Battery empty - landing")
                return
        self.report("Sequence completed - repeating")
        self.follow_commands()



   