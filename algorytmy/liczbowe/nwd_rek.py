# NWD (największy wspólny dzielnik) to największa liczba naturalna, która dzieli bez reszty obie liczby.
# Na przykład NWD(12, 18) = 6, ponieważ 6 jest największą liczbą, która dzieli zarówno 12 jak i 18.

# Rekurencyjna implementacja algorytmu NWD
def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a % b)

# Rekurencyjna implementacja algorytmu NWD z wyjaśnieniami
def _nwd(a, b):
    # Jeśli druga liczba jest zerem, pierwsza liczba jest NWD
    if b == 0:
        return a
    # W przeciwnym razie wywołujemy funkcję rekurencyjnie
    # z argumentami: b i reszta z dzielenia a przez b
    return _nwd(b, a % b)

# Przykład wykonania funkcji nwd(12, 18):
# 1. nwd(12, 18) -> b != 0, więc wywołujemy nwd(18, 12 % 18) czyli nwd(18, 12)
# 2. nwd(18, 12) -> b != 0, więc wywołujemy nwd(12, 18 % 12) czyli nwd(12, 6)
# 3. nwd(12, 6)  -> b != 0, więc wywołujemy nwd(6, 12 % 6) czyli nwd(6, 0)
# 4. nwd(6, 0)   -> b == 0, więc zwracamy a = 6
# Ostateczny wynik: 6

# Przykłady użycia:
print(nwd(12, 18))    # 6
print(nwd(48, 18))    # 6
print(nwd(17, 5))     # 1 (liczby względnie pierwsze)
print(nwd(0, 5))      # 5
print(nwd(0, 0))      # 0