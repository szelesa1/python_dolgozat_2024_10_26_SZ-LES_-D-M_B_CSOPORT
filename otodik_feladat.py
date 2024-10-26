# 5. feladat: Írd ki a 60 és -70 közötti számokat vesszővel elválasztva egy sorba, úgy hogy az utolsó után ne legyen vessző. A tanult két fajta módon is valósítsd meg a programod.

def otodik_for():

    # for ciklussal megoldva:

    for i in range(59, -69, -1):
        print(i, end=", ")

    print(-69)


def otodik_while():

    # while ciklussal megoldva:

    i = 59

    while i < 60:
        print(i, end=", ")
        i += 1

    while i > -69:
        print(i, end=", ")
        i -= 1

    print(-69)
