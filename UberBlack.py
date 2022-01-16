from Car import  Car

class UberBlack(Car):

    def __init__(self,id,license,driver,passenger,color,Type_car,Type_Seat):
        super.__init__(id,license,driver,passenger,color)
        self.__Type_Car = Type_car = []
        self.__Type_Seat = Type_Seat = []
