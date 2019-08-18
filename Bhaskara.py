#Fórmula de Bhaskara - Equação do 2ºGrau (ax^2 + bx + c = 0)

#Informando os valores da equação
print("Bem-Vindo(a)!")
print()
a=float(input("Informe o valor de a: "))
b=int(input("Informe o valor de b: "))
c=float(input("Informe o valor de c: "))
print()

#Calculando Delta
delta = (b^2) - (4*a*c)
print("O delta é: ", delta)
print()
if delta < 0:
    print("Raíz não pode ser negativo")
else:
#Resolvendo Bhaskara
    bhaskara = (-b)
    delta = delta ** (1/2)
    X1 = (bhaskara + delta) / (2*a)
    X2 = (bhaskara - delta) / (2*a)
    
    print("O X1 é: %.0f"%X1)
    print("O X2 é: %.0f"%X2)
    print()
    print("S = {%.0f"%X1,"; %.0f"%X2,"}")
