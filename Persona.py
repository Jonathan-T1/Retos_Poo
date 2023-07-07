class Persona:

    # Atributos
    nombre = ''
    apellido = ''
    sexo = ''
    tipoDoc = ''
    documento = 0
    peso = 0
    estatura = 0
    edad = 0

    # Método constructor
    # def __init__(self, nom, ape, sex, tip, doc, pes, est, ed):
    #     self.nombre = nom
    #     self.apellido = ape
    #     self.sexo = sex
    #     self.tipoDoc = tip
    #     self.documento = doc
    #     self.peso = pes
    #     self.estatura = est
    #     self.edad = ed

    # Métodos 
    def pedirDatos(self):
        self.nombre = input('Ingrese su nombre: ')
        self.apellido = input('Ingrese su apellido: ')
        self.sexo = input('Ingrese su género: ')
        self.tipoDoc = input('Ingrese el tipo de documento: ')
        self.documento = int(input('Ingrese el número de documento: '))
        self.peso = int(input('Ingrese su peso en kilogramos: '))
        self.estatura = float(input('Ingrese su estatura: '))
        self.edad = int(input('Ingrese su edad: '))
    def mostrarPersona(self):
        print(f'Nombre: {self.nombre} \nApellido: {self.apellido} \nGénero: {self.sexo} \nTipo de documento: {self.tipoDoc} \nDocumento: {self.documento} \nPeso: {self.peso} \nEstatura: {self.estatura} \nEdad: {self.edad}')
    def calcularImc(self):
        pesoActual = self.peso / self.estatura ** 2 
        if pesoActual < 20:
            print('El peso esta por debajo de lo ideal.')
        elif pesoActual >= 20 and pesoActual <= 25:
            print('El peso es ideal')
        else:
            print('Tiene sobrepeso.') 
    def mayorEdad(self):
        if  self.edad < 18:
            print('Usted es menor de edad.')
        else:
            print('Usted es mayor de edad.')