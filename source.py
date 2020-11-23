import sys
import sqlite3
from sqlite3 import Error
import datetime
import pandas as pd

lista_total_venta = []  

 
loop = 1

while loop == 1:
    
    menu = int(input("Que accion deseas realizar\n 1.Registrar una venta\n 2. Consultar una venta\n 3. Salir\n"))
    if menu == 1:
        try:
            with sqlite3.connect("Registro_de_Ventas.db") as conn:
                c = conn.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS ventas (codigo INTEGER PRIMARY KEY, nombre TEXT NOT NULL, cantidad INTEGER, precio INTEGER, fecha DATE);")
                print("Conexión establecida correctamente\n")
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
            
        continuar = 1
        del lista_total_venta[:]
        while continuar == 1:
            clave_prd = int(input("Ingresa la clave del producto o Ingresa el numero 0(cero) para regresar al menu: ")) 
            if clave_prd == 0:
                continuar = 2
            else:
                print("----------REGISTRANDO VENTA----------")
                contador_cantidad = 0
                contador_unitario = 0
                contador_nombre = 0
                while contador_nombre == 0:
                    nombre_prd = input("¿Cual es el nombre del producto?: ")
                    if (nombre_prd.isspace() or len(nombre_prd) ==0):
                        print("\n-----AVISO-----")
                        print("Por favor vuelve a ingresa el nombre del producto no se acepta el nombre vacio\n")
                    else:
                        
                        contador_nombre = contador_nombre + 1
                while contador_cantidad == 0:
                    cantidad_prd = int(input("¿Cuantos productos vas a registrar?: "))
                    if cantidad_prd < 0:
                        print("\n-----AVISO-----")
                        print("SOLO SE ACEPTAN NUMEROS ENTEROS Y POSITIVOS ")
                        print("Por favor vuelve a ingresar la cantidad de productos\n")
                    else:
                        contador_cantidad = contador_cantidad + 1
                while contador_unitario ==0:
                    precio_prd = float(input("¿Cual es el valor unitario del producto?: "))
                    if precio_prd < 0:
                        print("\n-----AVISO-----")
                        print("SOLO SE ACEPTAN NUMEROS POSITIVOS ")
                        print("Por favor vuelve a ingresar el costo unitario del producto\n")
                    else:
                        contador_unitario = contador_unitario + 1
                fecha_venta = datetime.date.today()
                total_venta = (cantidad_prd * precio_prd)
                    
                try:
                    with sqlite3.connect("Registro_de_ventas.db") as conn:
                        c = conn.cursor()
                        valores = {"clave":clave_prd, "nombre":nombre_prd, "cantidad":cantidad_prd, "precio":precio_prd, "fecha":fecha_venta}
                        c.execute("INSERT INTO ventas VALUES(:clave, :nombre, :cantidad, :precio, :fecha)", valores)
                        print("*** Registro agregado exitosamente ***\n")
                        lista_total_venta.append(cantidad_prd * precio_prd) 
                        
                except Error as e:
                    print(e)
                except:
                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        total_venta = sum(lista_total_venta)
        print(f"\nSe debe cobrar al cliente: ${total_venta}")
        print(f"Fecha del registro: {fecha_venta}\n")
        print("Se concluyó la carga de registros")


    
    
    elif menu == 2:
        try:
            with sqlite3.connect("Registro_de_Ventas.db") as conn:
                c = conn.cursor()
                consulta = input("¿Cuál es la fecha de venta que quieres consultar? Escribe la fecha con el siguiente formato: yyyy-mm-dd:\n ")
                valor ={"fecha":consulta}                
                c.execute("SELECT * FROM ventas WHERE fecha =(:fecha)",valor)
                registros = c.fetchall()
                print("*** Registros consultados exitosamente ***")
                
                if registros:
                    print("Clave\tNombre\tCantidad\tPrecio\tFecha")
                    for clave, nombre, cantidad, precio, fecha in registros:
                        print(f"{clave} \t", end="")
                        print(f"{nombre} \t", end="")
                        print(f"{cantidad} \t", end="")
                        print(f"{precio} \t", end="")
                        print(fecha)
                        
                else:
                    print(f"No se encontraron ventas en: {consulta}, intentelo de nuevo con otra fecha")
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    
    
    elif menu == 3:
        
        print("Vuelve pronto :)")
        loop = 2
    
    
    else:
        
        print("Opcion no valida ingrese una opcion presentada en el menu")