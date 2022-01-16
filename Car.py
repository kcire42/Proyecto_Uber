from Account import Account

class Car:
    def __init__(self,id,license,driver,passenger,color):
        self.__id = id
        self.__license = license
        self.__driver = Account(id,license)
        self.__passenger = passenger
        self.__color = color





       
