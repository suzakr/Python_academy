# 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.

# 2. Změň cenu jedné libovolné knihy. Vypiš list.

# 3. Odstraň nějakou knihu. Vypiš list.

# 4. Vypiš celkový počet knih v listu.

# Bonusový úkol (dobrovolné): Přidej 1 knihu pomocí uživatelského vstupu (https://www.w3schools.com/python/ref_func_input.asp)

books = [
    {
        "name": "Pán prstenů: Společenstvo prstenu",
        "price": 500,
        "author": "J.R.R. Tolkien",
        "publication_year": 1954
    }
]

# 1: Přidání dvou knih od listu
book2 = {"name": "Zaklínač: Poslední přání", "price": 499, "author": "Andrzej Sapkowski", "publication_year": 1993}
book3 = {"name": "The Old Republic: Revan", "price": 501, "author": "Drew Karpyshyn", "publication_year": 2011}

books.append(book2)
books.insert(0, book3)      # aby to bylo zajímavější
print(books)

# 2: Změna ceny jedné z knih
book2["price"] = 399
print(books)

# 3: Odstranění jedné z knih
del books[1]
print(books)

# 4: Celkový počet knih v listu
print(len(books))

# 5: Přidání knihy pomocí uživatelského vstupu
name_x = input("Napiš název knihy:")
price_x = input("\nJakou má kniha cenu? (uveď částku v Kč,-)")
author_x = input("\nKdo knihu napsal?")
publication_year_x = input("\nRok, ve kterém byla kniha vydána:")          # Mohl bych nastavit i "if" statement, kdyby se třeba někdo pokusil napsat text do ceny knihy, ale to jindy...

book4 = {"name": name_x, "price": price_x, "author": author_x, "publication_year": publication_year_x}
books.insert(0, book4)
print("\nVaše kniha byla zařazena do seznamu.\n")
print(books)
