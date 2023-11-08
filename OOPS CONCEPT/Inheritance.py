class A:
    x=10
    print(x)
    def method1():
        print("Method1 gets called")

class B(A):
    y=20
    print(y)
    def method2():
        print("Method2 gets called")

obj=B
obj.method2()
obj.method1()