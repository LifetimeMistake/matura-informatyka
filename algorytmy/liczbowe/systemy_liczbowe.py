# Konwersja liczby na string w dowolnym systemie liczbowym
# Algorytm konwertuje liczbę całkowitą na jej reprezentację w zadanym systemie
# Przykład: 12 w systemie binarnym -> "1100"
# Specjalne przypadki:
# - 0 -> "0" w każdym systemie
# - Liczby ujemne -> "-" + reprezentacja wartości bezwzględnej
# - System musi być z przedziału [2, 36] (0-9 + a-z)

# Algorytm w wersji prostej - działa dla systemów [2,n]
# Zasada działania:
# 1. Używamy stałej tablicy znaków jako lookup table
# 2. Dzielenie liczby przez system i zbieranie reszt
# 3. Konwersja reszt na znaki przez indeksowanie tablicy
# 4. Odwrócenie kolejności cyfr (bo zbieramy od najmniej znaczącej)
#
# Zalety:
# - Prostszy do zapamiętania
# - Szybszy (nie ma warunków w pętli)
# - Łatwiejszy do zaimplementowania na kartce
#
# Wady:
# - Ograniczony zakres systemów (tylko tyle, ile znaków w tablicy)
# - Mniej elastyczny

def liczba_na_string_prosta(n, system):
    # Tablica znaków używanych w różnych systemach
    # Indeks w tablicy odpowiada wartości cyfry
    # Więc należy zdefiniować tyle znaków ile istnieje w docelowym systemie liczbowym
    # Poniżej przykład dla systemu szesnastkowego
    ZNAKI = "0123456789ABCDEF"
    
    if n == 0:
        return "0"
        
    # Obsługa liczb ujemnych
    znak = "-" if n < 0 else ""
    n = abs(n)
    
    cyfry = []
    while n > 0:
        # Używamy tablicy ZNAKI do konwersji reszty na znak
        cyfry.append(ZNAKI[n % system])
        n = n // system
        
    # Odwracamy kolejność cyfr i łączymy ze znakiem
    return znak + "".join(reversed(cyfry))


# Algorytm ogólny - działa dla systemów [2,36]
# Zasada działania:
# 1. Dzielenie liczby przez system i zbieranie reszt
# 2. Konwersja reszt na znaki:
#    - 0-9 -> cyfry 0-9
#    - 10-35 -> litery a-z
# 3. Odwrócenie kolejności cyfr (bo zbieramy od najmniej znaczącej)

def liczba_na_string_ogolna(n, system=10):
    if n == 0:
        return "0"
        
    # Obsługa liczb ujemnych
    znak = "-" if n < 0 else ""
    n = abs(n)
    
    cyfry = []
    while n > 0:
        reszta = n % system
        # Konwersja reszty na odpowiedni znak
        if reszta < 10:
            # Jeśli reszta mieści się w systemie dziesiętnym, to używamy cyfr
            cyfra = str(reszta)
        else:
            # Dla systemów >10 używamy liter (a=10, b=11, ..., z=35)
            cyfra = chr(ord('A') + reszta - 10)
        cyfry.append(cyfra)
        n = n // system
        
    # Odwracamy kolejność cyfr i łączymy ze znakiem
    return znak + "".join(reversed(cyfry))

# Przykłady użycia:
print("Konwersja liczby na string w różnych systemach:")
print(f"12 w systemie binarnym -> {liczba_na_string_ogolna(12, 2)}")  # "1100"
print(f"12 w systemie ósemkowym -> {liczba_na_string_ogolna(12, 8)}")  # "14"
print(f"12 w systemie szesnastkowym -> {liczba_na_string_ogolna(12, 16)}")  # "C"
print(f"255 w systemie szesnastkowym -> {liczba_na_string_ogolna(255, 16)}")  # "FF"
print(f"-12 w systemie binarnym -> {liczba_na_string_ogolna(-12, 2)}")  # "-1100"
print(f"0 w systemie binarnym -> {liczba_na_string_ogolna(0, 2)}")  # "0"