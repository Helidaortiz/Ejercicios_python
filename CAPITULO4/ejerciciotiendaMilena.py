import random

input("Bienvenido a nuestra tienda, el dia de hoy tendremos descuentos por sorteos de compras superiores a $50.000")
valor_compra=(int(input("ingrese el valor de su compra: ")))

if valor_compra>=50000:
    print('Apreciado cliente aplica para la promoción!')

balota=['balota roja','balota verde','balota blanca','balota negra','balora amailla']
balota1=random.choice(balota)
print(balota)
if balota1=='balota roja':
    print(f"ha sacado la balota roja el valor de su descuento es de 100%",float(valor_compra-(valor_compra*100)/100))
elif balota1=="balota verde":
    print(f"ha sacado la balota verde el valor de su descuento es de 50%",float(valor_compra-(valor_compra*50)/100))
elif balota1=="balota blanca":
    print(f"ha sacado la balota blanca el valor de su descuento es de 30%",float(valor_compra-(valor_compra*30)/100))
elif balota1=="balota negra":
    print(f"ha sacado la balota negra el valor de su descuento es de 20%",float(valor_compra-(valor_compra*20)/100))
elif balota1=="balota amarilla":
    print(f"ha sacado la balota amarilla el valor de su descuento es de 10%",float(valor_compra-(valor_compra*10)/100))
else:
    print("No tiene descuento")