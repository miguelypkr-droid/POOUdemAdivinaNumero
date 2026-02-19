import random

class Jugador:

# nombre (str): Nombre del jugador.
# puntaje (int): Puntos obtenidos al adivinar correctamente el número.

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.puntaje = 0


# incrementar_puntaje(): Aumenta en 1 el puntaje del jugador cuando acierta.

    def incrementar_puntaje(self):
        self.puntaje += 1

# mostrar_puntaje(): Devuelve una cadena indicando la cantidad de puntos del jugador.

    def mostrar_puntaje(self):
        return f"Puntaje: {self.puntaje}"


class Partida:

# intentos (list): Lista de números ingresados por el jugador durante la partida.
    def __init__(self):
        self.intentos = []

# registrar_intento(intento: int): Almacena cada intento en la lista.

    def registrar_intento(self, intento: int):
        self.intentos.append(intento)

# mostrar_intentos(): Devuelve una lista de los intentos realizados o un mensaje si no hay intentos.
    def mostrar_intentos(self):

        if len(self.intentos) == 0:
            return "No hay intentos"

        return f"Intentos: {self.intentos}"


class JuegoAdivinanza:

    def __init__(self, nombre: str):

        self.nombre = nombre
        self.numero_secreto = random.randint(1, 100)

    def verificar_intento(self, intento: int, jugador: Jugador, partida: Partida):

        partida.registrar_intento(intento)

        if intento < self.numero_secreto:

            return "El número secreto es mayor"

        elif intento > self.numero_secreto:

            return "El número secreto es menor"

        else:

            jugador.incrementar_puntaje()

            self.numero_secreto = random.randint(1, 100)

            return "¡Correcto!"
