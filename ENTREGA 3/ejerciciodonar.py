edad=int(input('¿Que edad tiene?'))
peso=int(input('¿Cuanto pesa?'))
heartbeat=int(input('¿cuanto son los latidos del corazon?'))
plaquetas=int(input('¿Cuantas plaquetas tiene?'))
if edad>=34 and peso>=81 and heartbeat>=70 and plaquetas>=150000:
    print(f"La edad es :{edad},Su peso es :{peso},Latidos del corazon son :{heartbeat},Tiene de plaquetas :{plaquetas}//Es apto para donar sangre") 
else:
    if edad<34 and peso<81 and heartbeat<70 and plaquetas<150000:
        print("No es apto para donar sangre")
#print(f"La edad es :{edad},Su peso es :{peso},Latidos del corazon son :{heartbeat},Tiene de plaquetas :{plaquetas}")

