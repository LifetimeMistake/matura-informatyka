# Szyfr kolumnowy jest przykładem szyfru transpozycyjnego, w których znaki tekstu jawnego 
# nie są zamieniane na inne, ale ich kolejność jest zmieniana według ustalonej reguły.

# Istnieją dwa popularne warianty szyfru kolumnowego:
# 1. Prosty szyfr kolumnowy, gdzie kluczem jest liczba kolumn.
# 2. Szyfr kolumnowy z permutacja kolumn, gdzie kluczem jest ciąg określający kolejność kolumn.

# W obu przypadkach tekst jawny jest wpisywany poziomo do tabeli, a następnie odczytywany w kolumnach.
# (w kolejności od lewej do prawej lub według kolejności zgodnej z kluczem)

# Wariant 1: Prosty szyfr kolumnowy
# Kluczem jest liczba kolumn (np. 4)
# Tekst jest wpisywany wierszami do tabeli o rozmiarze N x K,
# a następnie odczytywany kolumnami.
# Długość tekstu może wymagać uzupełnienia znakiem wypełniającym (padding)
# Dla czytelności w tym przypadku używamy znaku kropki.

import math

# k to liczba kolumn
def szyfruj1(tekst, k):
    tekst = tekst.replace(" ", "-") # Nie obsługujemy spacji
    n = math.ceil(len(tekst) / k) # Liczba wierszy
    tablica = [[""] * k for _ in range(n)]

    # Wpisujemy tekst wierszami
    index = 0
    for r in range(n):
        for c in range(k):
            if index < len(tekst):
                # Mamy jeszcze znaki do wpisania
                tablica[r][c] = tekst[index]
                index += 1
            else:
                # Nie ma więcej znaków do wpisania
                # Wypełniamy paddingiem
                tablica[r][c] = "."

    # Odczytujemy tekst kolumnami
    output = ""
    for c in range(k):
        for r in range(n):
            output += tablica[r][c]

    return output

# Odszyfrowanie jest bardzo podobne do szyfrowania, ale odwracamy kolejność operacji.
# Na początku wpisujemy tekst kolumnami, a następnie odczytujemy wierszami.
def odszyfruj1(tekst, k):
    n = math.ceil(len(tekst) / k)
    tablica = [[""] * k for _ in range(n)]

    # Wpisujemy tekst kolumnami
    index = 0
    for c in range(k):
        for r in range(n):
            tablica[r][c] = tekst[index]
            index += 1

    # Odczytujemy tekst wierszami
    output = ""
    for r in range(n):
        for c in range(k):
            output += tablica[r][c]

    return output

# Wariant 2: Szyfr kolumnowy z permutacją kolumn
# Klucz to lista/liczba określająca kolejność kolumn.
# np. klucz [3, 1, 2] oznacza, że 1. kolumna ma stanąć na 3. miejscu
# Indeksy są 1-indeksowane (czyli pierwsza kolumna ma indeks 1)
# W tym przypadku przyjmujemy, że kluczem jest lista
# Algorytm jest w zasadzie identyczny z przykładem z wariantem 1.
# poza tym, że zamieniamy kolejność odczytu zgodnie z kluczem.

def szyfruj2(tekst, klucz):
    tekst = tekst.replace(" ", "-") # Nie obsługujemy spacji
    k = len(klucz) # Liczba kolumn
    n = math.ceil(len(tekst) / k) # Liczba wierszy
    tablica = [[""] * k for _ in range(n)]

    # Wpisujemy tekst wierszami
    index = 0
    for r in range(n):
        for c in range(k):
            if index < len(tekst):
                # Mamy jeszcze znaki do wpisania
                tablica[r][c] = tekst[index]
                index += 1
            else:
                # Nie ma więcej znaków do wpisania
                # Wypełniamy paddingiem
                tablica[r][c] = "."

    # Odczytujemy tekst kolumnami zgodnie z kluczem
    output = ""
    for c in klucz:
        c = c - 1 # Python indeksuje od 0
        for r in range(n):
            output += tablica[r][c]

    return output

# Odszyfrowanie z kluczem polega na wpisywaniu zaszyfrowanego tekstu
# w odpowiedniej kolejności i odczytaniu od lewej do prawej.

def odszyfruj2(tekst, klucz):
    k = len(klucz) # Liczba kolumn
    n = math.ceil(len(tekst) / k)
    tablica = [[""] * k for _ in range(n)]

    # Wpisujemy tekst kolumnami zgodnie z kluczem
    index = 0
    for c in klucz:
        c = c - 1 # Python indeksuje od 0
        for r in range(n):
            tablica[r][c] = tekst[index]
            index += 1

    # Odczytujemy tekst wierszami
    output = ""
    for r in range(n):
        for c in range(k):
            output += tablica[r][c]

    return output

# Przykłady użycia:
print(szyfruj1("SZYFRKOLUMNOWY", 4))  # SRUWZKMYYON.FLO.
print(szyfruj2("ALAMAKOTATEST123", [3, 1, 2, 4])) # AOE2AAATLKT1MTS3

print(odszyfruj1("SRUWZKMYYON.FLO.", 4))  # SZYFRKOLUMNOWY
print(odszyfruj2("AOE2AAATLKT1MTS3", [3, 1, 2, 4])) # ALAMAKOTATEST123

