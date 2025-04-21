# Merge sort (divide and conquer) to algorytm sortowania, który zamiast porównywać elementy
# zamiast tego dzieli listy na połówki, dopóki każda z list nie będzie miała
# jedynie 1 element. Następnie rekonstruuje listę w taki sposób, że każda
# para list jest scalana ponownie wstawiając jej elementy w odpowiedniej kolejności.

# Przykład:
# Start:        [6, 3, 8, 2]
# Podział:        ↙      ↘
#            [6, 3]    [8, 2]
#            ↙  ↘       ↙  ↘
#           [6] [3]    [8] [2]
#            ↘  ↙       ↘  ↙
#            Merge       Merge
#            [3,6]       [2,8]
#              ↘          ↙
#              Finalny Merge
#            → [2, 3, 6, 8]

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    # Podziel na 2 listy
    mid = len(lista) // 2
    lewa = lista[:mid]
    prawa = lista[mid:]

    # Sortuje następnie obie listy
    merge_sort(lewa)
    merge_sort(prawa)

    # Łączenie list
    i = j = k = 0
    while i < len(lewa) and j < len(prawa):
        # Przesuwamy wskaźniki w zależności od porównania
        if lewa[i] < prawa[j]:
            lista[k] = lewa[i]
            i += 1
        else:
            lista[k] = prawa[j]
            j += 1
        k += 1

    # Dodajemy pozostałe elementy
    while i < len(lewa):
        lista[k] = lewa[i]
        i += 1
        k += 1

    while j < len(prawa):
        lista[k] = prawa[j]
        j += 1
        k += 1

    # Lista jest sortowana w miejscu, ale generalnie można ją również zwrócić
    return lista

# Przykłady użycia:
print(merge_sort([5, 3, 1, 4, 2]))  # [1, 2, 3, 4, 5]
print(merge_sort([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(merge_sort([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]