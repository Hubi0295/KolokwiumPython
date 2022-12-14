def Euklides(a,b):
    r=a%b
    test = None
    while r!=0:
        if a<b:
            x=a
            a=b
            b=x
        r = a % b
        a=b
        b=r
    return a
def main():
    a=int(input("Podaj liczbe a: "))
    b = int(input("Podaj liczbe b: "))
    nwd = Euklides(a,b)
    print(nwd)

if __name__=="__main__":
    main()