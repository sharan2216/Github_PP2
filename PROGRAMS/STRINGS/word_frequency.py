def meth(str):
    list=str.split()
    # print(list)
    d={}
    for i in list:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print(d)

str=input("enter a string ")
meth(str)
#letter frequency-------------------------------
def meth2(str):

    # print(list)
    d={}
    for i in str:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print(d)

str=input("enter a string ")
meth2(str)