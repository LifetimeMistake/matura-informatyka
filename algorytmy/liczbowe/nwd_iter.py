# NWD (największy wspólny dzielnik) to największa liczba naturalna, która dzieli bez reszty obie liczby.
# Na przykład NWD(12, 18) = 6, ponieważ 6 jest największą liczbą, która dzieli zarówno 12 jak i 18.

# Prosta implementacja algorytmu NWD
def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

# Implementacja algorytmu NWD z wyjaśnieniami
def _nwd(a, b):
    # Dopóki druga liczba nie jest zerem
    while b != 0:
        # Zapamiętujemy resztę z dzielenia a przez b
        reszta = a % b
        # Przypisujemy a wartość b
        a = b
        # Przypisujemy b wartość reszty
        b = reszta
        # Powtarzamy proces aż b będzie równe 0
    # Gdy b jest równe 0, a zawiera NWD
    return a

# Przykłady użycia:
print(nwd(12, 18))    # 6
print(nwd(48, 18))    # 6
print(nwd(17, 5))     # 1 (liczby względnie pierwsze)
print(nwd(0, 5))      # 5
print(nwd(0, 0))      # 0