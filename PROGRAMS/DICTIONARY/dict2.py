def meth(mydict1):
    list1 = []
    for i in mydict1:
        list1.append(mydict1[i])
        print(list1)
        result = sum(list1)
    return result



mydict1={'a': 10, 'b': 9, 'c': 15, 'd': 2, 'e': 32}
print("sum is :",meth(mydict1))