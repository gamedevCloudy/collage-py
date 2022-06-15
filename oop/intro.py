#inheritance --> creawting a new class by using properties of old class

"""
Type: 
    1. Single - base -> new class
    2. Multiple- base1 + base2 -> class 
    3. Multilevel - base -> cl1->cl2
    4. Hierarchial -base > c1 + c2
"""

#Single Inheritance

class first:
    def add(self, a,b):
        c = a+b
        print(c)

obj = first()
obj.add(5,6)

class second(first):
    def sub(self, c,d):
        f = c-d
        print(f)

obj1 = second()
obj1.sub(10,5)

obj1.add(10,5) #add is function inherited from first class

#end single inheritance
