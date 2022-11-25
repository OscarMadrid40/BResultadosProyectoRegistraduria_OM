from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):

    def getTotalVotosPorMesa(self, idMesa):
        print("Mostrando el total de votos en una mesa")
        query = {
            "$match": {"mesa.$id": ObjectId(idMesa)}
        }
        query1 = {
            "$group":{
                "_id":"$mesa",
                "totalVotosEnMesas":{
                    "$sum":"$voto",
                },

                "doc":{"$first":"$$ROOT" }
            }
        }
        query2 = {
            "$sort":{
                "suma":1
            }
        }
        pipeline = [query,query1,query2]
        return self.queryAggregation(pipeline)

