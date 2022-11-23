from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato

class ControladorMesa():
    def __init__(self):
        print("Creando Controlador Mesa")
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        print("Listar todas las Mesas")
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        print("Crear una Mesa")
        nuevaMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        print("Mostrando una Mesa con id ", id)
        laMesa = Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__

    def update(self, id, infoMesa):
        print("Actualizando Mesa con id ", id)
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        mesaActual.numeromesa = infoMesa["numero_mesa"]
        mesaActual.cedulasinscritas = infoMesa["cedula_inscrita"]
        return self.repositorioMesa.save(mesaActual)

    def delete(self, id):
        print("Elimiando Mesa con id ", id)
        return self.repositorioMesa.delete(id)

    """
    Relación mesa y candidato
    """
    def asignarCandidato(self, id, idCandidato):
        print("Asignando a una Mesa un Candidato con id", id)
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        candidatoActual = Candidato(self.repositorioCandidato.findById(idCandidato))
        mesaActual.candidato = candidatoActual
        return self.repositorioMesa.save(mesaActual)
