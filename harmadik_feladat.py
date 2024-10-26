# 3.feladat:	Írd ki a -200 és 150 közötti minden ötödik számot egy sorba kukac jelel elválasztva. (ne egyesével gépeld be őket, az nem jó megoldás!) A megoldásodat for-al és while-al is valósítsd meg!

def harmadik_for():

    # for ciklussal megoldva:

    for i in range(-195, 150, 5):
        print(i, end="@ ")


def harmadik_while():

    # while ciklussal megoldva:

    i = -195

    while i > -200:
        print(i, end="@ ")
        i -= 5

    while i < 150:
        print(i, end="@ ")
        i += 5
