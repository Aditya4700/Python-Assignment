
def add():
    {
    print(a+b)
    }
def subtract():
    {
        print(a-b)
    }
def multiply():
    {
        
     print(a*b)
    }
def divide():
    {
        
       print(a/b)
    }
a=int(input("Enter 2 Nums.\n"))
b=int(input())
c=input("inter operation like add,subtract,multiply,divide\n")
match c:
        case 'add':
            add()    
        case 'subtract':
            subtract()
        case 'multiply':
            multiply()
        case 'divide':
            divide()    