import time
def retry(func):
    def inner():
        
        
        print("try 1")
        time.sleep(3) 
            
    for i in range(0,3):
        inner()
        
       
@retry        
def fun():
    print("hii")
