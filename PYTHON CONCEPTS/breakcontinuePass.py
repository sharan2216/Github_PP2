class A:
    def meth1(self):
        for i in range(10):
            if i ==7:
                break
            print(i,end=" ")
    def meth2(self):
        for j in range(10):
            if j==7:
                continue
            print(j,end=" ")
    def meth3(self):
        for i in range(10):
            if i==7:
                pass
            print(i, end=" ")


obj=A()
obj.meth1()
print("\n")
obj.meth2()
print("\n")
obj.meth3()