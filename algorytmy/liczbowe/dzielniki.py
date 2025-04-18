# Algorytm znajdujący wszystkie dzielniki danej liczby naturalnej
# Dzielnik liczby to taka liczba, przez którą dana liczba dzieli się bez reszty
# Przykład: dzielniki liczby 12 to: 1, 2, 3, 4, 6, 12
# Optymalizacja: wystarczy sprawdzać dzielniki tylko do pierwiastka z liczby,
# ponieważ dzielniki występują w parach (np. dla 36: 2×18, 3×12, 4×9, 6×6)
# Znajdując jeden dzielnik, automatycznie znamy drugi z pary
# x/y = z, x/z = y

def dzielniki(liczba):
    # Nie istnieją dzielniki całkowite mniejsze niż 1
    if liczba < 1:
        return []
        
    dzielniki = [1]  # 1 jest zawsze dzielnikiem
    if liczba == 1:
        return dzielniki
        
    # Sprawdzamy dzielniki od 2 do pierwiastka z liczby
    for i in range(2, int(liczba**0.5) + 1):
        if liczba % i == 0:
            dzielniki.append(i)
            # Dodajemy również drugi dzielnik (liczba/i)
            if i != liczba // i:
                dzielniki.append(liczba // i)
                
    dzielniki.append(liczba)  # Liczba sama w sobie jest zawsze dzielnikiem
    return sorted(dzielniki) # ! Dzielniki mogą być opcjonalnie posortowane według uznania

# Przykłady użycia:
print(dzielniki(12))  # [1, 2, 3, 4, 6, 12]
print(dzielniki(17))  # [1, 17] - liczba pierwsza
print(dzielniki(1))   # [1]
print(dzielniki(0))   # []