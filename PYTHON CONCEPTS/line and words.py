file=open("C:\\Users\\shashi\\Desktop\\abc.txt")
data=file.read()
lines=data.split("\n")
for line in lines:
    words=line.split(" ")
    for word in words:
        print(word)
