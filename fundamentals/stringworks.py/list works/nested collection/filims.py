movies = [
    
    {
        "title": "Drishyam", 
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]


# total number of movies

movies_count=len(movies)

print("movies count",movies_count)

# movies with a genre drama

genre_filter=[m.get("title") for m in movies if "drama"]


# print latest movie

def get_year(mov):
    return mov.get("years")

# latest_movies=max(movies,key=get_year)

# latest_movie=[m.get("title") for m in movie if m.get("year")==latest_movie.get]
# print(latest_movie)

# print oldest movie

movie_dictionary={}

for m in movies:
    release_year=m.get("year")

    if release_year in movie_dictionary:
        movie_dictionary.get(release_year).append(m.get("title"))
    else:

        movie_dictionary[release_year]=[m.get("title")]
print(movie_dictionary)
