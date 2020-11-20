x = c(1.71, 2.98, 3.4, 2.17, 1.42)
x_mean = mean(x)
x_round = round(mean(x), 2)
s_kwadrat = var(x)
sigma_kwadrat = var(x) * 4/5
# Var to estymator wariancji - liczy ten s2
# liczy tym wzorem bo jest bardziej praktyczny
s = sd(x)
# print(s)
sigma = sd(x) * sqrt(4/5)
# print(sigma)
wspolczynnik_zmiennosci = sigma / x_mean
# print(wspolczynnik_zmiennosci * 100, '%')
dane = c(3.84, 7.07, 6.86, 5.38, 4.41, 6.61, 6.39, 7.62, 3.4, 5.18, 3.6, 7.02)
hist(dane)
sort(dane)
i = .25 * 12
j = i + 1
# 3.84 i 4.41
# to jest zle
# q_1 = 3.84 + .25 * (4.41 - 3.84)
# print(q_1)
# me = 3.84 + .50 * (4.41 - 3.84)
# print(me)
# q_3 = 3.84 + .75 * (4.41 - 3.84)
# print(q_3)
quantile(dane, 0.25, type=6)
quantile(dane, 0.50, type=6)
quantile(dane, 0.75, type=6)
# domyslnie jest typ 7










