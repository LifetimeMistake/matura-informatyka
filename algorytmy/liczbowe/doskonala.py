# Liczba doskonała to taka liczba naturalna, która jest równa sumie wszystkich swoich dzielników właściwych
# (czyli dzielników mniejszych od niej samej). Na przykład 6 jest liczbą doskonałą, ponieważ:
# 1 + 2 + 3 = 6

def czy_doskonala(liczba):
    if liczba < 2:  # Liczby doskonałe są większe od 1
        return False
        
    suma_dzielnikow = 1  # 1 jest zawsze dzielnikiem właściwym
    
    # Sprawdzamy dzielniki od 2 do pierwiastka z liczby
    for i in range(2, int(liczba**0.5) + 1):
        if liczba % i == 0:
            suma_dzielnikow += i
            # Dodajemy również drugi dzielnik (liczba/i)
            if i != liczba // i:
                suma_dzielnikow += liczba // i
                
    return suma_dzielnikow == liczba

# Przykłady użycia:
print(czy_doskonala(6))    # True (1 + 2 + 3 = 6)
print(czy_doskonala(28))   # True (1 + 2 + 4 + 7 + 14 = 28)
print(czy_doskonala(12))   # False (1 + 2 + 3 + 4 + 6 = 16 ≠ 12)
print(czy_doskonala(1))    # False (liczby doskonałe są większe od 1)
print(czy_doskonala(496))  # True (kolejna liczba doskonała)
