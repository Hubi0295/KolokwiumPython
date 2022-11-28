def main():
    suma=0
    iloczyn=1
    while suma<=255 and iloczyn<=50000:
        liczba = int(input("podaj liczbe: "))
        suma+=liczba
        iloczyn*=liczba
    print(suma)
    print(iloczyn)
if __name__ == '__main__':
    main()