# Wartość wielomianu bardzo łatwo można obliczyć metodą Hornera
# Jest to iteracyjny sposób wyznaczania wartości wielomianu

def wartosc_wielomianu(wspolczynniki, x):
    wynik = 0
    for a in wspolczynniki:
        wynik = wynik * x + a

    return wynik

# Przykłady użycia:
# 2x^3 + 3x^2 -x + 5 = 0
# Dla x=2: 2*8 + 3*4 - 2 + 5 = 16 + 12 - 2 + 5 = 31
print(wartosc_wielomianu([2, 3, -1, 5], 2))
# 4x^2 + 3x + 1 = 0
# Dla x=3: 4*9 + 3*3 + 1 = 36 + 9 + 1 = 46
print(wartosc_wielomianu([4, 3, 1], 3))  # 46
# x^2 + 2x + 3 = 0
# Dla x=4: 16 + 8 + 3 = 27
print(wartosc_wielomianu([1, 2, 3], 4)) # 27