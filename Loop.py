
def isrepfun(strs):
    mydict={}
    for i in strs:
        if i in mydict:
            mydict[i]+=1
        else:
            mydict[i]=1
    flag=0;        
    for cnt in mydict.values():
        if cnt>1:
                    print("string contain repeated character")
                    flag = 1
                    break
                
                
    if(flag==0):
        print("no repeated char in string")
           
            
def main():
    strs=input("enter a string")
    isrepfun(strs)

if __name__ == "__main__":
    main()

    
    