class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage


class Apple(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)


class Samsung(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)


# Creating objects of Apple class with different properties
iphone_12 = Apple("Touch Screen", "5G", False, "12MP", "48MP", "4GB", "64GB")
iphone_11 = Apple("Touch Screen", "4G", True, "8MP", "32MP", "3GB", "32GB")
iphone_x = Apple("Touch Screen", "4G", True, "12MP", "32MP", "4GB", "64GB")

# Creating objects of Samsung class with different properties
galaxy_s21 = Samsung("Touch Screen", "5G", True, "16MP", "64MP", "8GB", "128GB")
galaxy_s20 = Samsung("Touch Screen", "5G", False, "12MP", "48MP", "6GB", "256GB")
galaxy_a71 = Samsung("Touch Screen", "4G", True, "12MP", "32MP", "4GB", "128GB")
