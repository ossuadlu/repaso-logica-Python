
# ejemplo 1 hidroituango

NivelAgua=float(input("digita el nivel del agua: "))

if(NivelAgua >0 and < 200):
        print("la represa tiene poca agua")

elif(NivelAgua>=200 and nivelAgua<450):
         print("REPRESA ESTA OK")

elif(NivelAgua >=450):
        print("cuidado, abra compuertas")
else:
        print("digito un ivel invalido")



#ejemplo2 estaciones del año

mes=input("Digite el mes que desea consultar: ").lower()

if(mes== 'enero'or mes== 'febrero'or mes=='marzo'):
    print("Actualmente nos encontramos en invierno")

elif(mes=='abril'or mes== 'mayo' or mes=='junio'):
    print ("Actualmente nos encontramos en verano: v") 

elif(mes=='julio'or mes== 'agosto' or mes=='septiempre'):   
    print ("Actualmente nos encontramos en otoño: 3") 

elif(mes=='octubre'or mes== 'noviembre' or mes=='diciembre'):   
    print ("Actualmente nos encontramos en primavera: ") 
else:
    print("error, ingresa un mes valido..")

    #ejemplo3 edades

edad=float(input("digite edad: "))
if(edad >=0 and edad<=14):
    print("la etapa de la edad en que se encuentra es Niño")
elif(edad>14 and edad<=28):
    print("la edad en que se encuentra es joven")
elif(edad >28 and edad <60):
    print("la edad en que se encuhentra es adulto") 
elif(edad >=60) :
    print("su edad es adulto mayor")  
else:
    print ("error al digitar su edad")

