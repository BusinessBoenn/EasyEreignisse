Om_type = input("Omega-Typ? create [cr], custom [cu] ")

if om_type == "cr":
    start = input("start: ")
    stop = input("stop: ")
    Omega = list(range(start, stop + 1))
elif om_type == "cu":
    Omega = input("Omega:").split()
else:
    print("wrong input")

Ereignisse = []

num_of_E = input("Anzahl Ereignisse: ")

for i in range(1, num_of_E + 1):
    Ereignisse.append([])

for k in range(0, Ereignisse.length()):
    Ereignisse[k] = input("E" + k+1 + ": ").split()
