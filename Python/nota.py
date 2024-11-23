a = float(input("Digite a primeira nota:"))
b = float(input("Digite a segunda nota:"))
c = float(input("Digite a terceira nota:"))
d = (a+b+c)/3

if d>=6:
    print(f"Sua media e {d:.2f} e voce esta Aprovado")
else:
    print(f"Sua media e {d:.2f} e voce esta Reprovado")