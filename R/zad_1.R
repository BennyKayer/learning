# ZAD 1
# (Miary klasyczne) Obliczono wielkosci dochodu w pieciu małych firmach oznaczonych
# literami A, B, C, D, E i otrzymano nastepujace wyniki (w tys. zł.):

#x = c(1.71, 2.98, 3.4, 2.17, 1.42)
x = c(98,55,31,49,80)

# PODPUNKT 1
# Przedstaw otrzymane dane w postaci wykresu punktowego w układzie współrzednych.
# Latwiej to narysowac, tutaj to jest ciezka sprawa
print('')

# PODPUNKT 2
# Oblicz srednia z próby ¯x dla tych danych według wzoru
x_mean = mean(x)
x_round = round(mean(x), 2)
print('Srednia z proby wynosi')
print(x_mean)

# PODPUNKT 3
# Narysuj na wykresie linie y = ¯x (linia pozioma na wysokosci wartosci sredniej z próby) i dla
# kazdego pomiaru zaznacz róznice miedzy wartoscia pomiaru a srednia z próby.
# To byla prawdziwa rzeznia duzo latwiej narysowac na kartce
print('')

# PODPUNKT 4
# Oblicz wariancje z próby sigma ^ 2 i odchylenie standardowe z próby sigma według wzoru
# Tu trzeba poprzeksztalcac bo R ma jakies tam praktyczne wzory
sigma_kwadrat = var(x) * 4/5
sigma = sd(x) * sqrt(4/5)
print('Sigma^2 wynosi')
print(sigma_kwadrat)
print('Sigma wynosi')
print(sigma)

# PODPUNKT 5
# Oblicz estymator wariancji s2 i odchylenia standardowego s według wzoru
# Var to estymator wariancji - liczy ten s2
s_kwadrat = var(x)
s = sd(x)
print('Estymator wariancji s^2 wynosi')
print(s_kwadrat)
print('Odchylenie standardowe s wynosi')
print(s)

# PODPUNKT 6
# Oblicz współczynnik zmiennosci według ponizszego wzoru. Zinterpretuj otrzymany wynik.
wspolczynnik_zmiennosci = sigma / x_mean
print(wspolczynnik_zmiennosci)

# PODPUNKT 7
# Wyznacz przedziały [¯x − sigma, ¯x + sigma], [¯x − 2sigma, ¯x + 2sigma] i zinterpretuj otrzymany wynik.
# Nie ma sensu robic tego w R












