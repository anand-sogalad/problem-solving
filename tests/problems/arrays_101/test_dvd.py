import random
from problems.arrays_101.dvd import DVD


class TestDVD:
    dvds: list[DVD] = []

    def test_store_dvd_using_comprehension(self):
        TestDVD.dvds = [
            DVD(f"movie{i}", random.randint(1999, 2006), f"director{i}")
            for i in range(1, 11)
        ]

    def test_access_dvds_using_for_loop(self):
        for idx, dvd in enumerate(TestDVD.dvds):
            assert dvd.movie == TestDVD.dvds[idx].movie

    def test_access_dvds_using_while_loop(self):
        idx = 0
        while idx < len(TestDVD.dvds):
            assert TestDVD.dvds[idx].movie is not None
            idx += 1
