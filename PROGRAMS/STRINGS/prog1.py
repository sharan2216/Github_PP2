# str="sky is blue"
# l=str.split()
# print(l)
# print("----------------")
# print(l[::-1])
# l2=l[::-1]
# l3=' '.join(l2)
# print(l3)

# str2="my name is kant"
# li1=str2.split()[::-1]
# print(li1)
# li2=[]
# for i in li1:
#     li2.append(i)
# print(li2)
# li3=' '.join(li2)
# print(li3)


# # vowels
# str3="aaioofgghhrrttuufaeioud"
# v=['a','e','i','o','u']
# count=0
# for i in str3:
#     if i in v:
#         count=count+1
#
# print(count)

# # Reverse a string
#
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

#string Aplhabet
str7="B7HAA123"
alphabet=[]
numbers=[]
count=0
for i in str7:
    if i.isalpha():
        alphabet.append(i)
    else:
        numbers.append(i)
print(alphabet)
print("-------------")
sort_alpha=sorted(alphabet)
l11=' '.join(sort_alpha)
print(l11)
print("-------------")
print(numbers)
sorted_num=sorted(numbers)
l22=' '.join(sorted_num)
print(l22)
print(l11)
print(l11 + l22)



