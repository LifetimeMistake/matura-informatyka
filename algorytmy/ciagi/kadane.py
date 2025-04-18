# Algorytm Kadane służy do znalezienia podciągu o największej sumie w danym ciągu liczb.
# Działa w czasie liniowym O(n) i jest jednym z najefektywniejszych rozwiązań tego problemu.
# 
# Zasada działania:
# 1. Przechodzimy przez ciąg element po elemencie
# 2. Dla każdego elementu decydujemy, czy:
#    - kontynuować obecny podciąg (dodać element do aktualnej sumy)
#    - czy rozpocząć nowy podciąg od tego elementu
# 3. Wybór zależy od tego, która opcja da większą sumę:
#    - suma dotychczasowa + aktualny element
#    - czy sam aktualny element
# 4. W każdym kroku aktualizujemy maksymalną znalezioną sumę
# 
# Przykład:
# Dla ciągu [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Największy podciąg to [4, -1, 2, 1] o sumie 6

# Minimalna implementacja Kadana (szuka tylko największej sumy)
def kadane(ciag):
    max_suma = suma = ciag[0]
    
    for num in ciag:
        suma = max(num, suma + num)
        max_suma = max(max_suma, suma)
        
    return max_suma

# Minimalna implementacja Kadana (szuka największej sumy i indeksów początku i końca)
def kadane2(ciag):
    max_suma = suma = ciag[0]
    start = end = obecny_start = 0
    
    for i in range(1, len(ciag)):
        if suma + ciag[i] < ciag[i]:
            suma = ciag[i]
            obecny_start = i
        else:
            suma += ciag[i]
            
        if suma > max_suma:
            max_suma = suma
            start = obecny_start
            end = i
            
    return max_suma, start, end


# Rozpisana implementacja Kadana
def _kadane(ciag):
    # Inicjalizacja zmiennych
    max_suma = ciag[0]  # Największa dotychczas znaleziona suma
    suma = ciag[0]      # Suma aktualnego podciągu (początkowo równa pierwszemu elementowi)
    start = 0           # Indeks początku najlepszego podciągu
    end = 0             # Indeks końca najlepszego podciągu
    obecny_start = 0      # Tymczasowy indeks początku aktualnego podciągu

    # Iteracja przez wszystkie elementy ciągu
    # ! Zaczynamy od drugiego elementu, gdyż pierwszy element jest już dodany przy inicjalizacji
    for i in range(1, len(ciag)):
        # Jeśli suma aktualnego podciągu + kolejny element jest mniejsza niż sam element,
        # oznacza to, że kontynuowanie obecnego podciągu zmniejszyłoby jego sumę.
        # W takim przypadku lepiej jest zrestartować podciąg od obecnego elementu,
        # ponieważ zaczynając od niego mamy szansę na znalezienie lepszego podciągu.
        # Jest to istotne jedynie gdy mamy do czynienia z ujemnymi liczbami,
        # w przeciwnym wypadku największą sumą ciągu jest cały ciąg (gdy ciąg nie ma elementów ujemnych)
        if suma + ciag[i] < ciag[i]:
            suma = ciag[i]
            obecny_start = i
        else:
            # W przeciwnym razie kontynuujemy aktualny podciąg
            suma += ciag[i]

        # Jeśli znaleźliśmy lepszy podciąg, aktualizujemy najlepsze wyniki
        if suma > max_suma:
            max_suma = suma
            start = obecny_start
            end = i

    return max_suma, start, end

# Przykład użycia
if __name__ == "__main__":
    # Przykładowe ciągi
    ciag1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ciag2 = [1, 2, 3, 4, 5]
    ciag3 = [-1, -2, -3, -4, -5]
    
    # Testowanie pierwszej implementacji
    print("Implementacja 1:")
    print(f"ciag1: {kadane(ciag1)}")  # Powinno zwrócić 6
    print(f"ciag2: {kadane(ciag2)}")  # Powinno zwrócić 15
    print(f"ciag3: {kadane(ciag3)}")  # Powinno zwrócić -1
    
    # Testowanie drugiej implementacji
    print("\nImplementacja 2:")
    suma1, start1, end1 = kadane2(ciag1)
    print(f"ciag1: suma = {suma1}, indeksy = [{start1}, {end1}]")
    
    suma2, start2, end2 = kadane2(ciag2)
    print(f"ciag2: suma = {suma2}, indeksy = [{start2}, {end2}]")
    
    suma3, start3, end3 = kadane2(ciag3)
    print(f"ciag3: suma = {suma3}, indeksy = [{start3}, {end3}]")
