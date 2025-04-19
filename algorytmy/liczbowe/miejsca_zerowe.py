# Znajdowanie miejsc zerowych funkcji to operacja matematyczna, która dla danej funkcji f(x)
# znajduje taką liczbę x, że f(x) = 0.
# Na przykład dla funkcji f(x) = x^2 - 4, miejscem zerowym jest x = 2, ponieważ f(2) = 0.

# Metoda bisekcji (połowienia przedziału)
# --------------------------------------
# Jak działa:
# 1. Metoda wykorzystuje podział przedziału na pół w każdym kroku
# 2. Dla funkcji f(x):
#    - Zakładamy, że funkcja zmienia znak w przedziale [lewy, prawy]
#    - W każdym kroku sprawdzamy środek przedziału
#    - Jeśli f(środek) * f(lewy) < 0, to miejsce zerowe jest w lewej połowie
#    - W przeciwnym razie miejsce zerowe jest w prawej połowie
#
# Przykład dla f(x) = x^2 - 2:
# 1. Początkowo: lewy = 0, prawy = 2
# 2. Krok 1:
#    - środek = (0 + 2)/2 = 1
#    - f(1) = -1, f(0) = -2
#    - f(środek) * f(lewy) > 0, więc lewy = 1
# 3. Krok 2:
#    - środek = (1 + 2)/2 = 1.5
#    - f(1.5) = 0.25, f(1) = -1
#    - f(środek) * f(lewy) < 0, więc prawy = 1.5
#
# Szczegółowe wyjaśnienie:
# - Metoda bisekcji opiera się na twierdzeniu o wartości pośredniej
# - W każdym kroku:
#   1. Obliczamy środek przedziału
#   2. Sprawdzamy znak funkcji w środku i na lewym końcu
#   3. Zawężamy przedział do połowy zawierającej miejsce zerowe
#   4. Powtarzamy aż osiągniemy wymaganą dokładność
#
# Uwagi:
# - Metoda bisekcji jest zawsze zbieżna dla funkcji ciągłych
# - Wymaga aby funkcja zmieniała znak w przedziale
# - Liczba kroków potrzebnych do osiągnięcia dokładności ε:
#   log2((prawy - lewy)/ε)

def miejsce_zerowe_bisekcja(f, lewy, prawy, dokladnosc=0.0001):
    # Sprawdzamy czy funkcja zmienia znak w przedziale
    if f(lewy) * f(prawy) > 0:
        raise ValueError("Funkcja musi zmieniać znak w przedziale [lewy, prawy]")
    
    while prawy - lewy > dokladnosc:
        srodek = (lewy + prawy) / 2
        if f(srodek) * f(lewy) < 0:
            prawy = srodek
        else:
            lewy = srodek
    return (lewy + prawy) / 2

# Metoda Newtona-Raphsona
# ----------------------
# Jak działa:
# 1. Metoda wykorzystuje iteracyjne przybliżanie miejsca zerowego
# 2. Dla funkcji f(x):
#    - W każdym kroku używamy wzoru:
#      x_{n+1} = x_n - f(x_n)/f'(x_n)
#    - gdzie f'(x) to pochodna funkcji f
#
# Przykład dla f(x) = x^2 - 2:
# 1. Początkowo: x = 2
# 2. Krok 1:
#    x = 2 - (2^2 - 2)/(2*2) = 2 - 2/4 = 1.5
# 3. Krok 2:
#    x = 1.5 - (1.5^2 - 2)/(2*1.5) ≈ 1.5 - 0.25/3 ≈ 1.4167
#
# Szczegółowe wyjaśnienie:
# - Metoda Newtona-Raphsona wykorzystuje styczną do funkcji w punkcie
#   do znalezienia lepszego przybliżenia miejsca zerowego
# - W każdym kroku:
#   1. Obliczamy wartość funkcji i jej pochodnej w aktualnym punkcie
#   2. Znajdujemy punkt przecięcia stycznej z osią OX
#   3. Ten punkt staje się nowym przybliżeniem miejsca zerowego
#
# Uwagi:
# - Metoda Newtona-Raphsona jest znacznie szybsza niż metoda bisekcji
# - Wymaga znajomości pochodnej funkcji
# - Może nie zbiegać dla niektórych punktów startowych
# - Dokładność wyniku zależy od parametru dokladnosc

def miejsce_zerowe_newton(f, f_pochodna, x0, dokladnosc=0.0001, max_iter=1000):
    x = x0
    for _ in range(max_iter):
        x_nastepny = x - f(x) / f_pochodna(x)
        if abs(x_nastepny - x) < dokladnosc:
            return x_nastepny
        x = x_nastepny
    raise ValueError("Metoda nie zbiegła w podanej liczbie iteracji")

# Przykłady użycia:
def f(x):
    return x**2 - 2

def f_pochodna(x):
    return 2*x

print(miejsce_zerowe_bisekcja(f, 0, 2))     # ≈ 1.4142 (√2)
print(miejsce_zerowe_newton(f, f_pochodna, 2))  # ≈ 1.4142 (√2) 