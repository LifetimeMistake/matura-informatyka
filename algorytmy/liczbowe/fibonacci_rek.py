# Ciąg Fibonacciego to sekwencja liczb, gdzie każda kolejna liczba jest sumą dwóch poprzednich.
# Wzór rekurencyjny: F(n) = F(n-1) + F(n-2) z założeniem, że:
# F(0) = 0, F(1) = 1

# Poniższy algorytm realizuje to podejście dokładnie tak, jak definiuje je wzór rekurencyjny.
# Minusem tego rozwiązania jest jego wydajność – działa bardzo wolno dla dużych wartości n,
# ponieważ wiele wartości jest przeliczanych wielokrotnie.
# Można to zoptymalizować np. przez zapamiętywanie wyników (tzw. memoizacja).

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Przykłady użycia:
print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(5))   # 5
print(fibonacci(10))  # 55
print(fibonacci(36))  # 14930352 (ale trwa długo!)
# print(fibonacci(1000)) # praktycznie niemożliwe do wykonania bez cache'a