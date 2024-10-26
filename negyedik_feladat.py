# 4.feladat: Kérj be a felhasználótól egy valósszámot. A programod számítsa ki a bekért érték alsó egész részét (kerekítse lefele), ehhez a math csomag floor() eljárását használd.

import math


def negyedik():

    bekert_szam = float(input("Kérlek, adj meg egy valós számot: "))
    print(math.floor(bekert_szam))
