from graph.movie_graph import MovieGraph
from movies.movie_details_builder import MovieDetailsBuilder


def movies(actor=None):
    movie = MovieGraph()
    results = movie.all(actor)

    return [dict(movie['m']) for movie in results]


def movie_details(title):
    graph = MovieGraph()
    result = graph.details(title)
    builder = MovieDetailsBuilder()

    for record in result:
        movie = record['m']
        relationship = record['r']
        person = record['p']
        builder.add(movie, relationship, person)

    return builder.create()
