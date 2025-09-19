# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class House :
    def __init__(self):
        self.walls = None
        self.roof = None 
        self.door = None 
        self.windows = None
    
    def __str__(self):
        return f"House with {self.walls} walls, {self.roof} roof, {self.door} door(s), {self.windows} window(s)"


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self, walls):
        self.house.walls = walls
        return self

    def build_roof(self, roof):
        self.house.roof = roof
        return self

    def build_door(self, door):
        self.house.door = door
        return self

    def build_windows(self, windows):
        self.house.windows = windows
        return self

    def get_result(self):
        return self.house


Builder = HouseBuilder().build_walls(10).build_roof(3).build_door(4).build_windows(20).get_result()
print(Builder)




class Computer:
    """The product class that we want to build"""
    
    def __init__(self):
        self.ram = None
        self.hdd = None
        self.cpu = None
        self.gpu = None
        self.bluetooth = False
        self.wifi = False
    
    def __str__(self):
        return (f"Computer: RAM={self.ram}GB, HDD={self.hdd}GB, CPU={self.cpu}, "
                f"GPU={self.gpu}, Bluetooth={self.bluetooth}, WiFi={self.wifi}")


class ComputerBuilder:
    """The builder class that constructs the Computer object"""
    
    def __init__(self):
        self.computer = Computer()
    
    def set_ram(self, ram):
        self.computer.ram = ram
        return self
    
    def set_hdd(self, hdd):
        self.computer.hdd = hdd
        return self
    
    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self
    
    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self
    
    def enable_bluetooth(self):
        self.computer.bluetooth = True
        return self
    
    def enable_wifi(self):
        self.computer.wifi = True
        return self
    
    def build(self):
        # Validate the configuration if needed
        if self.computer.ram is None or self.computer.hdd is None or self.computer.cpu is None:
            raise ValueError("Computer must have RAM, HDD, and CPU")
        return self.computer


# Director (optional) - can be used to define common configurations
class Director:
    """Optional director that defines common computer configurations"""
    
    @staticmethod
    def build_gaming_computer(builder):
        return (builder.set_ram(32)
                .set_hdd(2000)
                .set_cpu("Intel i9")
                .set_gpu("NVIDIA RTX 3080")
                .enable_wifi()
                .enable_bluetooth()
                .build())
    
    @staticmethod
    def build_office_computer(builder):
        return (builder.set_ram(16)
                .set_hdd(500)
                .set_cpu("Intel i5")
                .enable_wifi()
                .build())


# Client code
if __name__ == "__main__":
    # Using the builder directly
    builder = ComputerBuilder()
    custom_computer = (builder.set_ram(16)
                      .set_hdd(1000)
                      .set_cpu("AMD Ryzen 7")
                      .set_gpu("NVIDIA GTX 1660")
                      .enable_wifi()
                      .build())
    
    print("Custom Computer:")
    print(custom_computer)
    print()
    
    # Using the director for predefined configurations
    builder2 = ComputerBuilder()
    gaming_computer = Director.build_gaming_computer(builder2)
    
    print("Gaming Computer:")
    print(gaming_computer)
    print()
    
    builder3 = ComputerBuilder()
    office_computer = Director.build_office_computer(builder3)
    
    print("Office Computer:")
    print(office_computer)