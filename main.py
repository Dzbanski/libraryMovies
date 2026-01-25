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
            return f'{self.title} S{self.season:02d}E{self.episode:02d} {self.number_play}'

    
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

def get_movies(films):
    moviess = [z for z in films if not isinstance(z, Series)]
    movies_sorted = sorted(moviess, key=lambda x: x.title)
    return movies_sorted

def get_series(films):
    seriess = [k for k in films if isinstance(k, Series)]
    series_sorted = sorted(seriess, key=lambda x: x.title)
    return series_sorted

def generate_views(films):
    generated_view = random.choice(films)
    generated_view.number_play += random.randint(0,100)
    return generated_view

def multiple_views(films, times=10):
    """
    Function use while loop to activate function generate_views ten times. While list watched will have 10 records loop will work. If film not in watched list it will be append.
    """
    watched = []

    while(len(watched)<times):
        film = generate_views(films)
        if film not in watched :
            watched.append(film)

    return watched

def search(films):

    tytul = input("Podaj tytuł filmu:").lower()

    for film in films:
        if tytul in film.title.lower():
            return film
        
    return f'There is no such a movie or serie'

def top_titles(films, content_type="movies"):
   x = datetime.datetime.now()
   print("Najpopularniejsze filmy i seriale dnia", x.strftime("%d.%m.%Y"))

   if content_type == "movies": 
        sorted_titles = get_movies(films)
   else:
       sorted_titles = get_series(films)
                        
   return sorted(sorted_titles, key=lambda x: x.numer_play, reverse=True)[:3]

    
   
def add_series(films, title, release, species, season, num_i, number_play=0):
    for i in range(1, num_i+1):
        films.append(Series(title, release, species, season, i, number_play))
        
def count_episodes(films, title):

    count = 0
    for i in films:
        if i.title.lower() == title.lower():
            count += 1
    return count

if __name__ == "__main__":

    list_of_films = []
    list_of_films.extend(rand_movies())
    list_of_films.extend(rand_series())

    print("Biblioteka filmów")

    watched = multiple_views(list_of_films, 10)
    
    for film in watched:
     print(film)

    for z in top_titles(list_of_films, "series"):
        print(z)

   

