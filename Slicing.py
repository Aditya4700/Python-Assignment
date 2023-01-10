
def slice(list1,a,b):
    print(list1[(a-1):(b)])


def main():
    list1=[]
    n = int(input("Enter number of elements : "))
  
# iterating till the range
    for i in range(0, n):
        ele = int(input())
  
        list1.append(ele)
    a=int(input("inter start index"))
    b=int(input("inter end index"))
    slice(list1,a,b)


if __name__ == "__main__":
    main()
