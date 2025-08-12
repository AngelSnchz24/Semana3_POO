# Vamos a crear nuestro menu con cada una de las opciones.
# Cada opcion llamara a una funcion que resuelve el ejercicio correspondiente.
def menu():
    continuar = True
# Bucle principal del menu.
    while continuar:
        print("=== Bienvenido a los ejercicios de la semana 3 ===")
        print("Elija un ejercicio a resolver:")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Salir")

        option = int(input())

        if option == 1:
            ejercicio1()
        elif option == 2:
            ejercicio2()
        elif option == 3:
            ejercicio3()
        elif option == 4:
            ejercicio4()
        elif option == 5:
            print("Saliendo del programa... Hasta luego :D")
            continuar = False
        else:
            print("La opcion ingresada no es válida. Por favor, intente de nuevo.")

# Ahora vamos a definir nuestro primer ejercicio como una funcion, cada uno ira dentro de su propia funcion.
def ejercicio1():
    print("=== Ejercicio 1 ===")
    print("Escriba un programa que solicite al usuario un numero y que determine si es postivo, negativo o cero.")
    # Solicitar al usuario un numero.
    numero = int(input("Ingrese un numero: "))
    # Determinar si el numero es positivo, negativo o cero.
    if numero > 0:
        print("El numero es positivo.")
    elif numero < 0:
        print("El numero es negativo.")
    # Si no es positivo ni negativo, entonces es cero.
    else:
        print("El numero es cero.")
    # Llegamos al final del ejercicio 1.
    print("=== Fin del ejercicio 1 ===")

# Ahora vamos a definir nuestro segundo ejercicio como una funcion.
def ejercicio2():
    print("=== Ejercicio 2 ===")
    print("Escriba un programa que solicite un numero positivo al usuario y cree un contador desde el 1 hasta el numero ingresado.")
    # Solicitar al usuario un numero positivo.
    numero = int(input("Ingrese un numero positivo: "))
    # Crear un contador desde el 1 hasta el numero ingresado.
    if numero > 0:
        for i in range(1, numero + 1):
            print(i)
    # Si el numero no es positivo, informar al usuario.
    else:
        print("El numero ingresado no es positivo.")
    # llegamos al final del ejercicio 2.
    print("=== Fin del ejercicio 2 ===")
# Ahora vamos a definir nuestro tercer ejercicio como una funcion.
def ejercicio3():
    print ("=== Ejercicio 3 ===")
    print("Escriba un programa que solicite al usuario un numero y que imprima la tabla de multiplicar de ese numero.")
    # Solicitar al usuario un numero.
    numero = int(input("Ingrese un numero: "))
    # Imprimir la tabla de multiplicar del numero ingresado.
    print(f"Tabla de multiplicar del numero {numero}: ")
    # Usamos un bucle for para imprimir la tabla de multiplicar.
    for i in range (1, 11):
    # Imprimir el resultado de la multiplicacion.
        print(f"{numero} x {i} = {numero * i}")
    # Llegamos al final del ejercicio 3.
    print("=== Fin del ejercicio 3 ===")

# Ahora vamos a definir nuestro cuarto ejercicio como una funcion.
def ejercicio4():
    print("=== Ejercicio 4 ===")
    print("Crea un programa que sume numero introducidos por el usuario uno por uno hasta que el usuario introduzca un numero negativo.")
    # Inicializar la suma en 0.
    suma = 0
    # Bucle para solicitar numeros al usuario hasta que ingrese un numero negativo.
    while True:
        numero = int(input("Ingrese un numero (negativo para terminar): "))
    # Si el numero es negativo, salir del bucle.
        if numero < 0:
        # Con la instruccion break salimos del bucle.
            break
        suma += numero
    # Imprimir la suma de los numeros ingresados.
    print(f"La suma de los numeros ingresados es: {suma}")
    # Llegamos al final del ejercicio 4.
    print("=== Fin del ejercicio 4 ===")

menu()  # Llamamos a la funcion menu para iniciar el programa.