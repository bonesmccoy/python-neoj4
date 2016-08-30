from .graph import BaseGraph


class MovieGraph(BaseGraph):

    def all(self, actor=None):

        where = ''
        if actor:
            where = "WHERE p.name =~ '(?i).*" + actor + ".*' "

        query = "MATCH (m:Movie)<-[:ACTED_IN]-(p:Person) " + where + " RETURN m LIMIT {limit}"

        return self.graph.run(query, {"limit": 100})