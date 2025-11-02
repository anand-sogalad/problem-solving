from faker import Faker

faker = Faker()


class DVD:
    def __init__(self, movie: str, year: int, director: str, description: str):
        self.movie = movie
        self.year = year
        self.director = director
        self.description = description

    def __str__(self):
        return f"movie: {self.movie}, year: {self.year}, director: {self.director}, description: {self.description}"


class DVDContainer:
    def __init__(self, dvds: list[DVD] | None = None):
        self.container = dvds if dvds else list()

    def add(self, dvd: DVD):
        self.container.append(dvd)

    def remove(self):
        if not self._is_empty():
            return self.container.pop()
        raise IndexError("Container is already empty!")

    def _is_empty(self):
        return len(self.container) == 0

    def __len__(self):
        return len(self.container)

    def __iter__(self):
        return iter(self.container)

    def add_many(self, dvds: list[DVD]):
        self.container.extend(dvds)


if __name__ == '__main__':
    for dvd in DVDContainer([DVD(faker.name(), int(faker.year()), faker.name(), faker.sentence()) for _ in range(10)]):
        print(dvd)
