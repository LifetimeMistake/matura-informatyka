# Wyszukiwanie Fibonacciego to mniej znana, ale interesująca metoda wyszukiwania w posortowanej liście.
# Działa podobnie do wyszukiwania binarnego, ale wykorzystuje liczby Fibonacciego do podziału
# zamiast wyznaczać środki przedziałów.
# Ma podobną złożoność do wyszukiwania binarnego - O(log n), ale nie wykonuje operacji dzielenia,
# co może skutkować lepszą wydajnością na systemach bez sprzętowego wsparcia dla tej operacji 
# (np. na niektórych mikrokontrolerach).

def wyszukiwanie_fibonacciego(lista, szukana_wartosc):
    n = len(lista)
    fibMMm2 = 0 # fib(m-2)
    fibMMm1 = 1 # fib(m-1)
    fibM = fibMMm2 + fibMMm1 # fib(m)

    # Znajdujemy najmniejszą liczbę fibM większą lub równą n
    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    # Offset śledzi przedział przeszukiwany z lewej strony
    offset = -1
    while fibM > 1:
        # Obliczamy indeks do porównania: offset + fib(m-2) lub ostatni indeks jeśli wykraczamy za rozmiar listy
        i = min(offset + fibMMm2, n - 1)
        if lista[i] == szukana_wartosc:
            return i
        # Jeśli wartość pod tym indeksem jest mniejsza, to wartość szukana musi być w prawym podziale
        elif lista[i] < szukana_wartosc:
            # Redukujemy liczby Fibonacciego i przesuwamy przedział w prawo
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        # Jeśli wartość pod tym indeksem jest większa, to wartość szukana musi być w lewym podziale
        else:
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1

    # Porównujemy ostatni element za offsetem
    if fibMMm1 and offset + 1 < n and lista[offset + 1] == szukana_wartosc:
        return offset + 1
    
    # Nie znaleziono wartości
    return -1

# Przykład użycia:
lista = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
print(wyszukiwanie_fibonacciego(lista, 85))