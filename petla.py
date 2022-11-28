def main():
    n = int(input("Podaj ile licz: "))
    suma=0
    while n>0:
        liczba = int(input("Podaj liczbe: "))
        if liczba<10 or liczba>50:
            print("Zly przedzial liczby powtorz")
            continue
        suma+=liczba*liczba
        n-=1
    print(suma)
if __name__ == '__main__':
    main()