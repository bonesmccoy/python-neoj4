import unittest
from movies.movie_details_builder import MovieDetailsBuilder
from py2neo import Node, Relationship


class TestMovieDetailsBuilder(unittest.TestCase):

    def test_build_actor(self):
        builder = MovieDetailsBuilder()
        movie = Node("Movie", title="The Matrix", released=1999, tagline ="Welcome to the Real World")
        actor = Node("Person", name="Keanu Reeves", born=1964)
        relationship = Relationship(actor, "ACTED_IN", movie)

        builder.add(movie, relationship, actor)

        actor = Node("Person", name="Laurence Fishburne", born=1961)
        builder.add(movie, relationship, actor)

        details = builder.create()

        self.assertEqual(details['details']['title'], "The Matrix")
        self.assertEqual(2, len(details['actors']))
        self.assertEqual(0, len(details['directors']))
        self.assertEqual(0, len(details['producers']))

if __name__ == '__main__':
    unittest.main()