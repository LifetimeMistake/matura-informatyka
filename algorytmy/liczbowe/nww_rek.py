# NWW (najmniejsza wspólna wielokrotność) to najmniejsza liczba naturalna, która jest podzielna przez obie liczby.
# Na przykład NWW(12, 18) = 36, ponieważ 36 jest najmniejszą liczbą, która jest podzielna zarówno przez 12 jak i 18.


# Pomocnicza funkcja NWD potrzebna do obliczenia NWW
# (w wersji rekurencyjnej)
def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a % b)

# Prosta implementacja algorytmu NWW
def nww(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // nwd(a, b)

# Implementacja algorytmu NWW z wyjaśnieniami
def _nww(a, b):
    # Jeśli któraś z liczb jest zerem, NWW wynosi 0
    if a == 0 or b == 0:
        return 0
    # NWW = |a * b| / NWD(a, b)
    return abs(a * b) // nwd(a, b)

# Jak obliczamy NWW:
# 1. Najpierw obliczamy NWD (największy wspólny dzielnik) obu liczb
# 2. Następnie korzystamy ze wzoru: NWW(a, b) = |a * b| / NWD(a, b)
# 
# Przykład dla NWW(12, 18):
# 1. Obliczamy NWD(12, 18) = 6
# 2. Obliczamy NWW = |12 * 18| / 6 = 216 / 6 = 36
# 
# Uwagi:
# - Wartość bezwzględna |a * b| jest potrzebna, gdy jedna z liczb jest ujemna
# - Jeśli jedna z liczb jest zerem, NWW wynosi 0
# - Jeśli obie liczby są zerami, NWW wynosi 0


# Przykłady użycia:
print(nww(12, 18))    # 36
print(nww(48, 18))    # 144
print(nww(17, 5))     # 85
print(nww(0, 5))      # 0
print(nww(0, 0))      # 0