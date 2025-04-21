# Używane do generowania losowego klucza dla testu, nie jest wymagane do działania algorytmu
import random

# Szyfry podstawieniowe to klasa szyfrów w kryptografii, w której każdy znak tekstu jawnego
# jest zastępowany innym znakiem, zgodnie z ustaloną metodą lub kluczem. Jest to podstawowy
# rodzaj szyfrów klasycznych.

# Poniższy algorytm podstawieniowy jest szyfrem podstawieniowym prostym.
# W tym algorytmie każdy znak tekstu jawnego jest zastępowany dokładnie jednym znakiem
# z ustalonego klucza. Klucz musi przyjąć formę mapowania litera do litera, i mapowania nie mogą się powtarzać.
# Jeżeli klucz nie zawiera całego alfabetu tekstu jawnego lub posiada powtarzające się mapowania, to algorytm nie działa.
# W tej implementacji klucz jest w postaci stringa, gdzie każdy index reprezentuje literę zaszyfrowaną.
# (ale może być też np. tablicą czy dictionary)
# np. klucz "BCA" oznacza, że "A" (indeks 0) zostanie zaszyfrowany jako "B", "B" jako "C", "C" jako "A",
# Uwaga: Poniższy algorytm działa tylko dla alfabetu A-Z.

def szyfruj(tekst, klucz):
    output = ""
    podstawa = ord("A")
    for c in tekst:
        index = ord(c) - podstawa
        output += klucz[index]

    return output

# Odszyfrowanie jest analogiczne do szyfrowania, jednak zamiast wybierać znak z klucza w danym indeksie
# To wyszukujemy na jakim indeksie w kluczu znajduje się zaszyfrowany znak.
def odszyfruj(tekst, klucz):
    output = ""
    podstawa = ord("A")
    for c in tekst:
        index = klucz.index(c)
        output += chr(index + podstawa)

    return output

# Przykłady użycia:
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
klucz = "".join(random.sample(alfabet, len(alfabet)))
print("Wylosowany klucz: " + klucz)

zaszyfrowane = szyfruj("SZYFRPODSTAWIENIOWY", klucz)
odszyfrowane = odszyfruj(zaszyfrowane, klucz)
print(f"Zaszyfrowany tekst: {zaszyfrowane}")
print(f"Odszyfrowany tekst: {odszyfrowane}")