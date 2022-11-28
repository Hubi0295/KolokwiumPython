def naj(x,y,z):
    if x>y and x>z:
        return x
    if y>x and y>z:
        return y
    if z>x and z>y:
        return z
def main():
    x = int(input("Podaj pierwsza liczbe: "))
    y = int(input("Podaj pierwsza liczbe: "))
    z = int(input("Podaj pierwsza liczbe: "))
    najwieksza = naj(x,y,z)
    print("Najwieksza liczba to: " + str(najwieksza))
if __name__ == '__main__':
    main()