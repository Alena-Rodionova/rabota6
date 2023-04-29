countries_dict = {"Австрия": "Вена", "Нидерланды":	"Амстердам",
                  "Андорра":	"Андорра-ла-Велья",
                  "Греция":	"Афины",
                  "Сербия": "Белград",
                  "Германия":	"Берлин",
                  "Швейцария":	"Берн",
                  "Словакия":	"Братислава",
                  "Бельгия":	"Брюссель",
                  "Венгрия":	"Будапешт",
                  "Румыния": "Бухарест"}

print("a) ", countries_dict)
K=input('b) Введите страну ')
if K in countries_dict:
    print(countries_dict[K])
else: print("Страна не найдена в словаре")
print("c)")
for key in sorted(countries_dict):
    print(key, " - ", countries_dict[key])
