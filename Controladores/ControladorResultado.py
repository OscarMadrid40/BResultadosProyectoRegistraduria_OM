from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa


class ControladorResultado():
    def __init__(self):
        print("Creando Controlador Resultados")
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        print("Listar todos los inscritos")
        return self.repositorioResultado.findAll()
    """
    Asignación mesa y candidato a resultado
    """

    def create(self, infoResultado, idCandidato, idMesa):
        nuevoResultado = Resultado(infoResultado)
        elCandidato = Candidato(self.repositorioCandidato.findById(idCandidato))
        laMesa= Mesa(self.repositorioMesa.findById(idMesa))
        nuevoResultado.candidato = elCandidato
        nuevoResultado.mesa = laMesa
        return self.repositorioResultado.save(nuevoResultado)

    def show(self,id):
        print("Mostrando un resultado con id ",id)
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    """
    Modificación de resultados (candidato y mesa)
    """
    def update(self,id,infoResultado, idCandidato, idMesa):
        print("Actualizando un resultado")
        elResultado = Resultado(self.repositorioResultado.findById(id))
        elResultado.voto = infoResultado["voto"]
        elCandidato = Candidato(self.repositorioCandidato.findById(idCandidato))
        laMesa = Mesa(self.repositorioMesa.findById(idMesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.repositorioResultado.save(elResultado)

    def delete(self,id):
        print("Eliminando un resultado")
        return self.repositorioResultado.delete(id)

    """
    Obtener todos los candidatos inscritos en una mesa
    """

    def listarInscritosEnMesa(self, idMesa):
        return self.repositorioResultado.getListadoInscritosEnMesas(idMesa)

    def listarCandidatosEnPartidos(self,idPartido):
        return self.repositorioResultado.getListadoCandidatosEnPartidos(idPartido)