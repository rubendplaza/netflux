from Movie import Movie


class Recommender:
    def __init__(self, genres, actors, directors, writer, spokenLanguages, runtime, keyWords, movies):
        """
        Class to find movies to reccommend. Takes user input as well as a list of known movies.

        Parameters:
        genres (List): List of genres specified by the user
        actors (List): List of actors specified by the user
        directors(List): List of directors specified by the user
        writer (List): List of writers specified by the user
        spokenLanguages (str): Preferred Language specified by the user
        runtime (str): Preferred Length of Movie specified by the user. Expected input = 'long'/'short'
        keyWords (List): List of keywords to match with movies specified by the user
        movies (dict[Movie]): List of all known movies
        """
        self.genres = genres                        # Bias: 10
        self.actors = actors                        # Bias: 8
        self.directors = directors                  # Bias: 7
        self.writer = writer                        # Bias: 7
        self.spokenLanguages = spokenLanguages      # Bias: 10
        self.runtime = runtime                      # Bias: 3
        self.keyWords = keyWords                    # Bias: 5
        self.movies = movies

    def Weight(self):
        """
        Function to determine the weight of each Movie. Calling this function defines the weight of the list of movies you pass based on
        the entered values by the user. More matched qualities results in a higher weight.

        Parameters:
        None

        Returns:
        None

        Modifies:
        self.movies
        """
        keys = self.movies.keys()
        for id in keys:
            for genre in self.genres:
                if genre in self.movies[id].genres.keys():
                    self.movies[id].Weight += 10
            for actor in self.actors:
                if actor in self.movies[id].cast.keys():
                    self.movies[id].Weight += 8
            for director in self.directors:
                if director == self.movies[id].director:
                    self.movies[id].Weight += 7
            for writer in self.writer:
                if writer in self.movies[id].writer.keys():
                    self.movies[id].Weight += 7
            if self.spokenLanguages in self.movies[id].spokenLanguages.keys():
                self.movies[id].Weight += 10
            if float(self.movies[id].runtime) > 120 and self.runtime == 'long':
                self.movies[id].Weight += 3
            elif float(self.movies[id].runtime) <= 120 and self.runtime == 'short':
                self.movies[id].Weight += 3
            for keyWord in self.keyWords:
                if keyWord in self.movies[id].keyWords.keys():
                    self.movies[id].Weight += 5
