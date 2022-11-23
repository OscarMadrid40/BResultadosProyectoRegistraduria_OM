from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):
        print("Creando Controlador Partido")
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        print("Listando todos los partidos")
        return self.repositorioPartido.findAll()

    def create(self, infoPartido):
        print("Creando un partido")
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self, id):
        print("Mostrando un Partido con id ", id)
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartido):
        print("Actualizando Materia con id ", id)
        partidodActual = Partido(self.repositorioPartido.findById(id))
        partidodActual.nombre = infoPartido["nombre"]
        partidodActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(partidodActual)

    def delete(self, id):
        print("Elimiando Partido con id ", id)
        return self.repositorioPartido.delete(id)

