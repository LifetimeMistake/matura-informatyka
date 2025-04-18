# Potęgowanie to operacja matematyczna, która polega na wielokrotnym mnożeniu liczby przez siebie.
# Na przykład 2^3 = 2 * 2 * 2 = 8, gdzie 2 to podstawa, a 3 to wykładnik.

# Naiwna implementacja potęgowania
def potega_naiwna(podstawa, wykladnik):
    wynik = 1
    for _ in range(wykladnik):
        wynik *= podstawa
    return wynik

# Zoptymalizowana implementacja potęgowania (metoda szybkiego potęgowania)
def potega_szybka(podstawa, wykladnik):
    wynik = 1
    while wykladnik > 0:
        # Jeśli wykładnik jest nieparzysty, mnożymy wynik przez podstawę
        if wykladnik % 2 == 1:
            wynik *= podstawa
        # Podnosimy podstawę do kwadratu
        podstawa *= podstawa
        # Dzielimy wykładnik przez 2
        wykladnik //= 2
    return wynik

# Jak działa szybkie potęgowanie:
# 1. Rozkładamy wykładnik na sumę potęg dwójki (reprezentacja binarna)
# 2. Wykorzystujemy własność: a^(b+c) = a^b * a^c
# 3. Zamiast wykonywać n mnożeń, wykonujemy log(n) mnożeń
#
# Przykład dla 2^13:
# 13 = 8 + 4 + 1
# 2^13 = 2^8 * 2^4 * 2^1
#
# Szczegółowe wyjaśnienie działania algorytmu:
# Algorytm działa poprzez analizę reprezentacji binarnej wykładnika.
# Na przykład dla wykładnika 13 (1101 w systemie binarnym):
#   => 3^13 = 3^(8 + 4 + 0 + 1) = 3^8 * 3^4 * 3^0 * 3^1

# - Każda 1 w reprezentacji binarnej oznacza, że ta potęga dwójki jest częścią wyniku
# - Algorytm sprawdza kolejne bity wykładnika poprzez:
#   * Sprawdzanie czy wykładnik jest nieparzysty (ostatni bit to 1)
#   * Dzielenie wykładnika przez 2 (przesunięcie bitowe w prawo, pozbywa się właśnie użytego bitu i przygotowuje następny)
# - Kiedy wykładnik jest nieparzysty, oznacza to że aktualna potęga podstawy
#   jest potrzebna w wyniku końcowym
# - Podnoszenie podstawy do kwadratu w każdym kroku odpowiada przesuwaniu się
#   do kolejnej potęgi dwójki (3^1 → 3^2 → 3^4 → 3^8 itd.)
#
# Przykład krok po kroku dla 3^13:
# 1. Początkowo: wynik = 1, podstawa = 3, wykladnik = 13 (1101)
# 2. Krok 1 (wykladnik = 13, nieparzysty):
#    - wynik = 1 * 3 = 3  (bierzemy 3^1)
#    - podstawa = 3 * 3 = 9
#    - wykladnik = 13 // 2 = 6
# 3. Krok 2 (wykladnik = 6, parzysty):
#    - wynik = 3 (pomijamy 3^2)
#    - podstawa = 9 * 9 = 81
#    - wykladnik = 6 // 2 = 3
# 4. Krok 3 (wykladnik = 3, nieparzysty):
#    - wynik = 3 * 81 = 243 (bierzemy 3^4)
#    - podstawa = 81 * 81 = 6561
#    - wykladnik = 3 // 2 = 1
# 5. Krok 4 (wykladnik = 1, nieparzysty):
#    - wynik = 243 * 6561 = 1594323 (bierzemy 3^8)
#    - podstawa = 6561 * 6561 = 43046721
#    - wykladnik = 1 // 2 = 0
#
# Uwagi:
# - Szybkie potęgowanie działa dla wykładników całkowitych nieujemnych
# - Dla wykładnika 0 wynik zawsze wynosi 1
# - Dla podstawy 0 i wykładnika > 0 wynik wynosi 0
# - Dla podstawy 0 i wykładnika 0 wynik jest nieokreślony (w implementacji zwracamy 1)

# Przykłady użycia:
print(potega_naiwna(2, 3))     # 8
print(potega_naiwna(3, 4))     # 81
print(potega_naiwna(5, 0))     # 1
print(potega_naiwna(0, 5))     # 0
print(potega_naiwna(0, 0))     # 1

print(potega_szybka(2, 3))     # 8
print(potega_szybka(3, 4))     # 81
print(potega_szybka(5, 0))     # 1
print(potega_szybka(0, 5))     # 0
print(potega_szybka(0, 0))     # 1
