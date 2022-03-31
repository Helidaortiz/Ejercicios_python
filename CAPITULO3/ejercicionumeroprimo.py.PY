num=int(input("ingrese el numero: "))
if num>1:
    cont=0
    for i in range(2,num):
        resto= num%i
        if resto == 0:
            cont+=1        
    if cont==0:                
        print(f" {num} es primo")
    else:
        print(f" no es primo {num}",)