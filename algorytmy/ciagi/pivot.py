# Pivot index to taki indeks w tablicy, który dzieli ją na dwie części
# o równej sumie. Na przykład dla [1, 7, 3, 6, 5, 6] indeks to 3,
# ponieważ suma lewa (1+7+3) = suma prawa (5+6) = 11.
# Indeks w którym znajduje się pivot nie jest brany pod uwagę.
# W powyższym przykładzie indeks 3 ma wartość równą 6.
# Przypadki specjalne:
# - Jeśli tablica nie ma pivota to zwracamy -1
# - Jeśli tablica ma wiele pivotów to zwracamy ten najbardziej z lewej

def pivot_index(lista):
    # Dla tablicy o długości 1 nie ma pivota
    if len(lista) == 1:
        return -1
    
    # Zaczynamy od indeksu 0, więc suma lewa jest równa 0, a suma prawa 
    # jest równa sumie wszystkich elementów
    lewa = 0
    prawa = sum(lista)

    for i in range(len(lista)):
        # Usuwamy pivot z prawej strony
        prawa -= lista[i]
        if lewa == prawa:
            # Jeśli suma lewa i prawa są równe to znaleźliśmy pivot
            return i
        lewa += lista[i]

    return -1

# Przykłady użycia:
print(pivot_index([1, 7, 3, 6, 5, 6]))  # 3
print(pivot_index([1, 2, 3, 4, 5]))  # -1
print(pivot_index([1, 2, 3, 4, 5, 6]))  # -1
print(pivot_index([10, 3, 15, -5]))  # 1