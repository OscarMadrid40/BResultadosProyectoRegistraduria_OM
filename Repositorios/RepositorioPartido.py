from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Partido import Partido
class RepositorioPartido(InterfaceRepositorio[Partido]):

    def contidadVotosPorMesa(self,idMesa):
        query = {
            "$group":{
                "_id":"$partido",
                "total":{
                    "$sum":"$cantidad_votos"
                },
                "doc":{"$first":"$$ROOT"}
            }
        }
        pipeLine = [query]
        return self.queryAggregation(pipeLine)