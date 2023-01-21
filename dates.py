import free_date
import some_money_date
import expensive_date


class Dates:
    def __init__(self, dates):
        self.dates = dates

    def setDate(self, date):
        self.dates.append(date)

    def chargingCheapDates(self):
        self.setDate(free_date.cheap_and_sunny_suggest())
        self.setDate(free_date.cheap_and_some_clouds_suggest())
        self.setDate(free_date.cheap_and_rainny_suggest())
        self.setDate(free_date.cheap_and_night_suggest())

    def chargingSomeMoneyDates(self):
        self.setDate(some_money_date.some_money_and_sunny_suggest())
        self.setDate(some_money_date.some_money_and_some_clouds_suggest())
        self.setDate(some_money_date.some_money_and_rainny_suggest())
        self.setDate(some_money_date.some_money_and_night_suggest())

    def chargingExpensiveDates(self):
        self.setDate(expensive_date.expensive_and_sunny_suggest())
        self.setDate(expensive_date.expensive_and_some_clouds_suggest())
        self.setDate(expensive_date.expensive_and_rainny_suggest())
        self.setDate(expensive_date.expensive_and_night_suggest())

