# arr=[1,4,2,5,2,1,5]
# arr2=set(arr)
# arr3=list(set(arr))
# arr44=list(arr)
# print(arr2)
# print(arr3)
# print(arr44)
print("-------------------")
arr=[1,4,2,5,2,1,5]
arr2=[]
count=0
for i in arr:
    if i not in arr2:
        arr2.append(i)
        count=count+1

print(arr2)
print(count)