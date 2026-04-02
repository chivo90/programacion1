#1
nombre = input("Cliente: ").strip()

while nombre=="" or not nombre.isalpha():
    print("Error: Ingresa un nombre no vacio o solo con letras")
    nombre = input("Cliente: ").strip()

cantidad_str = (input("Ingresa la cantidad de productos: ")).strip()

while not cantidad_str.isdigit() or int(cantidad_str==0):
    print("Error: Ingresa una cantidad numerica y mayor a 0")
    cantidad_str = (input("Ingresa la cantidad de productos: ")).strip()

cantidad_int = int(cantidad_str)
total_sin_descuento = 0
total_con_descuento = 0.0
for i in range(1,cantidad_int+1):
    precio_str = input(f"Producto {i}= Precio: ").strip()

    while not precio_str.isdigit() or precio_str ==0:
        print("Error: El precio debe ser un entero positivo")
        precio_str = input(f"Producto {i}= Precio: ").strip()
        
    precio_int = int(precio_str)

    desc = input("Descuentro (S/N): ").strip().lower()

    while desc !="s" and desc!="n":
        print("Error: Ingresa S para si o N para no")
        desc = input("Descuentro (S/N): ").strip().lower()

    total_sin_descuento += precio_int

    if desc == "s":
        precio_final = precio_int *0.9
    else:
        precio_final = precio_int
        
    total_con_descuento += precio_final

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_int

print()
print(f"El total sin descuentos es ${total_sin_descuento}")
print(f"El total con descuentos es ${total_con_descuento:.2f}")
print(f"El ahorro total es ${ahorro:.2f}")
print(f"El promedio es {promedio:.2f}")

#2
usuario_correcto = "alumno"
clave_correcta= "python123"

max_intentos = 3
intentos= 0
while intentos<max_intentos:
    print(f"Intento {intentos+1}/3")
    usuario = input("Usuario: ").strip()
    clave = input("Clave: ").strip()

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido")
        break
    else:
        print("Error: Credenciales invalidas")
    intentos+=1

if intentos==max_intentos:
    print("Cuenta bloqueada")

else:
    while True:
        print("1) Ver estado")
        print("2) Cambiar clave")
        print("3) Mensaje motivacional")
        print("4) Salir")
        
        opcion = input("Opcion: ").strip()

        while not opcion.isdigit():
            print("Ingrese un numero valido")
            input("Numero entre 1 y 4")
            
        opcion = int(opcion)
        
        if opcion <1 or opcion >4:
            print("Opcion fuera de rango")
            continue

        if opcion ==1:
            print("Inscripto")

        elif opcion==2:
            nueva_clave= input ("Nueva clave: ").strip()
            confirmacion=input("Confirmar clave:  ").strip()

            if nueva_clave != confirmacion:
                print("Error, las claves no coinciden")
            elif len(nueva_clave)<6:
                print("Error: La clave debe tener 6 caracteres minimo")

            else:
                clave_correcta=nueva_clave
                print("Clave actualizada correctamente")

        elif opcion==3:
            print("Vamos que vos podes!")

        elif opcion==4:
            print("Saliendo del sistema")
            break

#3        
lunes1 = lunes2 = lunes3 = lunes4 =""
martes1 = martes2 = martes3 = ""

operador = input ("Ingrese el nombre del operador: ").strip()

while not operador.isalpha():
    print ("Error: El operador debe ser solo letras")
    operador = input ("error: Solo letras ").strip()

while True:
    print()
    print("1: Reservar turno")
    print("2: Cancelar turno")
    print("3: Ver agenda")
    print("4: Resumen")
    print("5: Cerrar sistema")
    
    opcion = (input("Opcion: ")).strip()
    while not opcion.isdigit():
        print("Error: Ingrese un numero: ")
        continue

    opcion = int (opcion)
    if opcion<1 or opcion>5:
        print ("Opcion fuera de rango")
        continue

    if opcion==1:
        print("Reservar turno:")
        dia = input("Elija 1 para Lunes o 2 para Martes: ").strip()
        while not dia.isdigit or dia!="1" and dia!="2":
            print ("Opcion incorrecta")
            dia = input("Error: Elija 1 o 2: ").strip()
        nombre = input("Escriba el nombre el paciente: ").strip()
        while not nombre.isalpha():
            print("Escriba el nombre del paciente solo con letras ")
            nombre = input("Error: Solo letras ").strip()
        
        if dia=="1":
            if nombre==lunes1 or nombre==lunes2 or nombre==lunes3 or nombre==lunes4:
                print("Ese paciente ya tiene turno el dia Lunes")

            elif lunes1=="":
                lunes1=nombre
                print("Turno agendado")

            elif lunes2=="":
                lunes2=nombre
                print("Turno agendado")

            elif lunes3=="":
                lunes3=nombre
                print("Turno agendado")

            elif lunes4=="":
                 lunes4=nombre
                 print("Turno agendado")

            else:
                print("No hay turnos disponibles para el dia Lunes")

        if dia=="2":
            if nombre==martes1 or nombre==martes2 or nombre== martes3:
                print("Ese paciente ya tiene turno el dia Martes")

            elif martes1=="":
                martes1 = nombre
                print("Turno agendado")

            elif martes2=="":
                martes2 = nombre
                print("Turno agendado")

            elif martes3=="":
                martes3 = nombre
                print("Turno agendado")

            else:
                print("No hay turnos disponibles para el dia Martes")

    elif opcion==2:
        print("Cancelar turno:")
        dia = input("Elija 1 para Lunes o 2 para Martes: ").strip()
        while not dia.isdigit() or dia!="1" and dia!="2":
            print ("Opcion incorrecta")
            dia = input("Error: Elija 1 o 2: ").strip()
        nombre = input("Escriba el nombre el paciente: ").strip()
        while not nombre.isalpha():
            print("Escriba el nombre del paciente solo con letras ")
            nombre = input("Error: Solo letras ").strip()
        
        encontrado = False

        if dia=="1":
            if nombre==lunes1:
                lunes1 =""
                encontrado = True
            elif nombre==lunes2:
                lunes2 =""
                encontrado =True
            elif nombre==lunes3:
                lunes3 =""
                encontrado =True
            elif nombre==lunes4:
                lunes4 =""
                encontrado =True
        
        elif dia=="2":
            if nombre==martes1:
                martes1=""
                encontrado = True
            elif nombre==martes2:
                martes2 =""
                encontrado =True
            elif nombre==martes3:
                martes3 =""
                encontrado =True

        if encontrado:
            print("Turno cancelado")

        else:
            print("Paciente no encontrado")

    elif opcion==3:
        print("Ver agenda:")
        dia = input("Elija 1 para Lunes o 2 para Martes: ").strip()
        while not dia.isdigit or dia!="1" and dia!="2":
            print ("Opcion incorrecta")
            dia = input("Error: Elija 1 o 2: ").strip()

        if dia =="1":
            if lunes1!="":
                print("Turno 1", lunes1)
            else:
                print("(Libre)")

            if lunes2!="":
                print("Turno 2", lunes2)
            else:
                print("(Libre)")

            if lunes3!="":
                print("Turno 3", lunes3)
            else:
                print("(Libre)")
            
            if lunes4!="":
                print("Turno 4", lunes4)
            else:
                print("(Libre)")


        if dia =="2":
            if martes1!="":
                print("Turno 1", martes1)
            else:
                print("(Libre)")

            if martes2!="":
                print("Turno 2", martes2)
            else:
                print("(Libre)")

            if martes3!="":
                print("Turno 3", martes3)
            else:
                print("(Libre)")

    elif opcion==4:
        
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1!="": ocupados_lunes+=1
        if lunes2!="": ocupados_lunes+=1
        if lunes3!="": ocupados_lunes+=1
        if lunes4!="": ocupados_lunes+=1

        if martes1!="": ocupados_martes+=1
        if martes2!="": ocupados_martes+=1
        if martes3!="": ocupados_martes+=1

        print("Ver resumen: ")
        print("Lunes:", ocupados_lunes, "ocupados", 4- ocupados_lunes, "libres")
        print("Martes:", ocupados_martes, "ocupados", 3 - ocupados_martes,"libres")

        if ocupados_lunes>ocupados_martes:
            print("Mas turnos dia lunes")

        elif ocupados_martes>ocupados_lunes:
            print("Mas turnos dia martes")

        else :
            print("Empate")

    elif opcion==5:
        break

#4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

nombre = input("Ingrese el nombre del agente: ").strip()

while not nombre.isalpha():
    nombre = input("Error. Solo letras: ").strip()

print("Bienvenido agente", nombre)

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 :
    
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado por alarma")
        break

    print("---Estado---")
    print("Energia", energia)
    print("Tiempo", tiempo)
    print("Cerraduras abiertas", cerraduras_abiertas)
    print("Alarma", "ON" if alarma else "OFF")

    print("---Menu---")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    
    opcion = (input("Opcion: ")).strip()
    while not opcion.isdigit() or opcion !="1" and opcion!="2" and opcion!="3":
        opcion = input("Ingrese 1, 2 o 3: ").strip()

    if opcion == "1":

        racha_forzar += 1
        energia -= 20
        tiempo -=2

        if racha_forzar == 3:
            print("La cerradura no abre! Alarma activada")
            alarma = True

        else:
            if energia < 40:
                numero = input ("Riesgo. Elige un numero (!-3)").strip()

                while not numero.isdigit() or numero!="1" and numero!="2" and numero!="3":
                    numero = input("Error. Elija 1, 2 o 3: ").strip()

                if numero ==3:
                    print("Fallaste. Alarma activada")
                    alarma = True

            if alarma == False:
                cerraduras_abiertas +=1
                print("Abriste una cerradura!")

    elif opcion == "2":

        racha_forzar = 0
        energia -= 10
        tiempo -=3

        for i in range(4):
            print("Hackeando paso", i+1)
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas +=1
            print("Hackeo exitoso! Se abrio una cerradura")

    elif opcion =="3":

        racha_forzar =0
        energia += 15
        
        if energia > 100:
            energia = 100

        tiempo -=1

        if alarma == True:
            energia -=10
        
        print("Descansaste")

if cerraduras_abiertas ==  3:
    print("VICTORIA! Abriste la boveda")

elif energia  <= 0 or tiempo <= 0:
    print("DERROTA! Te quedaste sin recursos")

else:
    print("DERROTA! Sistema bloqueado")  


#5
print("---BIENVENIDO A LA ARENA---")

nombre = input("Nombre del gladiador: ").strip()
while not nombre.isalpha():
    print("Solo se permiten letras: ")    
    nombre = input("Nombre del gladiador: ").strip()

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
daño_base = 15
daño_enemigo = 12
turno_gladiador = True

print("---INICIO DEL COMBATE---")

while vida_gladiador > 0 and vida_enemigo > 0:
    print("---NUEVO TURNO---")
    print(nombre, "(HP:", vida_gladiador, ") vs Enemigo (HP:", vida_enemigo, ") Pociones:", pociones)
    print("Elija accion:")
    print("1. Ataque pesado")
    print("2. Rafaga veloz")
    print("3. Curar")
    
    opcion = input("Opcion: ").strip()
    
    while not opcion.isdigit() or opcion!="1" and opcion!="2" and opcion!="3":
        print("Ingrese un numero valido")
        opcion = input("Opcion: ").strip()
    
    if opcion =="1":
        if vida_enemigo < 20:
            daño_final = daño_base*1.5
            print("Golpe critico")
        else:        
            daño_final = daño_base
        
        vida_enemigo -= daño_final
        print("Atacaste al enemigo por", daño_final, "puntos de daño")
    elif opcion =="2":
        print("Inicias una rafaga de golpes")
        for i  in range (3):
            print("Golpe conectado por 5 de dañe")
            vida_enemigo-=5

    elif opcion =="3":
        if pociones > 0:
            vida_gladiador += 30
            pociones -=1
            print("Te curaste 30 puntos")

        else:
            print("No te quedan pociones")

    if vida_enemigo > 0:
        vida_gladiador -= daño_enemigo
        print("El enemigo te ataco por 12 puntos de daño")

print("---FIN DEL COMBATE---")

if vida_gladiador > 0:
    print("VICTORIA!", nombre, "Has ganado la batalla")
else:
    print("DERROTA. Has caido en combate")




