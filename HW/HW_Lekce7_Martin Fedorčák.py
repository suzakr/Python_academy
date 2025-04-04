"""
Napiš program, který bude pracovat s informacemi o uživatelském účtu: username, age, email


Vytvoř následující funkce:

is_adult: Funkce ověří zda je uživatel dospělý
is_name_valid: Funkce ověří zda uživatelské jméno je alespoň 4 znaky dlouhé
create_user:
  Funkce vytvoří slovník reprezentujícího uživatele.
 Uvnitř funkce zkontroluj, zda je uživatel dospělý a jeho jméno je validní.
Pokud je vše v pořádku, create_user vrátí následující slovník:
{
"success": True,
"user": {"username": "...", "age": ..., "email": "..."}
}
 Pokud validace selže, create_user vrátí:
{
"success": False,
"error": "Chybová zpráva..."
}


print_user_info: Funkce vytiskne uživatele do konzole s libovolným formátováním, případně vytiskne chybovou zprávu při neúspěšném vytvoření

Pomocí metody create_user vytvoř alespoň 4 různé uživatele. Hodnoty si zvol podle sebe přímo v programu.

Nakonec vytvořené uživatele vytiskni pomocí cyklu a metody print_user_info.
"""



# def create_user():
#     user = {"success": True}
#     username = input("Type username for your account:")
#     if username == "End":
#         print(user_list)
#         exit()
#     def is_name_valid():
#         if len(username) < 4:
#             name_false = {"success": False, "error": "Username is too short (4 characters minimum)."}
#             print(name_false)
#             user_list.append(name_false)
#             loop()
#
#     is_name_valid()
#     user["username"] = username
#
#     age = int(input("Type your age:"))
#     def is_adult():
#         if age < 18:
#             age_false = {"success": False, "error": "Only adults can create an account."}
#             print(age_false)
#             user_list.append(age_false)
#             loop()
#
#     is_adult()
#     user["age"] = age
#
#     email = input("Type your valid email adress:")
#     user["email"] = email
#     user_list.append(user)
#     # print(user)
#
# def loop():
#     create_user()
#
# user_list = []
#
# while True:
#     create_user()
#
# print(user_list)

# ______________________________________________________________________ #


def create_user():
    def is_adult():
        is_running = True
        while is_running:
            age = int(input("Type your age:"))
            if age >= 18:
                user["age"] = age
                break
            age_false["success"] = False
            age_false["error"] = "Only adults can create an account."
            is_running = False
            print(age_false)
            user_info.append(age_false)


    def is_name_valid():
        while True:
            username = input("Type username for your account:")
            if len(username) >= 4:
                user["success"] = True
                user["username"] = username
                break
            name_false["success"] = False
            name_false["error"] = "Username is too short (4 characters minimum)."
            print(name_false)
            user_info.append(name_false)


# Funkce ma chybu, ze po zadani jednoho chybneho udaje do "age", mi funkce preskoci na zadani emailu. Misto toho bz mela skocit zpet na zacatek na zadani username, ale nevim, jak to udelat

# Funkce print_user_info() neni dodelana, protoze jsem nevedel, jak muzu zacyklit funkci create_user() do toho vseho ostatniho

# __________________________________________________________________ #

# def create_user():
#     def is_name_valid():
#         username = input("Type username for your account:")
#         if len(username) < 4:
#             name_false["success"] = False
#             name_false["error"] = "Username is too short (4 characters minimum)."




    user_list = []      # melo slouzit k ulozeni vsech uzivatelu, odkud bych je pak pridal do funkce print_user_info()
    user = {}
    name_false = {}
    age_false = {}
    user_info = []

    is_name_valid()
    is_adult()
    email = input("Type your valid email address:")
    user["email"] = email
    user_list.append(user)
    print(user_list)

create_user()


