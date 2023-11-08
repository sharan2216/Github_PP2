def dup(str):
    dup=[]
    for i in str:
        if str.count(i)==1 and i not in dup:
            dup.append(i)

    print(dup)


str=input("enter a string")
dup(str)


