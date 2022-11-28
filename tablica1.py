def main():
    n = int(input("Podaj ile elementow chcesz wprowadzic do tablicy:"))
    tab = [0]*n
    i=0
    while n>0:
        wartosc = int(input("Podaj liczbe: "))
        tab[i]=wartosc
        i+=1
        n-=1
    min=tab[0]
    max=tab[0]
    for x in tab:
        if x<min:
            min=x
        if x>max:
            max=x
    print(min,max)
if __name__=='__main__':
    main()