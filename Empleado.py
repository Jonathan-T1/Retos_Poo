class Empleado():

    # Atributos
    cargo = ''
    valorhora = 0
    horastrabajadas = 0
    departamento = ''

    # Métodos
    def pedirDatos(self):
        self.nombre = input('Ingrese su nombre: ')
        self.apellido = input('Ingrese su apellido: ')
        self.tipoDoc = input('Ingrese el tipo de documento: ')
        self.documento = int(input('Ingrese el número de documento: '))
        self.cargo = input('Ingrese su cargo: ')
        self.valorhora = int(input('Ingrese el valor a pagar por hora de trabajo: '))
        self.departamento = input('Ingrese el area en el que trabaja: ')    
    def mostrarPersona(self):
        print(f'Nombre: {self.nombre} \nApellido: {self.apellido} \nTipo de documento: {self.tipoDoc} \nDocumento: {self.documento} \nHoras trabajadas: {self.horastrabajadas} \nValor de la hora: {self.valorhora}')
    def calcularHonorarios(self):
        self.horastrabajadas = int(input('Ingrese las horas trabajadas: '))
        honorarios = (self.valorhora * self.horastrabajadas) - 0.966
        print(f'Sus honorarios correspondientes son: {honorarios}')