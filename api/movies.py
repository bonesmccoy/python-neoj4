from py2neo import authenticate, Graph

authenticate("192.168.99.100:32769", "neo4j", "admin");
graph = Graph("http://192.168.99.100:32769/db/data", bolt=False)


def movies(actor=None):
    where = ''
    if (actor is not None):
        where = "WHERE p.name =~ '.*" + actor + ".*.' "

    query = "MATCH (m:Movie)<-[:ACTED_IN]-(p:Person) " + where + " RETURN m LIMIT {limit}"
    print(query)
    results = graph.run(query, {"limit": 100})

    return [dict(movie['m']) for movie in results]


