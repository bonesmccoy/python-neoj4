from .graph import DataPointGraph


class MovieGraph(DataPointGraph):

    def all(self, actor=None):

        where = ''
        if (actor is not None):
            where = "WHERE p.name =~ '(?i).*" + actor + ".*' "

        query = "MATCH (m:Movie)<-[:ACTED_IN]-(p:Person) " + where + " RETURN m LIMIT {limit}"

        return self.graph.run(query, {"limit": 100})