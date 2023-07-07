from Persona import Persona
from Empleado import Empleado

op = 1

# pruebaPersona.mostrarPersona()

print('¡Bienvenido!')

while op == 1:
        
    print('1. Para registrarse como empleado.')
    print('2. Para registrarse como persona ordinaria.')
    print('3. Para salir.')

    opcion = int(input('Seleciones un opción: '))

    if opcion == 1:
        print('Ingrese sus datodo correcpondientes: \n')
        empleado = Empleado()
        empleado.pedirDatos()
        empleado.calcularHonorarios()
        empleado.mostrarPersona()

    elif opcion == 2:
        print('Ingrese sus datodo correcpondientes: \n')
        persona = Persona()
        persona.pedirDatos()
        persona.mostrarPersona()
        persona.calcularImc()
        persona.mayorEdad()

    elif opcion == 3:
        print('Gracias por usar nuestros servicios')
        break

    else:
        print('Opción no valida.')

    op =  int(input('1. Para añadir persona/empleado. \n2. Para salir. \n'))