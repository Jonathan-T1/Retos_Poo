from Carro import Carro

# Creamos el objeto, instanciando nuestra clase Carro. 

mustang = Carro('Ford', 'Mustang', 50000)

# Accedemos al precio del objeto con el método.

print(mustang.get_precio())

# En consola debe de salir el precio que ya pusimos. 50000

# Al intentar imprimir el precio de esta manera "print(mustang.__precio)", nos saltara un mensaje de error, debido a que es privado. 