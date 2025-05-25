class TravelPlan:
    def __init__(self, country, departure_date, return_date):
        self.country = country
        self.departure_date = departure_date
        self.return_date = return_date
        self.estimated_cost = 0

    def estimate_cost(self):
        base_cost = 3000
        country_multiplier = 1.2 if self.country.lower() == "usa" else 1.0
        self.estimated_cost = base_cost * country_multiplier
        return self.estimated_cost
