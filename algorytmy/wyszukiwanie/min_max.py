# Wyszukiwanie wartości minimalnej i maksymalnej w liście.
# Przeglądamy każdy element listy, zapamiętując aktualne minimum i maksimum.
# Algorytm nie wymaga sortowania listy i działa dla dowolnych elementów.
# Złożoność czasu: O(n)

def wyszukiwanie_min_max(lista):
    # Jeżeli lista jest pusta, to nie ma wartości minimalnej i maksymalnej
    if not lista:
        return None, None
    
    minimum = maksimum = lista[0]
    # Pomijamy pierwszy element, gdyż już był wykorzystany
    for x in lista[1:]:
        if x < minimum:
            minimum = x
        elif x > maksimum:
            maksimum = x

    return minimum, maksimum

# Przykłady użycia:
print(wyszukiwanie_min_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 1, 10
print(wyszukiwanie_min_max([4, 5, 7, 5, 3, 10, 11]))  # 3, 11