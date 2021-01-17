Joshua Melo joshua.melo@ryerson.ca
Dhaval Patel dhaval.h.patel@ryerson.ca
Ruben Plaza ruben.plaza@ryerson.ca

Team Rabbits

Netflux - Movie Recommendation Engine

File Structure: 
netflux/main.py
netflux/Recommendation.py
netflux/Movie.py
netflux/tmdb_5000_credits.csv
netflux/tmdb_5000_movies.csv

In order to run our program, the user will need to have python version 3.8.4 installed on their system.

STEPS TO EXECUTE

Unzip the project folder
From the terminal, in the current directory, run the command:
	$ python3 main.py
The user will be prompted to enter their movie preferences. 
Example Input:
Action Adventure Crime (List seperated by white space. All Capitalized)
Christian Bale, Tom Hardy (List seperated by ", ". All Capitalized)
Christopher Nolan (List seperated by ", ". All Capitalized)
Christopher Nolan (List seperated by ", ". All Capitalized)
English(Single Language- Capitalized)
long ('long' or 'short')
terrorist, dc comics (List seperated by ", ". All Lowercase)
The top 5 five recommended movies will be output to a csv file in the same directory as well as printed in the terminal.
