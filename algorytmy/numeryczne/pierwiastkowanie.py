# Pierwiastkowanie to operacja matematyczna, która dla danej liczby a i stopnia n
# znajduje taką liczbę x, że x^n = a.
# Na przykład √9 = 3, ponieważ 3^2 = 9.

# Warto zauważyć, że pierwiastkowanie jest po prostu szczególnym przypadkiem znajdowania miejsc zerowych funkcji.
# Dla pierwiastka stopnia n z liczby a, możemy zdefiniować funkcję f(x) = x^n - a.
# Znalezienie pierwiastka jest równoważne znalezieniu miejsca zerowego tej funkcji.
# Na przykład, aby znaleźć √2, szukamy miejsca zerowego funkcji f(x) = x^2 - 2.
# Podobnie, aby znaleźć ³√8, szukamy miejsca zerowego funkcji f(x) = x^3 - 8.

# Poniższe implementacje są specjalizowanymi wersjami ogólnych metod znajdowania miejsc zerowych:
# - pierwiastek_naiwny to specjalizacja metody bisekcji
# - pierwiastek_szybki to specjalizacja metody Newtona-Raphsona

# Naiwna implementacja pierwiastkowania (metoda bisekcji)
def pierwiastek_naiwny(liczba, stopien, dokladnosc=0.0001):
    # Szukamy pierwiastka w przedziale [0, liczba]
    lewy = 0    
    prawy = liczba
    while prawy - lewy > dokladnosc:
        srodek = (lewy + prawy) / 2
        if srodek ** stopien < liczba:
            lewy = srodek
        else:
            prawy = srodek
    return (lewy + prawy) / 2

# Jak działa metoda bisekcji:
# 1. Metoda wykorzystuje podział przedziału na pół w każdym kroku
# 2. Dla pierwiastka stopnia n z liczby a:
#    - Zakładamy, że pierwiastek znajduje się w przedziale [0, a]
#    - W każdym kroku sprawdzamy środek przedziału
#    - Jeśli środek^n < a, to pierwiastek jest w prawej połowie
#    - Jeśli środek^n > a, to pierwiastek jest w lewej połowie
#
# Przykład dla √2 (pierwiastek kwadratowy z 2):
# 1. Początkowo: lewy = 0, prawy = 2
# 2. Krok 1:
#    - środek = (0 + 2)/2 = 1
#    - 1^2 = 1 < 2, więc lewy = 1
# 3. Krok 2:
#    - środek = (1 + 2)/2 = 1.5
#    - 1.5^2 = 2.25 > 2, więc prawy = 1.5
# 4. Krok 3:
#    - środek = (1 + 1.5)/2 = 1.25
#    - 1.25^2 = 1.5625 < 2, więc lewy = 1.25
# 5. Krok 4:
#    - środek = (1.25 + 1.5)/2 = 1.375
#    - 1.375^2 = 1.8906 < 2, więc lewy = 1.375
#
# Szczegółowe wyjaśnienie działania algorytmu:
# - Metoda bisekcji opiera się na twierdzeniu o wartości pośredniej
# - W każdym kroku:
#   1. Obliczamy środek przedziału
#   2. Sprawdzamy czy środek^n jest mniejszy czy większy od a
#   3. Zawężamy przedział do połowy zawierającej pierwiastek
#   4. Powtarzamy aż osiągniemy wymaganą dokładność
#
# Uwagi:
# - Metoda bisekcji jest zawsze zbieżna
# - W każdym kroku przedział jest dzielony na pół
# - Liczba kroków potrzebnych do osiągnięcia dokładności ε:
#   log2((prawy - lewy)/ε)
# - Dla pierwiastków parzystego stopnia, liczba musi być nieujemna
# - Dla pierwiastków nieparzystego stopnia, liczba może być ujemna

# Zoptymalizowana implementacja pierwiastkowania (metoda Newtona-Raphsona)
def pierwiastek_szybki(liczba, stopien, dokladnosc=0.0001):
    # Wybieramy początkowy punkt startowy
    x = liczba
    while True:
        # Obliczamy następne przybliżenie
        x_nastepny = ((stopien - 1) * x + liczba / (x ** (stopien - 1))) / stopien
        # Sprawdzamy czy osiągnęliśmy wymaganą dokładność
        if abs(x_nastepny - x) < dokladnosc:
            return x_nastepny
        x = x_nastepny

# Jak działa metoda Newtona-Raphsona:
# 1. Metoda wykorzystuje iteracyjne przybliżanie pierwiastka
# 2. Dla pierwiastka stopnia n z liczby a:
#    - Szukamy miejsca zerowego funkcji f(x) = x^n - a
#    - W każdym kroku używamy wzoru:
#      x_{n+1} = x_n - f(x_n)/f'(x_n)
#      gdzie f'(x) = n * x^(n-1)
#    - Po uproszczeniu otrzymujemy:
#      x_{n+1} = ((n-1)*x_n + a/x_n^(n-1))/n
#
# Przykład dla √2 (pierwiastek kwadratowy z 2):
# 1. Początkowo: x = 2
# 2. Krok 1:
#    x = (1*2 + 2/2)/2 = (2 + 1)/2 = 1.5
# 3. Krok 2:
#    x = (1*1.5 + 2/1.5)/2 ≈ (1.5 + 1.333)/2 ≈ 1.4167
# 4. Krok 3:
#    x = (1*1.4167 + 2/1.4167)/2 ≈ (1.4167 + 1.4118)/2 ≈ 1.4142
#
# Szczegółowe wyjaśnienie działania algorytmu:
# - Metoda Newtona-Raphsona wykorzystuje styczną do funkcji w punkcie
#   do znalezienia lepszego przybliżenia pierwiastka
# - W każdym kroku:
#   1. Obliczamy wartość funkcji i jej pochodnej w aktualnym punkcie
#   2. Znajdujemy punkt przecięcia stycznej z osią OX
#   3. Ten punkt staje się nowym przybliżeniem pierwiastka
# - Proces powtarzamy aż osiągniemy wymaganą dokładność
#
# Uwagi:
# - Metoda Newtona-Raphsona jest znacznie szybsza niż metoda bisekcji
# - Dla pierwiastków parzystego stopnia, liczba musi być nieujemna
# - Dla pierwiastków nieparzystego stopnia, liczba może być ujemna
# - Dokładność wyniku zależy od parametru dokladnosc
# - Metoda może nie zbiegać dla niektórych wartości początkowych

# Przykłady użycia:
print(pierwiastek_naiwny(2, 2))     # ≈ 1.4142 (√2)
print(pierwiastek_naiwny(8, 3))     # ≈ 2.0 (³√8)
print(pierwiastek_naiwny(16, 4))    # ≈ 2.0 (⁴√16)

print(pierwiastek_szybki(2, 2))     # ≈ 1.4142 (√2)
print(pierwiastek_szybki(8, 3))     # ≈ 2.0 (³√8)
print(pierwiastek_szybki(16, 4))    # ≈ 2.0 (⁴√16)
