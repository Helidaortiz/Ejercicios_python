a=int(input("ingrese un numero "))
b=int(input(" Ingrese otro numero "))
c=int(input("Ingrese un numero "))
if(a<b and a<c):
    print("El numero mayor es " ,a)
else:
    if (b<a and b<c):
        print("el numero menor  es ",b)
    else:
        print("el numero menor es ",c)
        
    