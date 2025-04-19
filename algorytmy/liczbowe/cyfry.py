# Rozkład liczby na cyfry
# Algorytm rozkłada liczbę naturalną na jej poszczególne cyfry
# Przykład: 1234 -> [1, 2, 3, 4]
# Specjalne przypadki:
# - 0 -> [0]
# - Liczby ujemne są traktowane tak samo jak ich wartość bezwzględna

def cyfry(n):
    """Iteracyjna implementacja rozkładu liczby na cyfry"""
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

# Alternatywnie, gdy w rozwiązaniu dozwolone jest użycie zamiany typów danych
def cyfry_str(n):
    return [int(c) for c in str(n)]

# Przykłady użycia:
print(f"1234 -> {cyfry(1234)}")  # [1, 2, 3, 4]
print(f"0 -> {cyfry(0)}")  # [0]
print(f"-567 -> {cyfry(-567)}")  # [5, 6, 7]