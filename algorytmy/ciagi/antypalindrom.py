# Antypalindrom to ciąg, w którym podczas sprawdzania palindromowości
# nie występuje żadna para liter równa sobie.
# Przykład:
# 7111190009, ponieważ: 7≠9, 1≠0, 1≠0, 1≠0, 1≠9

def czy_antypalindrom(ciag: str) -> bool:
    for i in range(len(ciag) // 2):
        if ciag[i] == ciag[-i - 1]:
            return False
        
    return True

# Przykłady użycia:
print(czy_antypalindrom("2001030035")) # False
print(czy_antypalindrom("0010100001")) # False
print(czy_antypalindrom("7111190009")) # True
print(czy_antypalindrom("5550001110")) # False
print(czy_antypalindrom("0000000005")) # False