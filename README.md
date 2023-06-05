
QUESTION ONE
1. Create inheritance using MobilePhone as base class and Apple & Samsung
as child class
1. The base class should have properties:
1. ScreenType = Touch Screen
2. NetworkType = 4G/5G
3. DualSim = True or False
4. FrontCamera = (5MP/8MP/12MP/16MP)
5. rearCamera = (8MP/12MP/16MP/32MP/48MP)
6. RAM = (2GB/3GB/4GB)
7. Storage = (16GB/32GB/64GB)
2. Create basic mobile phone functionalities in the classes like:
make_call, recieve_call, take_a_picture, etc.
3. Use super() constructor for calling parent class’s constructor
4. Make some objects of Apple class with different properties
5. Make some objects of Samsung class with different properties
 [39 Marks]
3 | P a g e
SECTION B
QUESTION TWO
What is the output of the following code:
class BMW:
 def __init__(self, name, model, year):
 self.name = name
 self.model = model
 self.year = year
 def start(self):
 print("Starting the car ...")
 def stop(self):
 print("Stopping the car ...")
 def drive(self):
 pass
class ThreeClass(BMW):
 def __init__(self, CuriseAssistEnabled, name, model, year):
 BMW.__init__(self, name, model, year)
 self.CuriseAssistEnabled = CuriseAssistEnabled
 def display(self):
 print(self.CuriseAssistEnabled)
 def drive(self):
 print("Three Class is being driven..")
threeClass = ThreeClass(True, "BMW", "328i", 2018)
print(
 threeClass.CuriseAssistEnabled,
 threeClass.name,
 threeClass.model,
 threeClass.year
