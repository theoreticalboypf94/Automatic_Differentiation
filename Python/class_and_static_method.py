class Data:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <=31 and month < 13 and year < 3999

date2 = Data.from_string('11-09-2012')
is_date = Data.is_date_valid('11-09-2012')

print(date2)
print(is_date)

def f(x):
    def g(y):
        return x + 15
    return g(2) + 1

print(f(2))