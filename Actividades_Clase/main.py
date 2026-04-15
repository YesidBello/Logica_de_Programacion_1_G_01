# Validación de contraseña
def validate_passwword(PASSWORD):
    if len(PASSWORD) < 8:
        return False
    valid_especials = "*-+/&<$"

    # Los detectores inician en falso
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Revisar letra por letra
    for char in PASSWORD:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in valid_especials:
            has_special = True

    # Si todo es verdadero la contraseña es admitida
    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False


# Iniciamos registro en el sistema
while True:
    new_USERNAME = input("Crea un nuevo usuario: ")
    new_PASSWORD = input("Crea una nueva contraseña: ")
    is_valid = validate_passwword(new_PASSWORD)

    # Si la contraseña es válida
    if is_valid:
        print("Registro exitoso! Tu contraseña es segura.")

        # Rompemos el ciclo infinito
        break
    else:
        print(
            "Error: La contraseña debe tener minímo 8 caracteres y contener"
            " al menos: una mayúscula, una minúscula, un número y un caracter"
            " especial (*-+/&<$)."
        )
        print("Por favor intenta de nuevo.\n")

# Ingreso al sistema
print("\n---INICIO DE SESION---")
print("Por favor ingresa tus credenciales para continuar.\n")

# Intentos máximos
attemps = 0
while True < 3:

    login_USERNAME = input("Ingresa tu usuario: ")
    login_PASSWORD = input("Ingresa tu contraseña: ")

    # Ambos datos deben coincidir (comparación)
    if login_USERNAME == new_USERNAME and login_PASSWORD == new_PASSWORD:
        print(f"\nBienvenido al sistema {login_USERNAME}!")

        # Rompemos el ciclo
        break
    else:

        # Contamos errores
        attemps += 1
        intentos_restantes = 3 - attemps
        if intentos_restantes > 0:
            print("\nAcceso denegado. Usuario y/o contraseña incorrectos.")
            print(
                f"Intenta de nuevo. Tienes {intentos_restantes} intentos"
                " restantes.\n"
            )
        else:
            print("\nAcceso denegado. Cuenta bloqueada!")
            print("Por favor intenta de nuevo luego de 72 horas")
            print("\n***72 HORAS DE ESPERA***")

            # Reiniciamos los datos
            attemps = 0
