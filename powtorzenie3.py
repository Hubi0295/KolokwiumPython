def main():
    n = int(input("Podaj wielkosc tablicy: "))
    tab=[0]*n
    i=0
    while i<n:
        tab[i]=int(input("Podaj liczbe: "))
        i+=1
    tablica=[]
    znalezionych = 0
    i=0
    while i<n:
        liczba=tab[i]
        suma=0
        while liczba>0:
            cyfra = liczba%10
            suma = suma+cyfra
            liczba=liczba/10
        if suma>tab[-1]:
            znalezionych+=1
            tablica.append(tab[i])
        i+=1
    print(tab)
    x=tab[-1]
    if x in tablica:
        tablica.remove(x)
    print(tablica)
if __name__=='__main__':
    main()