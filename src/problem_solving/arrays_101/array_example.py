# create A DVD class for creating DVD object
class DVD:
    def __init__(self, movie: str, director: str, rel_year: int):
        self.movie = movie
        self.director = director
        self.rel_year = rel_year

    def __str__(self):
        return f"DVD: movie={self.movie} - director={self.director} - released={self.rel_year}"


if __name__ == "__main__":
    # creating DVD array/list
    # unlike java, python list are dynamic sized arrays
    dvds: list[DVD] = []

    # inserting value to array in python
    # this throws execpetion as array length is 0, where as it works well in  java as java is fixed lenth and memory allocated at front
    # dvds[2] = DVD("Good", "Great", 1999)

    # appending value to list
    dvds.append(DVD("Good", "Great", 1999))
    print(dvds)

    # accessing value to list
    dvd = dvds[0]
    print(dvd)
