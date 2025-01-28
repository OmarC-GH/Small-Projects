#########Omar Cooper
##### "Car" Object Oriented Small Project


### This program will create car objects and simulate them accelerating and deaccelerating

class Car:
    #### Define whats "in it"
    def __init__(self, year_model, make):
        ### Set the set version = to basic value version
        # DONT FORGET DOUBLE UNDERSCORES
        self.__year_model = year_model                      #### format is "self.__"
        self.__make = make 
        self.__speed = 0

    # Define set functions for each parameter
    def set_year_model(self, year_model):                  #### Don't forget colon after every function def
        self.__year_model = year_model
    def set_make(self, make):
        self.__make = make  
    def set_speed(self, speed):
        self.__speed = speed

    # Define get functions for each parameter
    def get_year_model(self):                               ## Only self parameter is needed in get functions
        return self.__year_model
    def get_make(self):
        return self.__make
    def get_speed(self):
        return self.__speed
    
    ## Define acceleration and brake
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    
### Define main
def main():
    # To create object use classic assignent operators
    car1 = Car("2013", "Dodge")

    # To call function on object use "object.function()"
    for x in range (5):
        car1.accelerate()
        print (f"The car's speed after accelerating {car1.get_speed()} miles per hour.")
    
    for x in range (5):                            
        car1.brake()
        print (f"The car's speed after braking {car1.get_speed()} miles per hour.")

### Test with main
if __name__ == "__main__":          ### Must use quotations around "__main__"
    main()
