

def ispali(str):
    length = len(str)
    k = len(str)-1
    flag = 0
    i = 0
    for j in str:
        if (str[i] == str[k]):
            i = i+1
            k = k-1
            continue
        else:
            print("not a palindrome")
            flag = 1
            break
    if flag == 0:
            print("string is palindrome")


def main():
    str = input("enter a string")
    ispali(str)


if __name__ == "__main__":
    main()
