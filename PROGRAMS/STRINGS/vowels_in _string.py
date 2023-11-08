def vowels_meth(str,vowels):
    count=0
    for ch in str:
        if ch in vowels:
            count+=1
    print("total vowels in string ",count)


vowels=['a','e','i','o','u']
str=input("enter a string : ")
vowels_meth(str,vowels)
