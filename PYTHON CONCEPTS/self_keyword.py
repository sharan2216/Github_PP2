class A:
    def __init__(self,name,age,location):
        self.name=name
        self.age=age
        self.location=location
    def method1(self):
        print(f'my name is {self.name} and my age is {self.age} and my loaction is {self.location}')


obj = A("Raj",22,"Bangalore")
obj.method1()

