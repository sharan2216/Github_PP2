# def wordreverse(str):
#     n=len(str)
#     if n==1:
#         return str
#     li=str.split()
#     size=len(li)
#     rev=" "
#     rev_all=" "
#     for i in range(size):
#         print("Value is :",i)
#         print(str[i])
#         rev=reversed(str[i])
#         # print(rev)
#         rev_all=rev_all+str(rev)+" "
#
#
# str=input("enter a string :")
# wordreverse(str)


# Reverse string
def reversestr2(str2):
    li=str2.split()[::-1]
    str3=' '.join(li)
    print(str3)


str2=input("Enter a string :")
reversestr2(str2)
print("--------------------")

def reversestr2(str22):
    li22=reversed(str22)
    str33=''.join(li22)
    print(str33)


str22=input("Enter a string :")
reversestr2(str22)






