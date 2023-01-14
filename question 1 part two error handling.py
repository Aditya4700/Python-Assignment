#[1, 0], [1, 2], [6, 3], [1, “a”]

# x=1/0

# print (x) #ZeroDivisionError

# x=1/2

# print(x)

# 
# x=1/'a'

# print (x)   #TypeError

def devision(num,deno):
    try:
        
        result = num/deno

        print(result)
    except ZeroDivisionError:
        print("Error: Denominator cannot be 0.")
    except TypeError:
        print("Error: Denominator cannot be character.")



devision(1, 0)
devision(1, 2)
devision(6, 3)
devision(1, 'a')
