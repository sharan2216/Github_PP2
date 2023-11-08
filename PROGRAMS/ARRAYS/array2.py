# 1. Write a Python program to create an array of 5 integers and display the array items.
# Access individual elements through indexes.
from numpy import *
from array import *
arr1=array('i',[1,3,5,7,9])
# for i in arr1:
#     print(i)
# 1. Write a Python program to create an array of 5 integers and display the array items.
# Access individual elements through indexes.
from numpy import *
from array import *
arr1 = array('i',[1,3,5,7,9])
# for i in arr1:
#     print(i,end=' ')
# print("Access first three items individually")
# print(arr1[0])
# print(arr1[1])
# print(arr1[2])

# 2. Write a Python program to append a new item to the end of the array.
# Sample Output:
# arr1.append(11)
# for i in arr1:
#     print(i,end=' ')
# # 3. Write a Python program to reverse the order of the items in the array.
# # Sample Output
# print("\n3rd Program------------")
# arr1.reverse()
# for i in arr1:
#     print(i,end=' ')
#
# # 6. Write a Python program to get the number of occurrences of a specified element in an array.
# arr2 = array('i',[1,3,5,7,9,3,1])
# print("\n6th Program------------")
# count=0
# for i in arr2:
#     if i==1:
#         count=count+1
# print(count)
#
# # 7.Write a Python program to append items from iterable to the end of the array.
# arr3 = array('i',[9,8,7,6])
# print("\n7th Program------------")
# arr1.extend(arr3)
# for i in arr1:
#     print(i,end=" ")

# 10. Write a Python program to insert a newly created item before the second element in an existing array.
# Sample Output:
print("\n10th Program------------")
print(arr1)
arr1.insert(1,4)
for i in arr1:
    print(i,end=' ')
print("\n POP Program------------removes element at specified position")
print(arr1)
arr1.pop(1)
print(arr1)

# 12. Write a Python program to remove the first occurrence of a specified element from an array.
# Sample Output:
arr12 = array('i',[1,3,5,7,9,3,])
print("\n12th Program------------removes first occurrence of a specified position")
print(arr12)
arr12.remove(3)
print(arr12)