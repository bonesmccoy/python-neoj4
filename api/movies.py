from graph.movie_graph import MovieGraph
from py2neo import Node, Relationship


def movies(actor=None):
    movie = MovieGraph()
    results = movie.all(actor)

    return [dict(movie['m']) for movie in results]


def movie_details(title):
    graph = MovieGraph()
    result = graph.details(title)

    actors = []
    producers = []
    directors = []
    movie = None
    for record in result:
        if not movie:
            movie = record['m']
        relationship = record['r']
        person = record['p']
        if relationship.type() == 'ACTED_IN':
            actors.append(dict(person))
        if relationship.type() == 'PRODUCED':
            producers.append(dict(person))
        if relationship.type() == 'DIRECTED':
            directors.append(dict(person))

    return dict({"details": movie, "actors": actors, "producers": producers, "directors": directors})
