from Car import Car

class UberPool(Car):

    def __init__(self,id,license,driver,passenger,color,brand,model):
        super.__init__(id,license,driver,passenger,color)
        self.__brand = brand
        self.__model = model