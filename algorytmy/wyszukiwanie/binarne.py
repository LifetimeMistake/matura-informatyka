# Wyszukiwanie binarne to wydajna metoda znajdowania elementu w posortowanej liście.
# Działa w czasie logarytmicznym O(log n), dzieląc listę na pół przy każdym kroku.
# Rozpoczynamy od wyznaczenia dwóch wskaźników - lewego i prawego, które będziemy
# przesuwać by wyznaczać nowe indeksy środka. Po obliczeniu środka, sprawdzamy czy
# wartość znalezionego elementu jest równa szukanej wartości. Jeżeli tak, to
# zwracamy jej indeks, jeżeli nie, to przesuwamy lewy lub prawy wskaźnik w zależności
# od wyniku porównania.

# Uwaga: Algorytm działa tylko na posortowanych danych!

def wyszukiwanie_binarne(lista, szukana_wartosc):
    left = 0
    right = len(lista) - 1

    while left <= right:
        # Obliczamy środek
        mid = (left + right) // 2
        if lista[mid] == szukana_wartosc:
            # Znaleziono
            return mid
        elif lista[mid] < szukana_wartosc:
            # Wartość szukana musi być w prawej połowie
            left = mid + 1
        else:
            # Wartość szukana musi być w lewej połowie
            right = mid - 1

    # Jeżeli nie ma takiego elementu, zwracamy indeks -1
    return -1

# Przykłady użycia:
print(wyszukiwanie_binarne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # 4