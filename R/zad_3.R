# ZAD 3
# (Indeksy �ancuchowe i jednopodstawowe) W publikacji "Budzety gospodarstw domowych w
# 2007 r." wydanej przez G��wny Urzad Statystyczny w serii "Informacje i opracowania statystyczne"
# znajduja sie informacje o przecietnych miesiecznych wydatkach na 1 osobe w gospodarstwach domowych
# w pewnym wojew�dztwie za lata 2000-2007 w z�.:

#dane = c(656.8, 654.53, 611.27, 657.91, 695.72, 768.26, 699.79, 843.47)
dane = c(48.3, 51.4, 58.5, 55.3, 62.4, 63.1, 62.0, 67.2)

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
