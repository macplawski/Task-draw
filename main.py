import random

def losujZadania():
    print("Ile zadan chcesz dzisiaj zrobic? Wpisz liczbe: ", end="")
    liczbaZadan = input()
    liczbaZadan = int(liczbaZadan)

    f = open("jeszczeDoZrobienia.txt", "r+")
    g = open("zrobione.txt", "r+")
    tmp = open("dzisiejszeDoZrobienia.txt", "w+")

    zadaniaZrobione = []
    zadaniaDoZrobienia = []

    for i in g:
        zadaniaZrobione.append(i)

    for i in f:
        zadaniaDoZrobienia.append(i)

    if liczbaZadan > len(zadaniaDoZrobienia):
        liczbaZadan = len(zadaniaDoZrobienia)

    print("Dzisiejsze zadania do zrobienia: ", end="")

    for i in range(0, liczbaZadan):
        a = random.randint(0, len(zadaniaDoZrobienia)-1)
        zadaniaZrobione.append(zadaniaDoZrobienia[a])
        tmp.writelines(zadaniaDoZrobienia[a])
        print(zadaniaDoZrobienia[a].strip(), end=', ')
        zadaniaDoZrobienia.pop(a)

    f.truncate(0)
    g.truncate(0)

    zadaniaZrobione.sort()

    g.seek(0, 0)
    for i in range(0, int(len(zadaniaZrobione))):
        g.writelines(zadaniaZrobione[i])

    f.seek(0, 0)
    for i in range(0, int(len(zadaniaDoZrobienia))):
        f.writelines(zadaniaDoZrobienia[i])

    tmp.close()
    g.close()
    f.close()

def dodajZadania():
    g = open("jeszczeDoZrobienia.txt", "w+")
    f = open("zrobione.txt", "w+")

    print("Zakres zadan: \nod: ", end=" ")
    x = input()
    x = int(x)
    print("do: ", end=" ")
    y = input()
    y = int(y)

    for i in range(x, y):
        g.write(str(i) + "\n")

    g.close()
    f.close()


while True:
    print("Co chcesz zrobic? Wpisz 1 by wylosowac zadania, wpisz 2 by stworzyc nowy zakres zadan: ", end="")
    wybor = input()
    if wybor == "1":
        losujZadania()
        print("\nChcesz kontynuowac? tak/nie ", end='')
        tmp = input()
        if tmp == 'tak':
            continue
        elif tmp == 'nie':
            print("Dziekuje za wspolprace. Do widzenia!")
            break
        else:
            print("Za brak rozwagi, do widzenia.")
            break

    elif wybor == "2":
        dodajZadania()
        print("\nChcesz kontynuowac? tak/nie ", end='')
        tmp = input()
        if tmp == 'tak':
            continue
        elif tmp == 'nie':
            print("Dziekuje za wspolprace. Do widzenia!")
            break
        else:
            print("Za brak rozwagi, do widzenia.")
            break
    else:
        print("Wybrales niepoprawna liczbe lub znak. Postaraj sie, to nie takie trudne ")