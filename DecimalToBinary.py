def ToBinary(n):
    binar=[]
    while n!=0:
        x=n%2
        binar.append(x)
        n=n//2
    binar.reverse()
    binary=""
    for x in binar:
        binary+=str(x)
    binary=int(binary)
    return binary
def ToDecimal(n):
    n=str(n)
    list=[0]
    list[0]=n
    newlist=[]
    for x in list[0]:
        newlist.append(x)
    i=0
    decimal=0
    while i<len(newlist):
        y = int(newlist[i])
        if i==0:
            decimal=y
            i+=1
            continue
        decimal=2*decimal+y
        i+=1
    return decimal
def main():
    n=int(input("Insert your number in decimal system: "))
    binary=ToBinary(n)
    print(binary)
    decimal=ToDecimal(binary)
    print(decimal)
if __name__=="__main__":
    main()