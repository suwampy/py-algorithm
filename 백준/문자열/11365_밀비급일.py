def 밀비급일():

    tmp =""
    tmp2=""
    s=""
    while tmp != "END":
        tmp = input()
        l = len(tmp)
        if tmp !="END" :
            s += tmp[l::-1]+"\n"

    print(s)

if __name__ =="__main__":
    밀비급일()