class Movie:
    def __init__(self, genres={}, movieID="0", keyWords={}, movieTitle="", popularity=0, runtime=0, spokenLanguages={}, voteAverage=0):
        """
        Container class to hold information about individual movies

        Parameters: 
        genres (dict): dictionary of movie genres
        movieID (str): ID to find specific movie
        keyWords (dict): dictionary of keywords used to identify movies
        movieTitle (str): name of movie
        populairy (float): popularity rating of movie
        runtime (float): length of movie
        spokenLanguages (dict): dictionary of languages in the movie
        voteAverage (float): Average rating of movie

        Returns:
        None
        """
        self.Weight = float(voteAverage)
        self.genres = genres
        self.movieID = movieID
        self.keyWords = keyWords
        self.movieTitle = movieTitle
        self.popularity = popularity
        self.runtime = runtime
        self.spokenLanguages = spokenLanguages
        self.voteAverage = voteAverage
        self.director = ""
        self.writer = ""
        self.cast = ""

    def addCredits(self, cast, writer, director):
        """
        Method which adds information from movie credits after movie has already been initialized

        Parameters:
        cast (dict): dictionary of cast members
        writer (dict): dictionary of writers who worked on the movie
        director (str): name of the movie director

        Returns:
        None
        """
        self.cast = cast
        self.writer = writer
        self.director = director

    def __str__(self):
        """
        String representation of a Movie object.

        Parameters:
        None

        Returns:
        str: String of Movie object
        """
        return f'MovieID: {self.movieID} \nGenres: {self.genres} \nkeyWords: {self.keyWords} \nmovieTitle: {self.movieTitle} \npopularity: {self.popularity}\nruntime: {self.runtime} \nlanguages: {self.spokenLanguages} \nvoteAverage: {self.voteAverage} \nCast: {self.cast} \nWriters: {self.writer} \nDirector: {self.director}'
