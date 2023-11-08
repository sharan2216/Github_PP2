def alphanum(str):
    list_alpha=[]
    list_numeric=[]
    for ch in str:
        if ch.isalpha():
            list_alpha.append(ch)
        elif ch.isdigit():
            list_numeric.append(ch)
    print(list_alpha)
    print(list_numeric)
    list3=list_alpha+list_numeric
    print(''.join(list3))

str=input("enter a string :")
alphanum(str)



