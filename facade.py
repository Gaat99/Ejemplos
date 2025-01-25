class Luces:
    def encender(self):
        print("Luces encendidas")

    def apagar(self):
        print("Luces apagadas")

class Proyector:
    def encender(self):
        print("Proyector encendido")

    def apagar(self):
        print("Proyector apagado")

class Sonido:
    def encender(self):
        print("Sonido activado")

    def apagar(self):
        print("Sonido apagado")

class CineFacade:
    def __init__(self):
        self.luces = Luces()
        self.proyector = Proyector()
        self.sonido = Sonido()

    def iniciar_pelicula(self):
        print("Preparando todo para ver la película...")
        self.luces.apagar()
        self.proyector.encender()
        self.sonido.encender()
        print("¡Disfruta de la película!")

    def terminar_pelicula(self):
        print("Terminando película...")
        self.luces.encender()
        self.proyector.apagar()
        self.sonido.apagar()
        print("¡Hasta la próxima!")



cine = CineFacade()
cine.iniciar_pelicula()   # Se prepara todo para ver la película
cine.terminar_pelicula()  # Se apagan las luces y demás cuando termina
