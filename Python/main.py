nome = "Samuel"
a = 9
b = 9
c = a+b
d = int(input("Ano em que nasceu:"))
print(f" Me chamo {nome} e tenho {c} anos. Nasci no ano de {d}")
if d <= 2005:
    print("Voce nao e obrigado a votar")
else:
    print("Voce e obrigado a votar")