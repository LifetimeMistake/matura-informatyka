# Rozkład liczby na cyfry
# Algorytm rozkłada liczbę naturalną na jej poszczególne cyfry
# Przykład: 1234 -> [1, 2, 3, 4]
# Specjalne przypadki:
# - 0 -> [0]
# - Liczby ujemne są traktowane tak samo jak ich wartość bezwzględna

def cyfry(n):
    if n == 0:
        return [0]
        
    # Usuwamy znak liczby ujemnej
    n = abs(n)
    
    cyfry = []
    while n > 0:
        # Bierzemy ostatnią cyfrę
        cyfra = n % 10
        # Dodajemy ją na początek listy
        cyfry.insert(0, cyfra)
        # Usuwamy ostatnią cyfrę z liczby
        n = n // 10
        
    return cyfry

# Dobrze by było zwrócić uwagę na to, że powyższa funkcja wykorzystuje do swojego działania funkcję insert
# Użycie insert(0, cyfra) jest nieefektywne, ponieważ:
# 1. Każde wstawienie na początek listy wymaga przesunięcia wszystkich istniejących elementów
# 2. Złożoność czasowa wynosi O(n) dla każdej operacji insert(0, ...)
# 3. Dla n cyfr, całkowita złożoność wynosi O(n²)

# Lepszym rozwiązaniem byłoby użycie append() (O(1) dla każdej operacji)
# i odwrócenie listy na końcu (O(n)):
def cyfry_optymalne(n):
    if n == 0:
        return [0]
    n = abs(n)
    cyfry = []
    while n > 0:
        cyfry.append(n % 10)
        n = n // 10
    return cyfry[::-1]

# Ta wersja ma złożoność O(n) i jest znacznie szybsza dla dużych liczb.

# Alternatywnie, gdy w rozwiązaniu dozwolone jest użycie zamiany typów danych
def cyfry_str(n):
    return [int(c) for c in str(n)]

# Przykłady użycia:
print(f"1234 -> {cyfry(1234)}")  # [1, 2, 3, 4]
print(f"0 -> {cyfry(0)}")  # [0]
print(f"-567 -> {cyfry(-567)}")  # [5, 6, 7]