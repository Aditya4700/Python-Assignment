#[1, 0], [1, 2], [6, 3], [1, “a”]

# x=1/0

# print (x) #ZeroDivisionError

# x=1/2

# print(x)

# 
# x=1/'a'

# print (x)   #TypeError

def devision(*args):
        for i in range(0,4):
             try:
                result = args[i][0]/args[i][1]
                print(result)
             except ZeroDivisionError:
                 print("Error: Denominator cannot be 0.")
             except TypeError:
                 print("Error: Denominator cannot be character.")



devision((1, 0),(1, 2),(6, 3),(1, 'a'))
