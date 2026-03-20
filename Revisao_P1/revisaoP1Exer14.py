x=int(input("Digite o valor de x: "))
y=int(input("Digite o valor de y: "))
z=int(input("Digite o valor de z: "))

if x>10 and x<5:
    x=x*2
elif y<z and z<x and x==y:
    y=y+z
elif y==z:
    if y!=z:
        z=z*3
    elif x==z and x!=y:
        x=y+z

print("Valor de x: ",x)
print("Valor de y: ",y)
print("Valor de z: ",z)