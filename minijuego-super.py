#Importar librerias necesarias
import time

#Variables globales
#contadores para cada categoría de productos
contador_frutas = 0
contador_verduras = 0
contador_lacteos = 0
contador_carnes = 0

#contadores para cada producto dentro de cada categoría
#contadores para frutas
contador_manzanas = 0
contador_peras = 0
contador_bananas = 0
contador_naranjas = 0

#contadores para verduras
contador_lechuga = 0
contador_tomates = 0
contador_zanahorias = 0
contador_pepinos = 0

#contadores para lácteos
contador_leche = 0
contador_yogurt = 0
contador_queso = 0
contador_mantequilla = 0

#contadores para carnes
contador_pollo = 0
contador_res = 0
contador_pescado = 0
contador_cerdo = 0

#contadores para compras exitosas y fallidas
contador_compras_exitosas = 0
contador_compras_fallidas = 0

#Funcion para hacer el tiempo de carga
def TiempoEspera():
    time.sleep(0.5)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1.5)
    print(".")
    time.sleep(2)

# Funciones y main, por medio de minijuego en consola de supermercado
def main():
    while True:
        print("===BIENVENIDO AL MINIJUEGO DEL SUPERMERCADO===")
        print("¿Qué deseas comprar hoy?")
        print("1. Frutas")
        print("2. Verduras")
        print("3. Lácteos")
        print("4. Carnes")
        print("5. Salir del supermercado")

        try:
            opcion = int(input("Ingrese el número de la opción deseada: "))
            
            match opcion:
                case 1:
                    Seleccion_Frutas()
                    TiempoEspera()
                case 2:
                    Seleccion_Verduras()
                    TiempoEspera()
                case 3:
                    Seleccion_Lacteos()
                    TiempoEspera()
                case 4:
                    Seleccion_Carnes()
                    TiempoEspera()
                case 5:
                    ReporteFinal()
                    break # El BREAK rompe el while y finaliza el programa
                case _:
                    print("Error: opción inválida, escriba un número entre 1 y 5.")
                    TiempoEspera()
                    
        except ValueError:
            print("Error: Por favor, ingresa únicamente números, no letras.")
            TiempoEspera()

#Funcion de seleccion de frutas
def Seleccion_Frutas():
    global contador_manzanas, contador_bananas, contador_naranjas, contador_peras
    global contador_compras_exitosas
    global contador_compras_fallidas
    while True:
        print("¿Qué tipo de frutas desea comprar?")
        print("1. Manzanas")
        print("2. Peras")
        print("3. Bananas")
        print("4. Naranjas")
        print("5. 'Creo que me retracte... (Regresar a menu principal)'")

        try:
            opcion2 = int(input("¿Qué desea realizar? (1-5)" ))

            match opcion2:
                case 1:
                    cantidad = int(input("¿Cuanto desea llevar? "))
                    if cantidad > 0:
                        contador_manzanas += cantidad  # Aquí se actualiza la variable global
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} manzanas a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1
                
                case 2:
                    cantidad = int(input("¿Cuanto desea llevar? "))
                    if cantidad > 0:
                        contador_peras += cantidad  # Aquí se actualiza la variable global
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} peras a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 3:
                    cantidad = int(input("¿Cuanto desea llevar? "))
                    if cantidad > 0:
                        contador_bananas += cantidad  # Aquí se actualiza la variable global
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} bananas a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 4:
                    cantidad = int(input("¿Cuanto desea llevar? "))
                    if cantidad > 0:
                        contador_naranjas += cantidad  # Aquí se actualiza la variable global
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} naranjas a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 5:
                    print("Regresando al pasillo principal...")
                    break

                case _:
                    print("Error: opción inválida, escriba un número entre 1 y 5.")
                    TiempoEspera()

        except ValueError:
            print("Error: Por favor, ingresa únicamente números, no letras.")
            TiempoEspera()

#Funcion de seleccion de verduras
def Seleccion_Verduras():
    global contador_pepinos, contador_lechuga, contador_tomates, contador_zanahorias
    global contador_compras_exitosas
    global contador_compras_fallidas
    while True:
        print("¿Qué tipo de verduras desea comprar?")
        print("1. Pepinos")
        print("2. Lechugas")
        print("3. Tomates")
        print("4. Zanahoria")
        print("5. 'Creo que me retracte... (Regresar a menu principal)'")

        try:
            opcion3 = int(input("¿Qué desea realizar? (1-5) "))

            match opcion3:
                case 1:
                    cantidad = int(input("¿Cuanto desea llevar? "))
                    if cantidad > 0:
                        contador_pepinos += cantidad  # Aquí se actualiza la variable global
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} pepinos a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1
                
                case 2:
                    cantidad = int(input("¿Cuanto desea llevar? "))
                    if cantidad > 0:
                        contador_lechuga += cantidad  # Aquí se actualiza la variable global
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} lechuga a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 3:
                    cantidad = int(input("¿Cuanto desea llevar? "))
                    if cantidad > 0:
                        contador_tomates += cantidad  # Aquí se actualiza la variable global
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} tomates a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 4:
                    cantidad = int(input("¿Cuanto desea llevar? "))
                    if cantidad > 0:
                        contador_zanahorias += cantidad  # Aquí se actualiza la variable global
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} zanahorias a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 5:
                    print("Regresando al pasillo principal...")
                    break

                case _:
                    print("Error: opción inválida, escriba un número entre 1 y 5.")
                    TiempoEspera()

        except ValueError:
            print("Error: Por favor, ingresa únicamente números, no letras.")
            TiempoEspera()

#Funcion de seleccion de lacteos
def Seleccion_Lacteos():
    global contador_leche, contador_yogurt, contador_queso, contador_mantequilla
    global contador_compras_exitosas
    global contador_compras_fallidas
    while True:
        print("¿Qué tipo de lácteos desea comprar?")
        print("1. Leche")
        print("2. Yogurt")
        print("3. Queso")
        print("4. Mantequilla")
        print("5.'Creo que me retracte... (Regresar a menu principal)'")

        try:
            opcion4 = int(input("¿Qué desea realizar? (1-5) "))

            match opcion4:
                case 1:
                    cantidad = int(input("¿Cuánto desea llevar? "))
                    if cantidad > 0:
                        contador_leche += cantidad
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} leche a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 2:
                    cantidad = int(input("¿Cuánto desea llevar? "))
                    if cantidad > 0:
                        contador_yogurt += cantidad
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} yogurt a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 3:
                    cantidad = int(input("¿Cuánto desea llevar? "))
                    if cantidad > 0:
                        contador_queso += cantidad
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} queso a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 4:
                    cantidad = int(input("¿Cuánto desea llevar? "))
                    if cantidad > 0:
                        contador_mantequilla += cantidad
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} mantequilla a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 5:
                    print("Regresando al pasillo principal...")
                    break

                case _:
                    print("Error: opción inválida, escriba un número entre 1 y 5.")
                    TiempoEspera()

        except ValueError:
            print("Error: Por favor, ingresa únicamente números, no letras.")
            TiempoEspera()

#Funcion de seleccion de carnes
def Seleccion_Carnes():
    global contador_pollo, contador_res, contador_pescado, contador_cerdo
    global contador_compras_exitosas
    global contador_compras_fallidas
    while True:
        print("¿Qué tipo de carnes desea comprar?")
        print("1. Pollo")
        print("2. Res")
        print("3. Pescado")
        print("4. Cerdo")
        print("5. 'Creo que me retracte... (Regresar a menu principal)'")

        try:
            opcion5 = int(input("¿Qué desea realizar? (1-5) "))

            match opcion5:
                case 1:
                    cantidad = int(input("¿Cuánto desea llevar? "))
                    if cantidad > 0:
                        contador_pollo += cantidad
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} pollo a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 2:
                    cantidad = int(input("¿Cuánto desea llevar? "))
                    if cantidad > 0:
                        contador_res += cantidad
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} res a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 3:
                    cantidad = int(input("¿Cuánto desea llevar? "))
                    if cantidad > 0:
                        contador_pescado += cantidad
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} pescado a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 4:
                    cantidad = int(input("¿Cuánto desea llevar? "))
                    if cantidad > 0:
                        contador_cerdo += cantidad
                        contador_compras_exitosas += 1
                        print(f"¡Añadiste {cantidad} cerdo a tu carrito!")
                    else:
                        print("Error: Debes llevar al menos 1.")
                        contador_compras_fallidas += 1

                case 5:
                    print("Regresando al pasillo principal...")
                    break

                case _:
                    print("Error: opción inválida, escriba un número entre 1 y 5.")
                    TiempoEspera()

        except ValueError:
            print("Error: Por favor, ingresa únicamente números, no letras.")
            TiempoEspera()

def ReporteFinal():
    #Llamar contadores generales
    global contador_frutas, contador_verduras, contador_lacteos, contador_carnes
    #Contadores de frutas
    global contador_manzanas, contador_bananas, contador_naranjas, contador_peras
    #Contadores de verduras
    global contador_pepinos, contador_lechuga, contador_tomates, contador_zanahorias
    #Contadores de lacteos
    global contador_leche, contador_yogurt, contador_queso, contador_mantequilla
    #Contadores de carnes
    global contador_pollo, contador_res, contador_pescado, contador_cerdo
    #Contador de compras exitosas y fallidas
    global contador_compras_exitosas, contador_compras_fallidas

    # Calculamos los totales por categoría sumando los productos individuales
    contador_frutas = contador_manzanas + contador_peras + contador_bananas + contador_naranjas
    contador_verduras = contador_lechuga + contador_tomates + contador_zanahorias + contador_pepinos
    contador_lacteos = contador_leche + contador_yogurt + contador_queso + contador_mantequilla
    contador_carnes = contador_pollo + contador_res + contador_pescado + contador_cerdo

    total_articulos = contador_frutas + contador_verduras + contador_lacteos + contador_carnes

    print("\n========================================")
    print("¡Has realizado tus compras con éxito!")
    print("Repasemos lo que llevas en el carrito:")
    print("========================================\n")

    # Mostramos solo lo que compró usando condicionales if
    print("--- FRUTAS ---")
    if contador_manzanas > 0:
        print(f"- Manzanas: {contador_manzanas}")
    if contador_peras > 0:
        print(f"- Peras: {contador_peras}")
    if contador_bananas > 0:
        print(f"- Bananas: {contador_bananas}")
    if contador_naranjas > 0:
        print(f"- Naranjas: {contador_naranjas}")
    if contador_frutas > 0:
        print(f"Total de Frutas: {contador_frutas}\n")
    else:
        print("No compraste ninguna fruta")

    print("--- VERDURAS ---")
    if contador_pepinos > 0:
        print(f"- Pepinos: {contador_pepinos}")
    if contador_lechuga > 0:
        print(f"- Lechugas: {contador_lechuga}")
    if contador_tomates > 0:
        print(f"- Tomates: {contador_tomates}")
    if contador_zanahorias > 0:
        print(f"- Zanahorias: {contador_zanahorias}")

    if contador_verduras > 0:
        print(f"Total de Verduras: {contador_verduras}\n")
    else:
        print("No compraste ninguna verdura")

    print("--- LACTEOS ---")
    if contador_leche > 0:
        print(f"- Leche: {contador_leche}")
    if contador_yogurt > 0:
        print(f"- Yogurt: {contador_yogurt}")
    if contador_queso > 0:
        print(f"- Queso: {contador_queso}")
    if contador_mantequilla > 0:
        print(f"- Mantequilla: {contador_mantequilla}")
    
    if contador_lacteos > 0:
        print(f"Total comprado en lacteos: {contador_lacteos}\n")
    else:
        print("No adquiriste ningun producto de lacteos")

    print("--- CARNES ---")
    if contador_pollo > 0:
        print(f"- Pollo: {contador_pollo}")
    if contador_res > 0:
        print(f"- Res: {contador_res}")
    if contador_pescado > 0:
        print(f"- Pescado: {contador_pescado}")
    if contador_cerdo > 0:
        print(f"- Cerdo: {contador_cerdo}")
    
    if contador_carnes > 0:
        print(f"Total comprado en carnes: {contador_carnes}\n")
    else:
        print("No compraste ningun producto de carnes")

    print("--- RESUMEN DE TU VISITA ---")
    print(f"Total de artículos en tu carrito: {total_articulos}")
    print(f"Transacciones exitosas: {contador_compras_exitosas}")
    print(f"Errores al comprar (cantidades inválidas): {contador_compras_fallidas}")
    print("========================================")
    print("¡Gracias por tu compra! Vuelve pronto.")

#Arranque del juego
if __name__ == "__main__":
    main()