from faker import Faker
import random
import datetime

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
        return f'{self.title} ({self.release}) {self.number_play}'
    
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

def rand_movies(how_much=50):
    """
    Function use library random to rand a fake title of a film, integer and append data to movies list.
    """
    movies = []

    for i in range(how_much):
        title = fake.sentence(nb_words=3).replace(".", "")
        release = random.randint(1950,2025)
        species = rand_species()
        movies.append(Movies(title, release, species))
    return movies

def rand_series(how_muc = 50, much_season = 8, much_episode = 12):
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

def generate_views():
    generated_view = random.choice(list_of_films)
    generated_view.number_play += random.randint(0,100)
    return generated_view

def multiple_views(times=10):
    """
    Function use while loop to activate function generate_views ten times. While list watched will have 10 records loop will work. If film not in watched list it will be append.
    """
    watched = []

    while(len(watched)<times):
        film = generate_views()
        if film not in watched :
            watched.append(film)

    return watched

def search():

    tytul = input("Podaj tytuł filmu:").lower()

    for film in list_of_films:
        if tytul in film.title.lower():
            return film
        
    return f'There is no such a movie or serie'

def top_titles(content_type="movies"):
   x = datetime.datetime.now()
   print("Najpopularniejsze filmy i seriale dnia", x.strftime("%d.%m.%Y"))

   if content_type == "movies":
        titles_top = [t for t in get_movies()]
        sorted_titles = sorted(titles_top, key=lambda x: x.number_play, reverse=True)
        return sorted_titles[:3]
   else:
       titles_top = [t for t in get_series()]
       sorted_titles = sorted(titles_top, key=lambda x: x.number_play, reverse=True)
       return sorted_titles[:3]
   
def add_series(title, release, species, season, num_i, number_play=0):
    for i in range(1, num_i+1):
        list_of_films.append(Series(title, release, species, season, i, number_play))
        
def count_episodes(title):

    count = 0
    for i in list_of_films:
        if i.title.lower() == title.lower():
            count += 1
    return count

if __name__ == "__main__":
    print("Biblioteka filmów")

    watched = multiple_views(10)

    for film in watched:
     print(film)

    for z in top_titles("movies"):
        print(z)

