import sys
import sqlite3
from sqlite3 import Error
import datetime

loop = 1

while loop == 1:
    
    menu = int(input("Que accion deseas realizar\n 1.Registrar una venta\n 2. Consultar una venta\n 3. Salir\n"))
    if menu == 1:
        try:
            with sqlite3.connect("Registro de Ventas.db") as conn:
                c = conn.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS ventas (codigo INTEGER PRIMARY KEY, nombre TEXT NOT NULL, cantidad INTEGER, precio INTEGER, fecha DATE);")
                print("Conexión establecida correctamente")
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
            
        continuar = 1
        while continuar == 1:
            print("=" * 40)
            print("----------INSTRUCCIONES----------")
            print("Proporcione los datos de la venta, introduzca la clave 0(cero) para terminar: ")
            print("\nINGRESA UN NUMERO ENTERO PARA LA CLAVE\n")
            clave_prd= int(input("¿Cual es la clave que le quieres dar al producto?: "))
            if clave_prd == 0:
                continuar = 2
            else:
                nombre_prd = input("¿Cual es el nombre del producto?: ")
                contador_cantidad = 0 
                
                while contador_cantidad == 0: 
                    cantidad_prd = int(input("¿Cuantos productos vas a registrar?: "))
                    if cantidad_prd < 0: 
                        print("\n-----AVISO-----") 
                        print("SOLO SE ACEPTAN NUMEROS ENTEROS Y POSITIVOS ") 
                        print("Por favor vuelve a ingresar la cantidad de productos\n")
                    else: 
                        contador_cantidad = contador_cantidad + 1 
                precio_prd = int(input("¿Cual es el valor unitario del producto?: "))
                fecha_venta = datetime.date.today()
                    
                try:
                    with sqlite3.connect("Registro de ventas.db") as conn:
                        c = conn.cursor()
                        valores = {"clave":clave_prd, "nombre":nombre_prd, "cantidad":cantidad_prd, "precio":precio_prd, "fecha":fecha_venta}
                        c.execute("INSERT INTO ventas VALUES(:clave, :nombre, :cantidad, :precio, :fecha)", valores)
                        print("*** Registro agregado exitosamente ***")
                except Error as e:
                    print(e)
                except:
                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("Se concluyó la carga de registros de fabricante")


    
    
    elif menu == 2:
        try:
            with sqlite3.connect("Registro de Ventas.db") as conn:
                c = conn.cursor()
                consulta = input("¿Cuál es la fecha de venta que quieres consultar? Escribe la fecha con el siguiente formato: yyyy-mm-dd:\n ")
                valor ={"fecha":consulta}                
                c.execute("SELECT * FROM ventas WHERE fecha =(:fecha)",valor)
                registros = c.fetchall()
                print("Clave\tNombre del producto\tCantidad\tPrecio\tFecha")
                print("◄" * 50)
                for clave, nombre, cantidad, precio, fecha in registros:
                    print(f"{clave}\t")
                    print(f"{nombre}\t")
                    print(f"{cantidad}\t")
                    print(f"{precio}\t")
                    print(f"{fecha}\t")
    
    
    elif menu == 3:
        
        print("Vuelve pronto :)")
        loop = 2
    
    
    else:
        
        print("Opcion no valida ingrese una opcion presentada en el menu")