def count(list):
    j=0
    for i in list:
        j+=1
    yield j


list=[1,2,3,4,7]
for i in count(list):
    print(i)