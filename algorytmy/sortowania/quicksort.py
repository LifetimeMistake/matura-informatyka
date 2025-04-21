# Quicksort (divide and conquer) to algorytm sortowania, który działa w następujący sposób:
# 1. Wybieramy "pivot", czyli element do którego będziemy porównywać wszystkie inne elementy
# 2. Wszystko co jest większe od pivota przesuwamy do prawej strony, a wszystko co jest mniejsze od pivota
# przesuwamy w lewo.
# 3. Po kroku 2 w efekcie otrzymujemy 2 listy podzielone przez pivot. Cały algorytm powtarzamy dla obu list

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    # Może być zwykły, środkowy lub pierwszy
    pivot = lista[0]
    lewa = [x for x in lista[1:] if x < pivot]
    prawa = [x for x in lista[1:] if x >= pivot]

    return quick_sort(lewa) + [pivot] + quick_sort(prawa)

# Przykłady użycia:
print(quick_sort([5, 3, 1, 4, 2]))  # [1, 2, 3, 4, 5]
print(quick_sort([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(quick_sort([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]