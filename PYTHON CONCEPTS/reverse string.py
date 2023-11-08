def revstring(str):
    n=len(str)
    str2=str.split()
    print("str2 is : ",str2)
    for i in range(1,n):
        rev=reversed(str2[i])
    print(rev)


str="python is easy"
revstring(str)