# XOR to algorytm szyfrujący, który dla każdego znaku tekstu jawnego
# wykonuje operację XOR z kawałkiem klucza. Jeżeli klucz jest krótszy
# niż tekst wejściowy, to klucz jest powtarzany tyle razy ile trzeba.

def xor(tekst, klucz):
    output = ""

    for i in range(len(tekst)):
        output += chr(ord(tekst[i]) ^ ord(klucz[i % len(klucz)]))

    return output

# Odszyfrowanie jest analogiczne do szyfrowania, gdyż operacja XOR jest symetryczna.
# W odróżnieniu od innych szyfrów, szyfr XOR nie gwarantuje, że zaszyfrowany tekst jest
# złożony z czytelnych znaków. Dlatego właśnie zaszyfrowane teksty mogą nie renderować
# się poprawnie. Zamiast tego lepiej jest posługiwać się szesnastkową reprezentacją bajtów
# na które składa się zaszyfrowany tekst.