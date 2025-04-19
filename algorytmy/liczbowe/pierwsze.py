# Algorytm sprawdzający czy liczba jest pierwsza
# Liczba pierwsza to liczba naturalna większa od 1, która ma dokładnie dwa dzielniki: 1 i samą siebie
# Przykłady liczb pierwszych: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...
# Liczby, które nie są pierwsze, nazywamy liczbami złożonymi
# Optymalizacja: wystarczy sprawdzać dzielniki tylko do pierwiastka z liczby,
# ponieważ jeśli liczba ma dzielnik większy od pierwiastka, to musi mieć też dzielnik mniejszy od pierwiastka
# dodatkowo, liczby pierwsze większe niż 2 muszą być nieparzyste

# Import używany w benchmarku, nie jest wymagany do działania algorytmu
import time

def czy_pierwsza(liczba):
    # Liczby mniejsze niż 2 nie są pierwsze
    if liczba < 2:
        return False
        
    # 2 jest liczbą pierwszą
    if liczba == 2:
        return True
        
    # Liczby parzyste większe niż 2 nie są pierwsze
    if liczba % 2 == 0:
        return False
        
    # Sprawdzamy dzielniki od 3 do pierwiastka z liczby, co 2 (tylko nieparzyste)
    for i in range(3, int(liczba**0.5) + 1, 2):
        if liczba % i == 0:
            return False
            
    return True

# Naiwna implementacja znajdowania liczb pierwszych w przedziale [2, k]
# Dla każdej liczby w przedziale sprawdzamy czy jest pierwsza
# Złożoność czasowa: O(k * sqrt(k))
def znajdz_pierwsze(k):
    if k < 2:
        return []
        
    pierwsze = []
    for i in range(2, k + 1):
        if czy_pierwsza(i):
            pierwsze.append(i)
    return pierwsze

# Implementacja sita Eratostenesa - efektywny algorytm znajdowania liczb pierwszych
# Zasada działania:
# 1. Tworzymy tablicę boolowską o rozmiarze k+1, gdzie indeksy reprezentują liczby
# 2. Na początku zakładamy, że wszystkie liczby są pierwsze (True)
# 3. Iterujemy od 2 do pierwiastka z k:
#    - Jeśli liczba jest oznaczona jako pierwsza, to wszystkie jej wielokrotności oznaczamy jako złożone
# 4. Na końcu wszystkie liczby oznaczone jako True to liczby pierwsze
# Złożoność czasowa: O(n log log n)
def znajdz_pierwsze_sito(k):
    if k < 2:
        return []
        
    # Tworzymy tablicę i inicjalizujemy wszystkie wartości jako True
    sito = [True] * (k + 1)
    sito[0] = sito[1] = False  # 0 i 1 nie są pierwsze
    
    # Iterujemy od 2 do pierwiastka z k
    for i in range(2, int(k**0.5) + 1):
        if sito[i]:  # Jeśli i jest pierwsze
            # Oznaczamy wszystkie wielokrotności i jako złożone
            for j in range(i*i, k + 1, i):
                sito[j] = False
                
    # Zbieramy wszystkie liczby pierwsze
    pierwsze = [i for i, jest_pierwsza in enumerate(sito) if jest_pierwsza]
    return pierwsze

# Przykłady użycia:
print("Czy liczba jest pierwsza:")
print(czy_pierwsza(2))    # True
print(czy_pierwsza(17))   # True
print(czy_pierwsza(12))   # False
print(czy_pierwsza(1))    # False
print(czy_pierwsza(0))    # False

print("\nLiczby pierwsze do 20 (naiwna implementacja):")
print(znajdz_pierwsze(20))  # [2, 3, 5, 7, 11, 13, 17, 19]

print("\nLiczby pierwsze do 20 (sito Eratostenesa):")
print(znajdz_pierwsze_sito(20))  # [2, 3, 5, 7, 11, 13, 17, 19]

print("\nBenchmark dla dużego zakresu (2 000 000):")
start = time.time()
pierwsze_sito = znajdz_pierwsze_sito(2_000_000)
czas_sito = time.time() - start
print(f"Sito Eratostenesa: {czas_sito:.2f} sekund")
print(f"Znaleziono {len(pierwsze_sito)} liczb pierwszych")

start = time.time()
pierwsze_naive = znajdz_pierwsze(2_000_000)
czas_naive = time.time() - start
print(f"Naiwna implementacja: {czas_naive:.2f} sekund")
print(f"Znaleziono {len(pierwsze_naive)} liczb pierwszych")

print(f"\nSito jest {czas_naive/czas_sito:.1f} razy szybsze!")
