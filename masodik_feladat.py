# 2.feladat:	Egy pizzázó téged kért fel belső rendszerének modernizálására. Vendégcsábító akciókba kezdtek. A te dolgod az akciók kezelésének kidolgozása. A felhasználó vásárol a felületen ezt egy vegOsszeg változóban tárolják, a felhasználó kedvezmény kategóriáját pedig egy kategoria nevű változóba. A különböző kedvezmények így néznek ki: Ha a felhasználó „arany kártyás” kategóriájú, akkor írd ki neki, hogy 10% kedvezményt kap! Ha a felhasználó „ezüst kártyás” kategóriájú, akkor írd ki neki, hogy 5% kedvezményt kap! Ha a felhasználó „bronz kártyás” kategóriájú, akkor írd ki neki, hogy 2% kedvezményt kap! Ha a felhasználó „VIP” kategóriájú, akkor írd ki neki, hogy 20% kedvezményt kap! Minden más kategória esetben pedig 1% kedvezményt kap, írd ki neki Haloween akció 1% kedvezményt kap. Ha a végösszeg 10.000. Ft felett van akkor további 5% kedvezményt kap, a kiírást ennek megfélően módosítsd. Felhasználói üzenet: „Nagy összegű vásárlás!”


def vegOsszeg():
    return vegOsszeg()

def masodik():
    kategoria = input("Kérem, adja meg a kártyájának a kategóriáját: ")

    if vegOsszeg() =< 10000 and kategoria == "arany":
        print("Rendelésed összesen: " + (str(vegOsszeg)))
        print("Akció: 10% kedvezményt kap ma!")

        if kategoria == "ezüst":
            print("Rendelésed összesen: " + (str(vegOsszeg)))
            print("Akció: 5% kedvezményt kap ma!")

        elif vegOsszeg() =< 8000 and kategoria == "bronz":
                print("Rendelésed összesen: " + (str(vegOsszeg)))
                print("Akció: 2% kedvezményt kap ma!")

        elif kategoria == "VIP":
                print("Rendelésed összesen: " + (str(vegOsszeg)))
                print("Akció: 20% kedvezményt kap ma!")
        else:
             print("Rendelésed összesen: " + (str(vegOsszeg)))
             print("Halloween akció 1% kedvezményt kap.")
    else:
        vegOsszeg() > 10000:
            print("Nagy összegű vásárlás!”)

