# Algorytm bubble sort działa w taki sposób, że każdy element
# jest porównywany z sąsiednim elementem i pary w złej kolejności
# są zamieniane miejscami. W efekcie największe liczby "bąbelkują"
# na sam koniec listy co sortuje ją rosnąco.

# Wykorzystujemy 2 pętle:
# - Zewnętrzna pętla zapewnia, że każdy element zostanie porównany
# - Wewnętrzna pętla przesuwa elementy na prawo od obecnego indeksu i
def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            # Jeśli element po lewej jest większy od elementu po prawej
            if lista[j] > lista[j + 1]:
                # To je zamieniamy miejscami
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    # Algorytm sortuje liste w miejscu, ale generalnie można ją również zwrócić
    return lista

# Przykłady użycia:
print(bubble_sort([5, 3, 1, 4, 2]))  # [1, 2, 3, 4, 5]
print(bubble_sort([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(bubble_sort([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]