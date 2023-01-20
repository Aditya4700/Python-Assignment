from collections import Counter
def count(lst):
    yield Counter(lst)

lst=[1,2,3,1,2,3,5,6]
for i in count(lst):
    print(i)

