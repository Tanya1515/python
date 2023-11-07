#OOP
#type() - returns type of the object
#__dict__ - atributes for class

#attributes of class is not attribute of object
class A:
    CLASS_ATR = 0
    __slots__ = ['_a', '__b']
    def __init__(self, a):
        self._a = a
        self.__b = b #__ - must not be changed
    
    @staticmethod #is udes for incapsulation
    def foo(): 
       return A(0, 0)
    
    def bar(cls):  
        return cls.__name__
    
    #property is made for all this methods 
    def set_a (self, a):
        self._a = a

    def get_a(self):
        return self._a

    def del_a (self):
        del self._a


    
#Add 15 as a parameter for object a
a = A(15, 5)

#type of the a 
type(a)

#methods for the object
dir(a)









