# def recursion(n):
#     if n==0:
#         return
#     print(n)
#     return recursion(n-1)
#
# n=int(input("eneter a number :"))
# print(recursion(n))
count=1
def meth(name):
    global count
    if count<=10:
        print(name ,count)
        count=count+1
        meth(name)
name=input("enter a name : ")
meth(name)
