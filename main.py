from faker import Faker

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
    
    list_of_films = []

class Series(Movies):
    def __init__(self, title, release, species, episode, season, number_play=0):
        super().__init__(title, release, species, number_play)
        self.episode = episode
        self.season = season
        
    def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d}'

