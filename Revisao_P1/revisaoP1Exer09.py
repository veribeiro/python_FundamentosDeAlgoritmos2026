x=int(input("Digite o valor de x: "))

if(x<30):
    print("olá")
elif(x<=30 or x<50.7):
    xdobro=x*2
    print("O valor de x será: ",xdobro)

elif(x>=50.7):
    xtriplo=x*3
    print("O valor de x será: ",xtriplo)

else:
    print("Algo deu errado")