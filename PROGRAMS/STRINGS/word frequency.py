def wordfrequency(str):
    d={}
    # li=str.split()
    for i in str:
        if i not in d.keys():
            d[i]=0
        d[i]+=1

    print(d)


str=input("enter a string :")
wordfrequency(str)



