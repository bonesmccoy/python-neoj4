from config import config
from py2neo import Graph, authenticate


class BaseGraph:

    @property
    def graph(self):
        if not self._graph:
            self._graph = Graph(self.endpoint, bolt=False)
        return self._graph

    def __init__(self):
        neo4j_url = config['DATABASE']['URL']
        neo4j_username = config['DATABASE']['USERNAME']
        neo4j_password = config['DATABASE']['PASSWORD']
        authenticate(neo4j_url, neo4j_username, neo4j_password)

        self.endpoint = config['DATABASE']['ENDPOINT']
        self._graph = None

