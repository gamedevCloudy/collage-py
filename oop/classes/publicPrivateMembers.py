class Student:
    def __init__(self, r,n):
        self.r = r #public variables
        self.n = n
    def disp(self):
        print(self.r, self.n)

obj = Student(609, "Banana")
obj.disp()


class emp:
    def __init__(self, r, n):
        self.__r = r #private "__" variable
        self.__n = n

obj1 = emp(89,"kela")
print(obj1._emp__r ) # access--> object_name._classname__variable


#public private and protected

class empl:
    public = 10
    _protected = 20
    __private = 30


e1 = empl()

print(e1.public)
print(e1._protected) #access --> obj_name._varaiable
print(e1._empl__private)
