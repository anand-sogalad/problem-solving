import random


class DVD:
    def __init__(self, movie: str, year: int, director: str):
        self.movie = movie
        self.year = year
        self.director = director

    def __str__(self):
        return f"DVD: {self.movie}-{self.year}-{self.director}"

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, movie: str):
        self.__movie = movie

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director: str):
        self.__director = director


if __name__ == "__main__":
    # store DVDs in an array (list in python)
    dvds = [
        DVD(f"movie{i}", random.randint(1995, 2005), f"director{i}")
        for i in range(1, 11)
    ]

    # iterate through each dvds
    for dvd in dvds:
        print(dvd)

    # iterating through array using index
    for idx in range(len(dvds)):
        print(dvds[idx])
