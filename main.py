import csv  # lib used to parse data
import ast  # lib used to convert data to more useful data types
from Movie import Movie  # Movie object
from Recommender import Recommender  # Reccommender object


# READING IN IMPORTANT INFO FROM MOVES.CSV FILE AND CREATING MOVIE OBJECTS
with open('tmdb_5000_movies.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    MovieList = {}  # dictionary for all movies
    for col in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            # Checking to see if a movie has certain voter score and ranking
            if float(col[18]) < 6 or float(col[8]) < 20:
                continue  # If the movie does not meet the condition, it is ignored

            # Finding Movie genres for current cell
            genres = {}

            col[1] = ast.literal_eval(col[1])
            for g in col[1]:
                genres[g["name"]] = g["name"]
            movieID = col[3]

            # Finding keywords of movie in current cell
            keywords = {}
            col[4] = ast.literal_eval(col[4])
            for k in col[4]:
                keywords[k["name"]] = k["name"]

            # Getting movie title, popularity, and length of movie
            title = col[6]
            popularity = col[8]
            runtime = col[13]

            # Getting languages movie is available in
            languages = {}
            col[14] = ast.literal_eval(col[14])
            for l in col[14]:
                languages[l["name"]] = l["name"]

            # Getting movie voted average
            voterAv = col[18]

            # Initializing movie object and adding it to the dicitonary, with a key of the movieID
            m = Movie(genres, movieID, keywords, title,
                      popularity, runtime, languages, voterAv)
            MovieList[str(movieID)] = m

# READING IMPORTANT INFO FROM CREDITS.CSV FILE AND ADDING TO EXISTING MOVIE OBJECT USING KEYS
with open('tmdb_5000_credits.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for col in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(col)}')
            line_count += 1
        else:
            # Checking to see if the ID exists in the list of movies, and if it does turn data into readable info
            if col[0] in MovieList:
                temp = MovieList[col[0]]
                col[2] = ast.literal_eval(col[2])
                col[3] = ast.literal_eval(col[3])

                # Getting data for cast
                cast = {}
                for c in col[2]:
                    cast[c["name"]] = c["name"]

                # Finding writers and director of current movie
                director = ""
                writer = {}
                for p in col[3]:
                    if p["job"] == "Director":
                        director = p["name"]
                    elif p["job"] == "Writer":
                        writer[p["name"]] = p["name"]
                # Adding info about the movie to the existing object
                temp.addCredits(cast, writer, director)


# GETTING USER INPUTS
genres = input('Input Favorite Genres: ')
#genres = "Action Adventure Crime"
genres = genres.split(" ")

actors = input('Input Favorite Actors: ')
#actors = "Christian Bale, Tom Hardy"
actors = actors.split(", ")

directors = input('Input Favorite Directors: ')
#directors = "Christopher Nolan"
directors = directors.split(", ")

writers = input('Input Favorite Movie Writers: ')
#writers = "Christopher Nolan"
writers = writers.split(", ")

spokenLanguage = input('Input Language: ')
#spokenLanguage = "English"

runtime = input(
    'Do you like Long Movies. Type long or short (approx. 2 > hr): ')
#runtime = "long"

keywords = input(
    'Enter Some Keywords that may help with the Recommendations: ')
#keywords = "terrorist, dc comics"
keywords = keywords.split(", ")


# CREATING RECCOMMENDER OBJECT AND CALCULATING WEIGHTS OF MOVIES
recommender = Recommender(genres, actors, directors,
                          writers, spokenLanguage, runtime, keywords, MovieList)
recommender.Weight()


# SEARCHING DICTIONARY FOR HIGHEST WEIGHTED MOVIES (BEST TO RECCOMMEND)
maxWeights = [Movie(), Movie(), Movie(), Movie(), Movie()]
movieTitles = ["", "", "", "", ""]


for i in range(5):
    minWeight = 0
    for key in MovieList.keys():
        if MovieList[key].Weight > minWeight and MovieList[key] not in maxWeights:
            minWeight = MovieList[key].Weight
            maxWeights[i] = MovieList[key]

# PRINT MOVIES TO RECCOMMEND
print('\n')
ctr = 1
for i in maxWeights:
    print(ctr, i.movieTitle)
    ctr += 1


with open('TeamRabbits-Output.csv', mode='w') as rec_file:
    rec_writer = csv.writer(rec_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

    rec_writer.writerow(['Title'])
    for i in maxWeights:
        rec_writer.writerow([i.movieTitle])
