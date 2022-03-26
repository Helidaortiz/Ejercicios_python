##**
##break
num=20
while num>=1:
    if num/3==0:
        print(num)
        break 
num==1

##continue
num=21
while num>=1:
    num==1
    if num/3==0:
        continue
    print(num,end=',')

##for
i=inicio
rengo:final

word='Python'
for letter in word:
    print(letter)


##
num=10
for i in range (num):
    print(i,end=",")
    
##
for i in range(0,10,2):
    print(i)
    
##interpolacion de caracteres  //ciclos anidados
for i in range(1,10):
    for j in range(1,10):
        result=i*j
        print(f'{i}*{j}={result}')
        
## MULTIPLICACION
valor="1"
for i in range(1,10):
    repetir_valor=int(valor*i)
    multiplicacion=repetir_valor*repetir_valor
    print(f'{repetir_valor}.{repetir_valor}={multiplicacion}')    



##
# num=1.1
# while num! <10:
# num +=1
##
