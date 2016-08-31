class MovieDetailsBuilder:

    def __init__(self):
        self._actors = []
        self._producers = []
        self._directors = []
        self._movie = None

    def add(self, movie, relationship, person):

        if not self._movie:
            self._movie = movie
        if relationship.type() == 'ACTED_IN':
            self._actors.append(dict(person))
        if relationship.type() == 'PRODUCED':
            self._producers.append(dict(person))
        if relationship.type() == 'DIRECTED':
            self._directors.append(dict(person))

    def create(self):

        return dict({"details": self._movie, "actors": self._actors, "producers": self._producers, "directors": self._directors})