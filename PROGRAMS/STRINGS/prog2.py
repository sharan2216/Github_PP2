# word frequency
# str4 = input("enter a string :")
# li1=str4.split()
# print(li1)
# d={}
# for i in li1:
#     if i not in d.keys():
#         d[i]=0
#     d[i]=d[i]+1
# print(d)
#

# letter frequency
# def meth(str):
#     d={}
#     for i in str:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     print(d)
#
#
# str = input("enter a string :")
# meth(str)



#abaabab2ab34b1a
# def meth2(str):
#     n=len(str)
#     count=1
#     newstr = " "
#     for i in range(n-1):
#         if str[i]==str[i+1]:
#             count=count+1
#         else:
#             newstr=newstr+str[i]+str(count)
#             count=1
#     return newstr
#
# str = input("enter a string")
# print(meth2(str))
#
# def method3(str):
#     # str=str.split()
#     # print(str)
#     count=1
#     char=input("enter a char to be searched:")
#     if char  in str:
#         count=count+1
#     else:
#         count=1
#
#     print(count)
#
#
# str=input("enter a string")
# method3(str)
#
str="shashi"
count=0
n=len(str)
char=input("enter a char : ")
for i in range(n):
    if char.__eq__(str[i]):
        count=count+1
    else:
        count=1

print(count)