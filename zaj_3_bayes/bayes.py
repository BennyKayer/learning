import yaml
from pathlib import Path

file_to_open = Path("zaj_3_bayes/") / "choroby1.yaml"
file = open(file_to_open, "r", encoding='utf8')
data = yaml.safe_load(file)


print("Hipoteza, prawdopodobieństwo a priori (1/100%):")
for h in data["Hypotheses"]:
    print("{}, {}".format(h["name"], h["prob"]))

print()
print("POJEDYNCZE FAKTY")

Pr_f = []
for fact in data["Facts"]:
    sum = 0
    for index, h in enumerate(data["Hypotheses"]):
        sum = sum + h["prob"]*fact["prob"][index]
    Pr_f.append([fact["name"], round(sum, 5)])

print("Fakt, prawdopodobieństwo (1/100%):")
for x in Pr_f:
    print(*x, sep=", ")


Pr_h_f = []
for indexh, h in enumerate(data["Hypotheses"]):
    for indexf, fact in enumerate(data["Facts"]):
        pr = round(h["prob"]*fact["prob"][indexh] / Pr_f[indexf][1], 5)
        Pr_h_f.append([h["name"], fact["name"], pr])

print()
print("Hipoteza, fakt, prawdopodobieństwo (1/100%):")
for x in Pr_h_f:
    print(*x, sep=', ')


print()
print("KILKA FAKTÓW JEDNOCZEŚNIE")
print("Fakty:")
for index, fact in enumerate(data["Facts"]):
    print(index, fact["name"])


ok = False
while not ok:
    selected_facts_indexes = sorted(
        input("Podaj numery objawów, oddzielając je spacjami: ").split())
    # Convert to int
    selected_facts_indexes = [int(i) for i in selected_facts_indexes]
    # Remove duplicates
    selected_facts_indexes = list(dict.fromkeys(selected_facts_indexes))
    # Check if a provided numbers are allowed
    ok = set(selected_facts_indexes).issubset(range(len(data["Facts"])))

selected_facts = [data["Facts"][int(i)]["name"]
                  for i in selected_facts_indexes]


'''
Zadanie: uzupełnić program tak, aby uwzględniał dowolne zestawy faktów
i wyświetlał je tak, jak poniżej.

'''

Pr_h_fk = []
for ih, h in enumerate(data["Hypotheses"]):
    il = 1
    for ifact, selected_fact in enumerate(selected_facts):
        for jfact, fact in enumerate(data["Facts"]):
            if selected_fact == fact["name"]:
                il *= fact["prob"][ih]
    licznik = h["prob"] * il

    mianownik = 0
    for ihl, hl in enumerate(data["Hypotheses"]):
        il = 1
        for ifact, selected_fact in enumerate(selected_facts):
            for jfact, fact in enumerate(data["Facts"]):
                if selected_fact == fact["name"]:
                    il *= fact["prob"][ihl]
        mianownik += hl["prob"] * il

    Pr_h_fk.append(licznik / mianownik)


print()
for i, h in enumerate(data["Hypotheses"]):
    print("Prawdopodobieństwo hipotezy {} przy uwzględnieniu faktów ({}) wynosi: {}%.".format(
        h["name"], ', '.join(selected_facts), round(Pr_h_fk[i] * 100, 2)))
