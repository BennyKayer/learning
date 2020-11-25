# ZAD 3
# (Indeksy ³ancuchowe i jednopodstawowe) W publikacji "Budzety gospodarstw domowych w
# 2007 r." wydanej przez G³ówny Urzad Statystyczny w serii "Informacje i opracowania statystyczne"
# znajduja sie informacje o przecietnych miesiecznych wydatkach na 1 osobe w gospodarstwach domowych
# w pewnym województwie za lata 2000-2007 w z³.:

dane = c(656.8, 654.53, 611.27, 657.91, 695.72, 768.26, 699.79, 843.47)

# PODPUNKT 1
# R liczy od 1 nie od 0
i = c(dane[2:8]/dane[1:7])
print("Wszystkie indexy lacuchowe od i_1 do i_n")
print(i)

# PODPUNKT 2
j = c(dane[2:8]/dane[1])
print("Indexy jednopodstawowe gdzie podstawa jest rok 2000")
print(j)

# PODPUNKT 3
ig = (dane[8] / dane[1]) ^ (1/7)
print('Sredni index lancuchowy wynosi')
print(ig)
