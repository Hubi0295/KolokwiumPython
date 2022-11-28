def main():

    rockpaperscissors()
def rockpaperscissors():
    print("0 – papier, 1 – nożyce, 2 – kamień")
    gracz1 = -1
    gracz2 = -1
    while (gracz1 < 0 or gracz1 > 2) or (gracz2 < 0 or gracz2 > 2):
        gracz1 = int(input("Witaj graczu 1, podaj co chcesz zagrać: "))
        gracz2 = int(input("Witaj graczu 2, podaj co chcesz zagrać: "))
    if gracz1==gracz2:
        while gracz1==gracz2 or ((gracz1 < 0 or gracz1 > 2) or (gracz2 < 0 or gracz2 > 2)):
                print("REMIS!")
                gracz1 = int(input("Witaj graczu 1, podaj co chcesz zagrać: "))
                gracz2 = int(input("Witaj graczu 2, podaj co chcesz zagrać: "))
    if gracz1==0 and gracz2==1:
        print("Wygrał gracz 2")
        return 0
    if gracz1==0 and gracz2==2:
        print("Wygrał gracz 1")
        return 0
    if gracz1==1 and gracz2==0:
        print("Wygrał gracz 1")
        return 0
    if gracz1==1 and gracz2==2:
        print("Wygrał gracz 2")
        return 0
    if gracz1==2 and gracz2==0:
        print("Wygrał gracz 2")
        return 0
    if gracz1==2 and gracz2==1:
        print("Wygrał gracz 1")
        return 0
if __name__ == '__main__':
    main()
