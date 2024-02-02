def verificar_longitud_palabra(palabra):
    longitud = len(palabra)

    if 4 <= longitud <= 8:
        print("La palabra es correcta.")
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")

# Solicitar al usuario que ingrese una palabra
palabra_ingresada = input("Ingresa una palabra: ")

# Verificar la longitud de la palabra
verificar_longitud_palabra(palabra_ingresada)