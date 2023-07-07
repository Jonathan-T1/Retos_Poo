class Carro:

    # En Python, se utiliza el prefijo de doble guion bajo "__", para marcar un atributo o un mértodo como privado y que solo pueda ser accedido dentro de la clase.  

    def __init__(self, marca, modelo, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    # Todos los atributos estan marcados como privado.

    # Para acceder a los atributos que se encuentran privados, usamos el método "get", en este caso vamos a devolver el valor del precio

    def get_precio(self):
        return self.__precio