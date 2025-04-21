# Selection sort to prosty algorytm sortowania, który skanuje listę elementów,
# wybiera jeden element, który jest najmniejszy, i umieszcza go na początku listy.
# Po każdym przesunięciu elementu, algorytm przesuwa go o jedno miejsce dalej.

def selection_sort(lista):
    for i in range(len(lista)):
        # Wybieramy indeks najmniejszego elementu
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j

        # Zamieniamy elementy
        lista[i], lista[min_index] = lista[min_index], lista[i]

    # Algorytm sortuje liste w miejscu, ale generalnie można ją również zwrócić
    return lista

# Przykłady użycia:
print(selection_sort([5, 3, 1, 4, 2]))  # [1, 2, 3, 4, 5]
print(selection_sort([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(selection_sort([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]