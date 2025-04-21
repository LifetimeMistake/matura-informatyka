# Tablica sum prefiksowych to specjalna tablica z zakresu [a, k], w której na i-tym elemencie
# przechowywana jest jakaś wartość obliczona dla przedziału [a, i] w innej tablicy.

# Typowym zadaniem na wykorzystanie tablic prefiksowych jest np. obliczanie ile jest
# liczb pierwszych w danym przedziale. Jeżeli mamy tylko jeden przedział do sprawdzenia
# to utworzenie tablicy sum prefiksowych jest w zasadzie zbędne - możemy po prostu
# zliczyć ile jest liczb pierwszych mieszczącym się w tym przedziale.

# Sytuacja komplikuje się jednak gdy mamy do obliczenia więcej takich przedziałów (np. setki tysięcy).
# Dla każdego przedziału musielibyśmy wtedy przynajmniej zliczyć w pętli sumę liczb pierwszych,
# a w mniej optymanym przypadku jeszcze policzyć liczby pierwsze od nowa dla każdego z przedziałów.

# Jeżeli przedziały do sprawdzenia mają postać [m, n], gdzie `m` da się ograniczyć liczbą `a` w taki sposób,
# że `a` jest najmniejszym `m` wśród wszystkich przedziałów (np. dla [2, 3], [2, 5], [2, 7] min(m) = 2 = a) 
# ORAZ da się ograniczyć parametr `b` w każdym z przedziałów liczbą `k` (np. dla [2, 3], [2, 5], [2, 7] max(b) = 7 = k) 
# to można zbudować tablicę sum prefiksowych w przedziale [a, k]. W takiej konfiguracji dla dowolnego przedziału 
# ograniczonego przez `a` i `k` możemy policzyć ile jest liczb pierwszych w stałym czasie.

# Tablica którą budujemy musi w każdym i-tym elemencie zawierać ilość liczb pierwszych w przedziale [a, i].
# Przykład:
# a = 0, k = 11
# liczby pierwsze = [2, 3, 5, 7, 11] (liczby pierwsze większe od k nie są uwzględniane)
# tablica sum = [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 5]
# Tablica zawiera teraz w każdym i-tym elemencie ilość liczb pierwszych w przedziale [a, i].
# np. dla i = 3 istnieją 2 liczby pierwsze.
# Teraz aby policzyć przedział [a, k] wystarczy sprawdzić wartośc tablicy dla indeksu a-1 i k,
# i wykonać operację tablica[k] - tablica[a-1].

# Poniższe importy są wykorzystywane w benchmarku, nie są wymagane do działania algorytmu
import time
import random

# Poniższy algorytm buduje tablicę sum prefiksowych dla liczb pierwszych w przedziale [2, k].
# Funkcja pomocnicza do obliczania liczb pierwszych w przedziale [a, k].
# Zamiast zwracać finalny wynik sita to zwracamy tablicę z wartościami True/False.
def znajdz_pierwsze_sito(k):
    if k < 2:
        return []
    
    t = [True] * (k + 1)
    t[0] = t[1] = False

    for i in range(2, int(k**0.5) + 1):
        if t[i]:
            for j in range(i*i, k + 1, i):
                t[j] = False

    return t

# Buduje tablicę prefiksową ilości liczb pierwszych w przedziale [0, k].
def zbuduj_tablice_prefiksowa(k):
    # Sito jest idealne do obliczania sum prefiksowych, ponieważ musimy zwiększać wartości tylko dla
    # elementów gdzie występuje wartość True.
    liczby_pierwsze = znajdz_pierwsze_sito(k)
    tablica = [0] * (k + 1)
    suma = 0
    for i in range(k + 1):
        if liczby_pierwsze[i]:
            suma += 1

        tablica[i] = suma

    return tablica

# Implementuje algorytm T[k] - T[a-1]
def suma_w_przedziale_tablica(a, k, tablica):
    return tablica[k] - tablica[a - 1]

# -------------------------------------------------------------
# Benchmark wersji naiwnej vs tablicy prefiksowej

# Implementuje sumę liczb pierwszych w wersji naiwnej
# Zakładamy, że zostały zastosowane podstawowe implementacje
# w postaci przechowywania już obliczonego sita.
def suma_w_przedziale_naiwna(a, k, sito):
    suma = 0
    for i in range(a, k + 1):
        suma += sito[i]

    return suma

def wylosuj_przedzialy(k, n):
    przedzialy = []
    for _ in range(n):
        a = random.randint(0, k)
        b = random.randint(a, k)
        przedzialy.append((a, b))

    return przedzialy


k = 1_000_000
n = 500 # 500 przedziałów (dla większych wartości metoda naiwna jest zbyt powolna)
# Wybieramy losowe przedziały do sprawdzenia
przedzialy = wylosuj_przedzialy(k, n)
sito = znajdz_pierwsze_sito(k)
tablica = zbuduj_tablice_prefiksowa(k)

# Jako test przyjmujemy, że naszym zadaniem jest obliczenie sumy wszystkich przedziałów
suma_naiwna = 0
start = time.time()
for przedzial in przedzialy:
    suma_naiwna += suma_w_przedziale_naiwna(*przedzial, sito)
czas_naiwny = time.time() - start

print(f"Naiwna implementacja: {czas_naiwny:.2f} sekund")
print(f"Znaleziono {suma_naiwna} liczb pierwszych")

start = time.time()
suma_tablica = 0
for przedzial in przedzialy:
    suma_tablica += suma_w_przedziale_tablica(*przedzial, tablica)
czas_tablicowa = time.time() - start

print(f"Tablicowa implementacja: {czas_tablicowa} sekund")
print(f"Znaleziono {suma_tablica} liczb pierwszych")

print(f"Tablica sum prefiksów jest {czas_naiwny/czas_tablicowa:.1f} razy szybsza!")