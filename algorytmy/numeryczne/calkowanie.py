# Obliczanie pola pod wykresem funkcji numerycznie (na danym przedziale [a, b]).
# Pole pod krzywą można przybliżyć, dzieląc przedział na n małych fragmentów,
# dla których łatwo obliczyć pole (np. prostokątów lub trapezów).
# Każdy kawałek ma określoną szerokość (b - a) / n i wysokość zależną od wartości funkcji.
# Im większe n (czyli węższe kawałki), tym dokładniejsze przybliżenie całkowitego pola.
# W granicy, gdy n → ∞, suma kawałków dąży do całki oznaczonej funkcji f:
# lim (n→∞) ∑ przybliżeń ≈ ∫_a^b f(x) dx

# Metoda prostokątów: dzielimy przedział [a, b] na n małych odcinków
# Dla każdego z nich obliczamy wartość funkcji i traktujemy ją jako wysokość prostokąta
# Pole to suma pól wszystkich prostokątów (szerokość * wysokość)

def metoda_prostokatow(f, a, b, n=1000):
    # Obliczamy szerokość każdego kawałka
    szerokosc = (b - a) / n
    pole = 0
    # Po kolei obliczamy kolejne kawałki
    for i in range(n):
        x = a + i * szerokosc # Lewy wierzchołek podstawy
        pole += f(x) * szerokosc # wysokosc * szerokosc
    return pole

# Metoda trapezów: każdy odcinek traktujemy jako podstawę trapezu, a wartości funkcji jako wysokości
# Pole trapezu = (a + b) / 2 * h, czyli średnia wartość funkcji na końcach * szerokość przedziału
# Metoda ta pozwala na dokładniejsze przybliżenie pola bez potrzeby zwiększania liczby kawałków
# Trapezy są obrócone bokiem, tak że mają stałą wysokość (szerokość kawałka), natomiast różnią się podstawami a i b.

def metoda_trapezow(f, a, b, n=1000):
    # Obliczamy szerokość każdego kawałka
    szerokosc = (b - a) / n
    pole = 0
    podstawa_a = f(a) # Pierwszy punkt funkcji (lewy wierzchołek podstawy w punkcie a)
    # Obliczamy kolejne trapezy
    for i in range(1, n + 1):
        x = a + i * szerokosc # Prawy wierzchołek podstawy
        podstawa_b = f(x)
        pole += podstawa_a + podstawa_b
        podstawa_a = podstawa_b # W następnym trapezie wykorzystamy tę podstawę gdyż trapezy są do siebie przyległe

    # Zmienna pole zawiera w tym momencie sumy podstaw wszystkich trapezów
    # Z wzoru na pole trapezu: pole = (a + b) / 2 * h
    # Gdy pole całkowite to suma pól trapezów, np. P = P1 + P2 + P3 + P4 + ...
    # Możemy zastosować przekształcenie:
    # P = (a1 + b1) / 2 * h + (a2 + b2) / 2 * h + ... + (an + bn) / 2 * h
    # P = h * (a1 + a2 + ... + an + b1 + b2 + ... + bn) / 2 
    return pole / 2 * szerokosc

# Przykładowa funkcja:
def funkcja(x):
    return x**3-2*x**2-x+3

# Przykłady użycia:
print(metoda_prostokatow(funkcja, 0, 2))     # Metoda prostokątów
print(metoda_trapezow(funkcja, 0, 2))        # Metoda trapezów