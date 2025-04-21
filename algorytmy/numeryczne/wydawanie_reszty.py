# Wydawanie reszty to problem w którym należy podzielić liczbę na określone czynniki
# Można go rozwiązać emtodą zachłanną, tj. będziemy po prostu po kolei wydawać banknoty
# bez zastanawiania się jaka kombinacja banknotów jest ta "optymalna"

# Poniższy algorytm działa tylko dla liczb całkowitch.
# Dodatkowo zakłada, że lista nominałów jest posortowana malejąco.
# Jeśli wymagana jest obsługa groszy to można kwotę i nominały pomnożyć przez 100,
# pozbywając się miejsc po przecinku.

def wydawanie_reszty(kwota: int, nominaly: list[int]):
    reszta = {}
    for n in nominaly:
        reszta[n] = kwota // n
        kwota -= reszta[n] * n

    return reszta

# Przykłady użycia:
nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]

print(wydawanie_reszty(1000, nominaly))
print(wydawanie_reszty(523, nominaly))
print(wydawanie_reszty(1234, nominaly))
print(wydawanie_reszty(7157, nominaly))