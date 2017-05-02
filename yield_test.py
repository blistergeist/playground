def createGenerator():
    myList = range(5)
    for i in myList:
        yield i*i
        print('garbage')


myGen = createGenerator()
for i in myGen:
    # print(i)
    pass