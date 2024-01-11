# fenyőfa rajzolása pythonban

magassag = 5
for i in range(1, magassag + 1):
    for j in range(magassag - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(2):
    for j in range(magassag - 1):
        print(" ", end="")
    print("|", end="")
    print()
