from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Mesa import Mesa
from bson import ObjectId

class RepositorioMesa(InterfaceRepositorio[Mesa]):
    def getListadoCandidatosEnMesas(self,idMesa):
        theQuery = {"candidato.$id": ObjectId(idMesa)}
        return self.query(theQuery)
