# Rozkład liczby na czynniki pierwsze
# Algorytm rozkłada liczbę naturalną na jej czynniki pierwsze
# Przykład: 12 -> [2, 2, 3] (bo 2 * 2 * 3 = 12)
# Specjalne przypadki:
# - 0 -> [] (nie ma rozkładu)
# - 1 -> [] (1 nie jest liczbą pierwszą)

def czynniki_pierwsze(n):
    n = abs(n) # Implementacja nie wspiera rozkładu dla liczb ujemnych
    # Aby zapewnić taką funkcjonalność, pierwszy czynnik należy dodać z znakiem ujemnym (jeśli liczba była ujemna),
    # a resztę operacji wykonywac na abs(n).

    if n < 2:
        return []
        
    czynniki = []
    
    # Najpierw sprawdzamy podzielność przez 2 (wyciągamy wszystkie czynniki 2)
    while n % 2 == 0:
        czynniki.append(2)
        n = n // 2
        
    # Następnie sprawdzamy podzielność przez nieparzyste liczby
    # od 3 do pierwiastka z n (wyciągamy wszystkie czynniki od 3 do n)
    i = 3
    while i * i <= n:
        while n % i == 0:
            czynniki.append(i)
            n = n // i
        i += 2
        
    # Jeśli pozostała liczba jest większa niż 2, to jest pierwsza
    if n > 2:
        czynniki.append(n)
        
    return czynniki

# Algorytm działa następująco (na przykładzie n=12):
# 1. Sprawdzamy przypadki specjalne:
#    - n<2 -> zwracamy []
# 2. Bierzemy wartość bezwzględną z n
# 3. Inicjalizujemy pustą listę czynników
# 4. Najpierw sprawdzamy podzielność przez 2:
#    a. Dopóki n jest podzielne przez 2:
#       - Dodajemy 2 do listy czynników
#       - Dzielimy n przez 2
#       np. dla n=12: 12/2=6 -> dodajemy 2, 6/2=3 -> dodajemy 2
# 5. Następnie sprawdzamy podzielność przez nieparzyste liczby:
#    a. Iterujemy od 3 do pierwiastka z n, co 2 (tylko nieparzyste)
#    b. Dla każdego i:
#       - Dopóki n jest podzielne przez i:
#         * Dodajemy i do listy czynników
#         * Dzielimy n przez i
#       np. dla n=3: 3/3=1 -> dodajemy 3
# 6. Jeśli pozostała liczba jest większa niż 2, dodajemy ją do czynników
#    (jest to ostatni czynnik pierwszy)
#
# Przykład dla n=12:
# - Start: n=12, czynniki=[]
# - Sprawdzamy podzielność przez 2:
#   * 12%2=0 -> n=12/2=6, czynniki=[2]
#   * 6%2=0 -> n=6/2=3, czynniki=[2,2]
#   * 3%2≠0 -> koniec
# - Sprawdzamy podzielność przez 3:
#   * 3%3=0 -> n=3/3=1, czynniki=[2,2,3]
#   * 1%3≠0 -> koniec
# - Wynik: [2,2,3]

# Powyższy algorytm jest ogólną implementacją rozkładu na czynniki pierwsze
# Jeżeli znamy już wszystkie liczby pierwsze występujące w przedziale [2, n] (np. policzone z sita Eratostenesa),
# to możemy uprościć algorytm rozkładu:

def czynniki_pierwsze_z_lista(n, lista_pierwszych):
    n = abs(n)

    if n < 2:
        return []
        
    czynniki = []
    
    # Sprawdzamy podzielność przez liczby pierwsze z listy
    for p in lista_pierwszych:
        # Sprawdzamy dzielniki tylko do pierwiastka z n.
        if p * p > n:
            break
        while n % p == 0:
            czynniki.append(p)
            n = n // p
            
    # Jeśli pozostała liczba jest większa niż 1, to jest pierwsza
    if n > 1:
        czynniki.append(n)
        
    return czynniki

# Wtedy jako źródła dzielników pierwszych używamy listy z sita (efektywnie pomijając obliczanie dzielnikó pierwszych),
# co pozwala szybko rozłożyć wiele liczb (przy założeniu, że lista dzielników jest z przedziału [2, max(n)]).

# Przykłady użycia:
print(f"12 -> {czynniki_pierwsze(12)}")  # [2, 2, 3]
print(f"17 -> {czynniki_pierwsze(17)}")  # [17] (liczba pierwsza)
print(f"0 -> {czynniki_pierwsze(0)}")    # []
print(f"1 -> {czynniki_pierwsze(1)}")    # []

# Przykłady użycia dla funkcji czynniki_pierwsze_z_lista:
print(f"12 -> {czynniki_pierwsze_z_lista(12, [2,3,5,7,11,13])}")  # [2, 2, 3]
print(f"17 -> {czynniki_pierwsze_z_lista(17, [2,3,5,7,11,13,17])}")  # [17] (liczba pierwsza)
print(f"0 -> {czynniki_pierwsze_z_lista(0, [2,3,5,7,11,13])}")    # []
print(f"1 -> {czynniki_pierwsze_z_lista(1, [2,3,5,7,11,13])}")    # []
print(f"100 -> {czynniki_pierwsze_z_lista(100, [2,3,5,7,11,13])}")  # [2, 2, 5, 5]
print(f"121 -> {czynniki_pierwsze_z_lista(121, [2,3,5,7,11,13])}")  # [11, 11]
