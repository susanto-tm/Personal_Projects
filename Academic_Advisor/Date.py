class Date:
    def __init__(self, date):
        self.month, self.date, self.year = date

    def set_month(self, val):
        self.month = val

    def get_month(self):
        return self.month

    def set_date(self, val):
        self.date = val

    def get_date(self):
        return self.date

    def set_year(self, val):
        self.year = val

    def get_year(self):
        return self.year
