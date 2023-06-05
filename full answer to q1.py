class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage
    
    def make_call(self, phone_number):
        print(f"Calling {phone_number}...")
    
    def receive_call(self):
        print("Receiving a call...")
    
    def take_a_picture(self):
        print("Taking a picture...")


class Apple(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage, face_id):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.face_id = face_id
    
    def unlock_with_face_id(self):
        print("Unlocking with Face ID...")


class Samsung(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage, fingerprint_sensor):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.fingerprint_sensor = fingerprint_sensor
    
    def unlock_with_fingerprint(self):
        print("Unlocking with fingerprint...")

# Creating objects of Apple class
iphone_12 = Apple("Touch Screen", "5G", False, "12MP", "48MP", "4GB", "64GB", True)
iphone_12.make_call("1234567890")
iphone_12.take_a_picture()
iphone_12.unlock_with_face_id()

# Creating objects of Samsung class
galaxy_s21 = Samsung("Touch Screen", "5G", True, "16MP", "64MP", "8GB", "128GB", True)
galaxy_s21.receive_call()
galaxy_s21.take_a_picture()
galaxy_s21.unlock_with_fingerprint()
