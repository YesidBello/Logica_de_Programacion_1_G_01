USERNAME = 'MichelleS"
PASSWORD = '130901Ms*

attempts = 0

user = input('Ingresa su nombre de usuario: ')
clave = input('Ingrese su password :')

def validar_password(password : str) -> bool:
    """Funcion para validar la longitud del password"""
    if len(password) >= 8:
        return True
    print('La longitud del password es de 8 caracteres')
    return False

























if validar_password(clave):
    if clave == PASSWORD and user == USERNAME:
        print('Bienvenido al sistema')
    else:
        attempts = 1
        while attempts < 3:
            print('Los datos ingresados son incorrectos. Intentelo nuevamente')
            user = input('Ingresa su nombre de usuario: ')
            clave = input('Ingrese su password :')
            if clave == PASSWORD and user == USERNAME:
                attempts = 0
                print(f'Bienvenido al sistema {user}')
                break
            attempts = attempts + 1
        else:
            print('su cuenta ha sido bloqueada')
else:
    print('La longitud del password es de 8 caracteres')










