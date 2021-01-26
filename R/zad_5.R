# ZAD 4
# (Miary klasyczne i pozycyjne) Dokonano analizy wyników 44 spółek notowanych na giełdzie
# reprezentujacych ten sam sektor gospodarczy. W okresie od 2009-02-26 do 2009-09-24 zapisywano
# wielkosc spółki [w mln zł] obliczona jako iloczyn liczby akcji i wartosci akcji oraz wskaznik cena/zysk
# [bez miana]. Nastepnie wyniki zostały usrednione w okresie obserwacji. Otrzymane srednie zapisano
# w pliku zadanie5.txt. Wczytasz je poleceniem


# PODPUNKT 1
# Oblicz kwartyle Q1, Q2, i Q3 wielkosci spółek. Spółke uznajemy za
# • bardzo mała - jesli jej wielkosc jest mniejsza lub równa Q1;
# • mała - jesli jej wielkosc jest powyzej Q1 i mniejsza lub równa Q2;
# • srednia - jesli jej wielkosc jest powyzej Q2
# • duza - jesli jej wielkosc jest powyzej Q3.
dane <- read.table(file = "zadanie5.txt", header = TRUE, sep = ";")
wielkosc <- dane[1]
cz <- dane[2]
q1 <- quantile(wielkosc$wielkosc, 0.25, type = 6)
q2 <- quantile(wielkosc$wielkosc, 0.50, type = 6)
q3 <- quantile(wielkosc$wielkosc, 0.75, type = 6)

b_male <- c()
male <- c()
srednie <- c()
duze <- c()

cz <- dane$C.Z
for (e in dane$wielkosc) {
  index <- which(e == dane)
  
  if (e <= q1) {
    b_male <- append(b_male, cz[index])
  } else if (e > q1 && e <= q2) {
    male <- append(male, cz[index])
  } else if (e > q2 && e <= q3) {
    srednie <- append(srednie, cz[index])
  } else if (e > q3) {
    duze <- append(duze, cz[index])
  }
}
rozwiazanie <- c(
  c("bardzo male", mean(b_male), median(b_male), sd(b_male)),
  c("male", mean(male), median(male), sd(male)),
  c("srednie", mean(srednie), median(srednie), sd(srednie)),
  c("duze", mean(duze), median(duze), sd(duze))
)
ret <- matrix(rozwiazanie, ncol = 4, byrow = TRUE)
colnames(ret) <- c("grupa", "srednia", "mediana", "odchylenie")
print(b_male)
print(ret)