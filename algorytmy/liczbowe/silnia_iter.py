# Silnia (factorial) - iloczyn wszystkich liczb naturalnych od 1 do n
# Oznaczana jako n!
# Przykład: 5! = 1 * 2 * 3 * 4 * 5 = 120
# Specjalne przypadki:
# - 0! = 1 (z definicji)
# - 1! = 1
# Silnia rośnie bardzo szybko, już dla n=20 wynik przekracza zakres standardowych typów całkowitych

def silnia(n):
    if n == 0 or n == 1:
        return 1
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik

# Przykłady użycia:
print(f"5! = {silnia(5)}")  # 120
print(f"10! = {silnia(10)}")  # 3628800
print(f"0! = {silnia(0)}")  # 1