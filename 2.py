# by using filter function
lst = [1, "a", 2, "b", 3, "c"]
digits = list(filter(lambda x: isinstance(x, int), lst))
alphabets = list(filter(lambda x: isinstance(x, str), lst))
print(digits)
print(alphabets)

#by using comprehension
digits = [x for x in lst if isinstance(x, int)]
alphabets = [x for x in lst if isinstance(x, str)]

print(digits)
print(alphabets)

#by using map

map_1={}
x=0
for i in range(0,len(lst)):
    
    if(isinstance(lst[i], int)):
        map_1[x]=lst[i]
        x+=1;
        

map_2={}
x=0
for i in range(0,len(lst)):
    
    if(isinstance(lst[i], str)):
        map_2[x]=lst[i]
        x+=1;

print(map_1)                
print(map_2)                