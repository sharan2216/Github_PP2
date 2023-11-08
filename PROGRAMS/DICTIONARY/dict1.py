d1 = {575: "Apple", 876: "Mango", 132: "Grapes", 782: "Banana"}
# print(d1)
# print(d1.keys())
print(d1.items())
# d1 = sorted(d1.keys())
# print(d1)
# print("------------------")

d2 ={}
for i in d1:
    d2[i] = d1[i]

print(d2.items())
print("items values are :", d2.items())