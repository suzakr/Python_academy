# 1. pomocí cyklu for vypište čísla ze seznamu numbers, ale přeskočte záporná čísla.

# 2. pomocí cyklu while vypište všechna jména, pokud narazíš na jméno 'Alice' cyklus ukonči

# 3. pomocí list comprehension vytvoř nový list, který bude obsahovat pouze prvky z 'random_codes', které obsahují 0

# Dobrovolny ukol pro pokrocile (nebude bodovan): Vypis všechny pod-seznamy s alespoň třemi po sobě jdoucími stejnými znaky v seznamu 'random_codes'

numbers = [1, 2, 4, -6, 7, 8, 100, -125, 11, 123]
names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa", "3-sOdSxhcds"]

# 1. Vypsani cisel bez zapornych cisel:

for number in numbers:
    if number < 0:
        continue
    print(number)

# 2. Vypsani jmen az po Alici:

is_True = True

while is_True:
    for name in names:
        if "Alice" in name:
            break
        print(name)
    is_True = False

# 3. Zapsani z listu do listu pouze s "0":

list_0 = [code_0 for code_0 in random_codes if "0" in code_0]
print(list_0)

# 4. Tri po sobe jdouci znaky:


x = len(random_codes)
# z = []

is_running = True
while is_running:
    for i in range(0, x):
        for char in random_codes[i]:
            if char*3 in random_codes[i]:
                # z.append(random_codes[i])
                print(random_codes[i])
                break
            continue

        is_running = False

# print(z)

# Zakomentovaná je část pro případné zapsání hodnot do listu "z"
# Nebudu lhát, ten bonusový úkol byl hodně těžký...