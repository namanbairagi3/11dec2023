class MyParent(): # Base Class
    #1.1 Property
    bloodGroup='+Bve'

    #1.2 constructor


    #1.3 Method


class MyChild(MyParent): # derived class
    #1.1 Property

    #1.2 constructor


    #1.3 Method
    def getMyBloodGroup(self):
        print(f'My Blood group is {self.bloodGroup}')

# Create Class Object
# WE always create object of child class
co = MyChild()
co.getMyBloodGroup()