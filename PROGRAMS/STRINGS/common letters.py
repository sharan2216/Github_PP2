#common letters-------------
def common(str1,str2):
    li=[]
    for i in str1:
        for j in str2:
            if i==j and i not in li:
                li.append(i)
    print(li)


str1=input(("enter a string :"))
str2=input("enter a string : ")
common(str1,str2)


#common didgits--------

def commondigits(l1,l2):
    li2=[]
    count=0
    for i in l1:
        for j in l2:
            if i==j and i not in li2:
                li2.append(i)
                count+=1
    print("common elements are :",li2)
    print("total common elements in both lists are :",count)

l1=[2,4,6,8,10,12,14,9]
l2=[3,6,9,12,15,18,6]

commondigits(l1,l2)

