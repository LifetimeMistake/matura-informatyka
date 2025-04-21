# Palindrom to ciąg, który po odwróceniu jest taki sam jak oryginał.

# Sprawdzenie palindromu za pomocą indeksowania
def czy_palindrom(ciag: str) -> bool:
    return ciag == ciag[::-1]

# Sprawdzenie palindromu za pomocą pętli
def czy_palindrom2(ciag: str) -> bool:
    for i in range(len(ciag) // 2):
        if ciag[i] != ciag[-i - 1]:
            return False
        
    return True

# Przykłady użycia:
print(czy_palindrom("radar"))  # True
print(czy_palindrom("radar2")) # False
print(czy_palindrom("abc"))    # False
print(czy_palindrom("cba"))    # False