# Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

def find_movies(flight_length, movie_lengths):

    movies_seen = set()

    for movie in movie_lengths:
        second_movie_length = flight_length - movie
        if second_movie_length in movies_seen:
            return True

        movies_seen.add(movie)
    
    return False