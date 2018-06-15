# sample 1
class Person:
    def getData(self):
        return 'hello world!'

myPerson = Person()
print myPerson.getData()


# sample 2
class Human(Person):
    info='first'
    data='second'
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def getFullName(self):
        result = self.name, self.lastName
        return result

person = Human('joel', 'gonzales')
print 'fullname', person.getFullName()
print 'info', person.info
print 'name', person.name
print 'lastname', person.lastName

print 'Inheritance person', person.getData()



# extra
class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0

my_account = BankAccount(15)
my_account.withdraw(5)
print my_account.balance



# herencia
class Persona(object):
    # "Clase que representa una persona."
    def __init__(self, identificacion, nombre, apellido):
        # "Constructor de Persona"
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return " %s: %s, %s" %
            (str(self.identificacion), self.apellido, self.nombre)

class AlumnoFIUBA(Persona):
    # "Clase que representa a un alumno de FIUBA."
    def __init__(self, identificacion, nombre, apellido, padron):
        # "Constructor de AlumnoFIUBA"
        # llamamos al constructor de Persona
        Persona.__init__(self, identificacion, nombre, apellido)
        # agregamos el nuevo atributo
        self.padron = padron

a = AlumnoFIUBA("DNI 35123456", "Damien", "Thorn", "98765")

 print a
