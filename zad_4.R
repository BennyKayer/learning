# ZAD 4
# Metody wygładzania danych) Dla danych z poprzedniego zadania zastosuj wygładzanie
# danych metoda

dane = c(656.8, 654.53, 611.27, 657.91, 695.72, 768.26, 699.79, 843.47)

# PODPUNKT 1
# sredniej ruchomej 3-okresowej
Srednia = function(wektor, k) {
  a = c()
  for (i in 1 : (length(wektor) - k + 1)) {
    a = c(a, mean(wektor[i:(i + k - 1)]))
  }
  return (a)
}
# albo
Srednia_2 = function(wektor) {
  a = c()
  for (i in 1:6) {
    a = c(a, mean(wektor[i:(i + 2)]))
  }
  return (a)
}

# PODPUNKT 2
# ruchomej mediany 3-okresowej

Mediana = function(wektor, k) {
  a = c()
  for (i in 1 : (length(wektor) - k + 1)){
    a = c(a, median(wektor[i:(i + k - 1)]))
  }
  return (a)
}

# PODPUNKT 3
# kroczacego minimum 3-okresowego:

Minimum = function(wektor, k) {
  a = c()
  for (i in 1 : (length(wektor) - k + 1)){
    a = c(a, min(wektor[i : (i + k - 1)]))
  }
  return (a)
}

# PODPUNKT 4
# kroczacego maksimum 3-okresowego:

Maximum = function(wektor, k) {
  a = c()
  for (i in 1 : (length(wektor) - k + 1)){
    a = c(a, max(wektor[i : (i + k - 1)]))
  }
  return (a)
}

# WYKRESY
Srednia_ruch = c(NA, Srednia(dane, 3), NA)
Mediana_ruch = c(NA, Mediana(dane, 3), NA)
Kroczace_min = c(NA, Minimum(dane, 3), NA)
Kroczace_max = c(NA, Maximum(dane, 3), NA)

# n - bez pkt i lini
plot(dane, type='n', xlab="Rok", ylab="Wydatki", main="Przecietne wynagrodzenie", axes=FALSE)
# 1 - x w prawo, 2 - y w góre, 3 - x w lewo, 4 - y w dól
axis(1, at=1:8, labels=c(2000:2007))
axis(2, ylim=c())

# b - pkt polaczone liniami
lines(dane, lwd=2, type='b', col='black')
lines(Srednia_ruch, lwd=2, type='b', col='red')
lines(Mediana_ruch, lwd=2, type='b', col='blue')
lines(Kroczace_min , lwd=2, type='b', col='green')
lines(Kroczace_max , lwd=2, type='b', col='purple')

# Legenda kolory do wykresow
etykiety=c("Dane", "Srednia", "Mediana" ,"Min", "Max")
colors=c("black", "red", "blue", "purple", "green")
legend("bottomright", legend=etykiety, fill=colors)
box()