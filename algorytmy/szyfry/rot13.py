# Szyfr ROT-N to prosty podstawieniowy szyfr, który podstawia każdą literę wiadomości
# inną literą następującą w alfabecie N miejsc po oryginale.
# Jest on uogólnieniem szyfru ROT-13 (szyfr Cezara), który przesuwa każdą literę wiadomości o 13 miejsc.
# Przykład:
# Rot13("Algorytm") -> Nytbelgz

# Minimalna implementacja ROT-13:
def rot13(wiadomosc):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""

    for c in wiadomosc:
        index = alfabet.index(c)
        output += alfabet[(index + 13) % len(alfabet)]

    return output

# Ogólna implementacja ROT-N:
def rotN(wiadomosc, n):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""

    # Zamieniamy każdą literę wiadomości na następującą w alfabecie N miejsc po oryginale
    for c in wiadomosc:
        if c in alfabet:
            index = alfabet.index(c)
            output += alfabet[(index + n) % len(alfabet)]
        else:
            # Jeżeli litera nie istnieje w alfabecie to pozostawiamy ją bez zmian
            output += c

    return output

# Aby odszyfrować wiadomość należy użyć operacji odwrotnej (np. dla N = 5 należy zastosować N = -5).
# Specjalnym przypadkiem jest ponownie ROT-13, gdyż przesunięcie jest równe dokładnie połowie długości alfabetu.
# Ponowne zastosowanie funkcji na zaszyfrowanym tekście powoduje jego odszyfrowanie:
# Rot13(Rot13("Algorytm")) -> Algorytm

# Przykłady użycia:
print(rot13("ALGORYTM"))  # NYTBELGZ
print(rotN("ALGORYTM", 13))  # NYTBELGZ
print(rotN("HELLO WORLD", 5)) # MJQQT BTWQI

# Odszyfrowanie:
print(rot13("NYTBELGZ"))  # ALGORYTM
print(rotN("MJQQT BTWQI", -5)) # HELLO WORLD
