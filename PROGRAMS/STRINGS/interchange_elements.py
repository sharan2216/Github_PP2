def interchange(list):
    n=len(list)
    list[0],list[n-1]=list[-1],list[0]
    print(list)

list=[1,2,3,4,5]
interchange(list)

