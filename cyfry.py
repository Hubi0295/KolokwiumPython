
def main():
    x = -1
    while x<0 or x>999:
        x = int(input("Podaj liczbe z zakresu 0-999: "))
    jednosci = (x%100)%10
    dziesiatki = (x//10)%10
    setki = x//100
    print(jednosci)
    print(dziesiatki)
    print(setki)
    print("Suma cyfr: ", jednosci+setki+dziesiatki)
if __name__ == '__main__':
    main()