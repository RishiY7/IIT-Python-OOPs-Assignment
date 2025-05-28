class Device:
    def __init__(self,model_no,place_of_origin):
        self.model_no=model_no
        self.place_of_origin=place_of_origin

    def base_info(self):
        print(f"model no : {self.model_no} , manufactured in :{self.place_of_origin}")


class Flyer:
    def fly(self):
        print("Drone flight simulation \n")

class Drone(Flyer,Device):
    def __init__(self, model_no, place_of_origin):
        super().__init__(model_no, place_of_origin)
    
    def capture_image(self):
        print("Image capturing on \n")
    
    def current_status(self,flight):
        super().base_info()
        if flight:
            super().fly()
        else:
            print("drone on ground \n")

d1=Drone("CD040",'INDIA')
d1.current_status(1)
d1.capture_image()