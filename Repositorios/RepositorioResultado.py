from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoInscritosEnMesas(self, idMesa):
        print("Mostrando una mesa con sus candidatos")
        theQuery = {"mesa.$id": ObjectId(idMesa)}
        return self.query(theQuery)

    def getListadoCandidatosEnPartidos(self, idPartido):
        print("Mostrando un partido con sus candidatos")
        theQuery = {"partido.$id": ObjectId(idPartido)}
        return self.query(theQuery)

    def getMesaMayorAMenor(self):
        query1 = {
            "$group": {
                "_id": "mesa",
                "max": {
                    "$max": "$mesa_final"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)

    def test(self, idMesa):
        query1 = {
            "$match": {"mesa.$id": ObjectId(idMesa)}
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)

