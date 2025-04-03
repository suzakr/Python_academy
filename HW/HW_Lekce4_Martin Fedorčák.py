"""
Vytvořte program pro určení ceny tramvajových jízdenek.

Program bude pracovat se třemi údaji: věk zákazníka, cena vstupenky a zda je nakupující zaměstnancem tramvajové služby.

Hodnoty pro údaje můžeš určit libovolně přímo v kódu [+0B],
nebo je můžeš načíst z uživatelského vstupu - pomocí funkce input [+1B],
pokud ještě navíc ukončíš program s chybovou hláškou, když je zadaný datový typ špatný, dostaneš [+1B]

Program určí a následně vypíše konečnou cenu na základě těchto kritérií:

Plná cena jízdenky je 45 Kč.
Cestující do 12 let jezdí zdarma.
Cestující mladší 18 let má slevu 50%.
Cestující nad 65 let mají 30% slevu.
Zaměstnanci tramvajové služby mají slevu 80%.
Zaměstnanci tramvajové služby nad 55 let mají jízdenku zdarma.

Bonusový úkol (Pokud ho nebudete mít hotový, nebude to mít vliv na váš celkový výsledek, body za něj nebudou odečítány.):
Při zadání špatného datového typu se program neukonči, ale vyzve uživatele o nové zadání hodnoty.

"""

print("=====  Vítejte v zákaznickém portále DP Ostrava.  =====\n")


while True:
    age = input("Pro správné vypočtení ceny Vašeho jízdného prosím zadejte Váš věk:\n")
    if age.isnumeric() is True:
        print("")
        break
    print("Vámi zadaná hodnota je ve špatném formátu.")

while True:
    dpo = input("Jste zaměstnancem DP Ostrava? (Ano/Ne)\n")
    if dpo.isalpha() is True and dpo == "Ano" or dpo == "Ne":
        print("")
        break
    print("Vámi zadaná hodnota je ve špatném formátu.")

age_int = int(age)
base_price = 45
age_18 = base_price - (base_price / 100 * 50)
age_65 = base_price - (base_price / 100 * 30)
dpo_z = base_price - (base_price / 100 * 80)

if dpo == "Ano":
    dpo = True
elif dpo == "Ne":
    dpo = False
else:
    print("Vámi zadaná informace je v rosporu. Prosím uveďte 'Ano' nebo 'Ne'")


if dpo is True and 15 < age_int <= 55:
    print("Vaše jízdné stojí " + str(dpo_z) + " Korun českých. Budete přesměrováni na platební portál. Děkujeme Vám, že zlepšujete služby naší společnosti!")

elif dpo is False and age_int < 12:
    print("Cestující mladší 12 let s námi cestují bezplatně. Děkujeme Vám, že jste využili našich služeb!")

elif dpo is True and 12 <= age_int <= 15:
    print("Společnost nenabírá zaměstnance mladší 15 let. Vaše jízdné stojí " + str(age_18) + " Korun českých. Budete přesměrováni na platební portál. Děkujeme Vám, že jste využili našich služeb!")

elif dpo is True and age_int < 12:
    print("Společnost nenabírá zaměstnance mladší 15 let, avšak cestující mladší 12 let s námi cestují bezplatně. Děkujeme Vám, že jste využili našich služeb!")

elif dpo is False and 12 < age_int < 18:
    print("Vaše jízdné stojí " + str(age_18) + " Korun českých. Budete přesměrováni na platební portál. Děkujeme Vám, že jste využili našich služeb!")

elif dpo is False and age_int > 65:
    print("Vaše jízdné stojí " + str(age_65) + " Korun českých. Budete přesměrováni na platební portál. Děkujeme Vám, že jste využili našich služeb!")

elif dpo is True and age_int > 55:
    print("Děkujeme Vám, že pracujete pro společnost DP Ostrava. Jako bonus máte od nás jízdné zdarma! Děkujeme!")

else:
    print("Vaše jízdné stojí " + str(base_price) + " Korun českých. Budete přesměrováni na platební portál. Děkujeme Vám, že jste využili našich služeb!")
