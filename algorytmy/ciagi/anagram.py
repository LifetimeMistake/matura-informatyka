# Anagram to wyrażenie, które powstało z przestawienia liter innego wyrażenia. 
# Liczba poszczególnych znaków w obu wyrażeniach musi być równa. Przykładowo:
# dla wyrazu `tok` anagramem jest `kot`. Widać, że w obu przypadkach wykorzystano tyle samo liter.
# Ponadto można stwierdzić, że oba wyrażenia muszą być takiej samej długości,
# więc jeśli ten warunek nie jest spełniony to od razu można stwierdzić, że wyrażenia nie są anagramami.

# Sprawdzenie anagramu odbywa się poprzez zliczenie wszystkich liter w obu wyrażeniach i sprawdzenie,
# czy liczba takich samych liter jest równa.
def czy_anagram(wyrazenie1: str, wyrazenie2: str) -> bool:
    # Warunek długości
    if len(wyrazenie1) != len(wyrazenie2):
        return False
    
    litery1 = {}
    litery2 = {}
    for litera in wyrazenie1:
        litery1[litera] = litery1.get(litera, 0) + 1
    for litera in wyrazenie2:
        litery2[litera] = litery2.get(litera, 0) + 1

    # Python posiada odpowiedni operator porównania dla słowników
    # Sprawdza czy istnieją te same klucze i czy ich wartości są równe
    return litery1 == litery2

# Algorytm można też zapisać tylko z jedną tablicą pomocniczą.
def czy_anagram2(wyrazenie1: str, wyrazenie2: str) -> bool:
    if len(wyrazenie1) != len(wyrazenie2):
        return False
    
    litery = {}
    for i in range(len(wyrazenie1)):
        # Dodajemy litery z wyrażenia 1,
        # a odejmujemy litery z wyrażenia 2
        litery[wyrazenie1[i]] = litery.get(wyrazenie1[i], 0) + 1
        litery[wyrazenie2[i]] = litery.get(wyrazenie2[i], 0) - 1
    
    # Jeśli dla każdej napotkanej litery jej zliczona wartośc jest równa zero,
    # to wyrażenia są anagramami
    return all(v == 0 for v in litery.values())

# Można też skusić się na zapisanie algorytmu w taki sposób, że nie potrzeba ani jednej tablicy.
def czy_anagram3(wyrazenie1: str, wyrazenie2: str) -> bool:
    if len(wyrazenie1) != len(wyrazenie2):
        return False
    
    # Sortujemy oba wyrażenia po ich literach
    wyrazenie1 = list(wyrazenie1).sort()
    wyrazenie2 = list(wyrazenie2).sort()

    # Jeśli wyrażenia są anagramami to ich posortowane wersje powinny być identyczne
    return wyrazenie1 == wyrazenie2

# Przykłady użycia:
print(czy_anagram("tok", "kot"))  # True
print(czy_anagram("kino", "ikon")) # True
print(czy_anagram("dom", "mood"))    # False
print(czy_anagram("słowo", "włos"))    # False