def list_to_dict():
    key=[1111,2222,3333,4444]
    value=['hi','how','are','you']
    result=dict(zip(key,value))
    print(result)

list_to_dict()

def dict_to_tup():
    d={1111: 'hi', 2222: 'how', 3333: 'are', 4444: 'you'}
    print(d.keys())
    print(d.values())
    for i in d.items():
        print(i)

dict_to_tup()



