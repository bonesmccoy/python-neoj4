from graph.movie_graph import MovieGraph


def movies(actor=None):
    movie = MovieGraph()
    results = movie.all(actor)

    return [dict(movie['m']) for movie in results]

