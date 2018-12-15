#done

class Guitar:
    def __init__(self, name = "", year = 0, cost = 0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        age = 2018 - self.year
        return age

    def is_vintage(self):
        if 2018 - self.year >= 50:
            return True
        else:
            return False

    def vintage(self):
        if 2018 - self.year >= 50:
            return "Vintage"
        else:
            return "Non Vintage"

    def __repr__(self):
        return("{} ({}) - worth ${:.2f} - ({})".format(self.name, self.year, self.cost, self.vintage()))
