from .graph import BaseGraph


class MovieGraph(BaseGraph):

    def all(self, actor=None):

        where = ''
        if actor:
            where = "WHERE p.name =~ '(?i).*" + actor + ".*' "

        query = "MATCH (m:Movie)<-[:ACTED_IN]-(p:Person) " + where + " RETURN m LIMIT {limit}"

        return self.graph.run(query, {"limit": 100})

    def details(self, title):
        query = "MATCH (m:Movie)<-[r]-(p:Person) \
                WHERE m.title = '" + title + "' \
                RETURN m,r,p"

        return self.graph.run(query)
