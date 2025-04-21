# Insertion sort to algorytm który krok po kroku wstawia
# elementy w odpowiednie miejsca by posortować listę.

# Przykład:
# A = [5, 2, 4, 6, 1] B = []
# 1. A = [2, 4, 6, 1] B = [5]
# 2. A = [4, 6, 1] B = [2, 5]
# 3. A = [6, 1] B = [2, 4, 5]
# 4. A = [1] B = [2, 4, 5, 6]
# 5. A = [] B = [1, 2, 4, 5, 6]

# Algorytm po prostu wstawia dany element między już posortowane elementy.
# Dodatkowo do jego działania nie jest potrzebna lista pomocnicza B,
# jeśli założymy, że posortowane elementy mają wylądować po lewej lub po prawej stronie
# posortowanej listy.

def insertion_sort(lista):
    # Skip pierwszego indeksu
    for i in range(1, len(lista)):
        k = lista[i]
        j = i - 1 # Rozpoczynamy sprawdzanie od elementu poprzedniego
        # Sprawdzamy teraz gdzie trzeba wstawić k
        while j >= 0 and lista[j] > k:
            # Przesuwamy elementy większe od k w prawo
            lista[j + 1] = lista[j]
            j -= 1

        # Finalnie wstawiamy k w odpowiednie miejsce
        lista[j + 1] = k

    # Algorytm sortuje liste w miejscu, ale generalnie można ją również zwrócić
    return lista

# Przykłady użycia:
print(insertion_sort([5, 3, 1, 4, 2]))  # [1, 2, 3, 4, 5]
print(insertion_sort([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(insertion_sort([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]