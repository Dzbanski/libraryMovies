from faker import Faker
import random

fake = Faker('pl_PL')


class Movies():
    def __init__(self, title, release, species, number_play=0):
        self.title = title
        self.release = release
        self.species = species
        self.number_play = number_play

    def play(self):
        self.number_play += 1

    def __str__(self):
        return f'{self.title} {self.release}'
    
class Series(Movies):
    def __init__(self, title, release, species, season, episode, number_play=0):
        super().__init__(title, release, species, number_play)
        self.season = season
        self.episode = episode
        
    def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d}'

def rand_species():
    species = [
        "Action",
        "Sci-Fi",
        "Comedy",
        "Horror",
        "Thriller",
        "Fantasy"
    ]
    return random.choice(species)

def rand_movies(how_much=10):
    movies = []

    for i in range(how_much):
        title = fake.sentence(nb_words=3).replace(".", "")
        release = random.randint(1950,2025)
        species = rand_species()
        movies.append(Movies(title, release, species))
    return movies

def rand_series(how_muc = 10, much_season = 8, much_episode = 12):
    series = []

    for y in range(how_muc):
        title = fake.sentence(nb_words=3).replace(".", "")
        release = random.randint(1980,2025)
        species = rand_species()
        season = random.randint(1, much_season)
        episode = random.randint(1, much_episode)
        series.append(Series(title, release, species, season, episode))
    return series


list_of_films = []
list_of_films.extend(rand_movies())
list_of_films.extend(rand_series())

def get_movies():
    moviess = [z for z in list_of_films if not isinstance(z, Series)]
    movies_sorted = sorted(moviess, key=lambda x: x.title)
    return movies_sorted

def get_series():
    seriess = [k for k in list_of_films if isinstance(k, Series)]
    series_sorted = sorted(seriess, key=lambda x: x.title)
    return series_sorted
 
wynik = get_movies()
wynik2 = get_series()

for word in wynik2:
    print(word)
