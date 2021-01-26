'''
Plik dane.csv zawiera dane zbierane na węźle ciepłowniczym przez 
przedsiębiorstwo dostarczające ciepło do budynku (patrz opisy kolumn w pliku). 
Napisać skrypt w języku Python, dokonujący podstawowej analizy tych danych.
'''

# A. Wczytanie obserwacji dla wybranych zmiennych.
import csv
import numpy as np
import matplotlib.pyplot as plt
import pathlib

data_folder = pathlib.Path("data")
dane_csv = data_folder / "dane.csv"
plik = open(dane_csv, "r")
dane = csv.reader(plik, delimiter=",")
przeplyw, temp_zas, temp_pow, rozn_temp, moc = [], [], [], [], []

next(dane)  # nagłówek zbędny
for row in dane:
    przeplyw.append(float(row[6]))
    temp_zas.append(float(row[7]))
    temp_pow.append(float(row[8]))
    rozn_temp.append(float(row[9]))
    moc.append(float(row[12]))
plik.close()

przeplyw.reverse()
temp_zas.reverse()
temp_pow.reverse()
rozn_temp.reverse()
moc.reverse()
# B. Sprawdzenie podstawowych statystyk dla poszczególnych zmiennych.
#    Wykreślenie histogramów.


def wyswietl_statystyki(nazwa_zmiennej, zmienna):
    print(f"\nSTATYSTYKI DLA ZMIENNEJ {nazwa_zmiennej}")
    print("min: ", min(zmienna))
    print("max: ", max(zmienna))
    print("srednia: ", np.mean(zmienna))  # print(sum(moc) / len(moc))
    print("mediana: ", np.median(zmienna))
    print("odchylenie standardowe: ", np.std(zmienna))


def wyswietl_histogram(zmienna):
    print("histogram", np.histogram(zmienna))
    plt.hist(zmienna, 10)
    plt.show()


# C. Identyfikacja zmiennych, w których występują potencjalnie błędne dane (obserwacje)
#    lub braki danych. Naprawa danych.

# Poprawa mocy
mediana_mocy = np.median(moc)
for index, wartosc in enumerate(moc):
    if wartosc > 1000:
        moc[index] = mediana_mocy

mediana_przeplywu = np.median(przeplyw)
for index, wartosc in enumerate(przeplyw):
    if wartosc > 10000:
        przeplyw[index] = mediana_przeplywu

for index, wartosc in enumerate(rozn_temp):
    if wartosc > 1000:
        prawdziwa_roznica = temp_zas[index] - temp_pow[index]
        prawdziwa_roznica = abs(prawdziwa_roznica)
        prawdziwa_roznica = round(prawdziwa_roznica, 2)
        rozn_temp[index] = prawdziwa_roznica
        # print(f"rozn_temp {rozn_temp[index]}, temp_zas {temp_zas[index]}, temp_pow {temp_pow[index]}")
# D. Obliczenie unormowanych korelacji pomiędzy poszczególnymi zmiennymi.


def correlate_normalize(a, b):
    a = (a - np.mean(a)) / (np.std(a) * len(a))
    b = (b - np.mean(b)) / (np.std(b))
    return np.correlate(a, b)


# E. Przeprowadzenie regresji liniowej dla wybranych zmiennych, wraz z wykresami.
r1 = len(moc) // 3  # 3 etapy ciągłości
r2 = r1 * 2
x = range(r1)
y = moc[:r1]
a, b = np.polyfit(x, y, 1)
yreg = [a * i + b for i in x]
plt.plot(x, y)
plt.plot(x, yreg)
plt.show()

x = range(r1)
y = moc[r1:r2]
a, b = np.polyfit(x, y, 1)
yreg = [a * i + b for i in x]
plt.plot(x, y)
plt.plot(x, yreg)
plt.show()

x = range(r1)
y = moc[r2+1:]
a, b = np.polyfit(x, y, 1)
yreg = [a * i + b for i in x]
plt.plot(x, y)
plt.plot(x, yreg)
plt.show()

# Combined
r1 = len(moc)
x = range(r1)
y = moc
a, b = np.polyfit(x, y, 1)
yreg = [a * i + b for i in x]
plt.plot(x, y)
plt.plot(x, yreg)
plt.show()


x = range(len(moc))
y = moc
a, b, c = np.polyfit(x, y, 2)
yreg = [a * i ** 2 + i * b + c for i in x]
plt.plot(x, y)
plt.plot(x, yreg)
plt.show()

x = moc
y = temp_zas
a, b = np.polyfit(x, y, 1)
yreg = [a * i + b for i in x]
# 45.3672, 81.3815
print(a * 45.3672 + b)
plt.plot(moc, temp_zas, ".")
plt.plot(x, yreg)
plt.show()

x = moc
y = przeplyw
a, b = np.polyfit(x, y, 1)
yreg = [a * i + b for i in x]
plt.plot(moc, przeplyw, ".")
plt.plot(x, yreg)
plt.show()

# F. Wykorzystanie wyników regresji dla podstawowej predykcji wyników.
# zapytaj podaj zadana moc i na tej podstawie wypisal temp_zas itd.

user_input = input("Insert some x for prediction: ")
print(f"For given x predicted y is {a * float(user_input) + b}")

if __name__ == "__main__":
    pass
    # B. Sprawdzenie podstawowych statystyk dla poszczególnych zmiennych.
    # Wykreślenie histogramów.
    wyswietl_statystyki("przeplyw", przeplyw)
    wyswietl_statystyki("moc", moc)
    wyswietl_statystyki("temp_zas", temp_zas)
    wyswietl_statystyki("temp_pow", temp_pow)
    wyswietl_statystyki("rozn_temp", rozn_temp)

    # D. Obliczenie unormowanych korelacji pomiędzy poszczególnymi zmiennymi.
    print("korelacja pomiedzy moc a temp_zas: ",
          correlate_normalize(moc, temp_zas))
    print("korelacja pomiedzy moc a temp_pow: ",
          correlate_normalize(moc, temp_pow))
    print("korelacja pomiedzy moc a przeplyw: ",
          correlate_normalize(moc, przeplyw))

    print("korelacja pomiedzy przeplyw a temp_pow: ",
          correlate_normalize(przeplyw, temp_pow))
    print("korelacja pomiedzy przeplyw a temp_zas: ",
          correlate_normalize(przeplyw, temp_zas))

    print("korelacja pomiedzy temp_zas a temp_pow: ",
          correlate_normalize(temp_zas, temp_pow))

    plt.plot(range(len(moc)), moc, "+")
    plt.plot(range(len(temp_zas)), temp_zas, "x")
    plt.show()

    # dlaczego roznica wychodzi dziwna - fizycznie i informatycznie
    # badanie korelacji miedzy danymi, czyszczenie
