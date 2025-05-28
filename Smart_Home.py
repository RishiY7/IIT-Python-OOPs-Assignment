# Smart Home Appliance
    
class Appliance:
    def status(self,is_on):
        if(is_on):
            print("default message: appliance is ON")
        else:
            print("off")

class Fan(Appliance):
    def status(self,is_on):
        if(is_on):
            print("fan is spinning ")
        else:
            print("off")

class Light(Appliance):
   def status(self,is_on):
        if(is_on):
            print("Light's ON")
        else:
            print("off")

class AC(Appliance):
    def status(self,is_on):
        if(is_on):
            print("AC is ON ")
        else:
            print("off")
        

fan1=Fan()
light1=Light()
ac1=AC()
appliance_list=[fan1,light1,ac1]
for i in appliance_list:
    i.status(1)