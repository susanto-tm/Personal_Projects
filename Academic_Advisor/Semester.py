class Semester:
    def __init__(self, semester):
        self.sem, self.year = semester

    def set_semester(self, val):
        self.sem = val

    def get_semester(self):
        return self.sem

    def set_year(self, val):
        self.year = val

    def get_year(self):
        return self.year