# ZAD 2
# (Miary pozycyjne) Obliczono wielkosci wynagrodzenia (w tys. zł.) w pewnej grupie
# pracowników i otrzymano nastepujace wyniki

dane = c(3.84, 7.07, 6.86, 5.38, 4.41, 6.61, 6.39, 7.62, 3.4, 5.18, 3.6, 7.02)

# PODPUNKT 1
# Narysuj histogram liczebnosci o jednostkowej długosci przedziałów klasowych dla tych danych.
hist(dane)

# PODPUNKT 2
# Oblicz kwartyle według ponizszych wzorów. Zinterpretuj otrzymane wyniki.
# Te wzory sa do dupy latwiej dac tu typ 6 i elo
# domyslnie jest typ 7
q1 = quantile(dane, 0.25, type=6)
print('Q1')
print(q1)
me = quantile(dane, 0.50, type=6)
print('Mediana')
print(me)
q3 = quantile(dane, 0.75, type=6)
print('Q3')
print(q3)

# PODPUNKT 3
# Oblicz rozstep według wzoru R = max xi − min xi
print('R - rozstep = ')
print(max(dane) - min(dane))

# PODPUNKT 4
# Oblicz odchylenie cwiartkowe według wzoru
q = (q3 - q1) / 2
print('Odchylenie cwiartkowe Q = ')
print(q)

# PODPUNKT 5
# Oblicz współczynnik zmiennosci w relacji do mediany. Zinterpretuj otrzymany wynik.
print('V(Q) => współczynnik zmiennosci w relacji do mediany = ')
print(q / me)

# PODPUNKT 6
# Oblicz współczynnik asymetrii w relacji do mediany. Zinterpretuj otrzymany wynik.
print('A(Q) => współczynnik asymetrii w relacji do mediany = ')
print((q3 - (2 * me) + q1) / (q3 - q1) )
