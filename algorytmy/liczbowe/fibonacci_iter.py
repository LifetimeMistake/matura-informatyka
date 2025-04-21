# Ciąg Fibonacciego to sekwencja liczb, w której każda liczba (od trzeciej) jest sumą dwóch poprzednich.
# Sekwencja zaczyna się od 0 i 1, czyli:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Poniższy algorytm oblicza n-tą liczbę Fibonacciego w sposób iteracyjny,
# co jest bardzo wydajne i szybkie.

def fibonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    # Obliczamy wyrazy od 2 do n
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Przykłady użycia:
print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(5))   # 5
print(fibonacci(10))  # 55
print(fibonacci(36))  # 14930352 (oblicza się bardzo szybko)
print(fibonacci(1000)) # 434665576869374564356885276750406258025646605173717...