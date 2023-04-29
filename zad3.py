import random

stud = {"Жуков", "Попов", "Иванова", "Сидоров", "Васильева", "Ралдугин", "Лебедев", "Жихарева"}
languages = {"Итальянский", "Английский", "Французский", "Немецкий", "Китайский"}

lang_stud = {}

for st in stud:
    s = random.randint(1,3)
    lang_stud[st] = random.sample(list(languages), s)

unique_lang = set()
for i in lang_stud:
    unique_lang = unique_lang.union(set(lang_stud[i]))

print(lang_stud)
print("Студенты знают языков", f" {len(unique_lang)}",": ",sorted(unique_lang))

china = [i for i in lang_stud if "Китайский" in lang_stud[i]]
print("Студенты, знающие китайский: ", china)