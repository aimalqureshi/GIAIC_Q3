from guide import HajjGuide
from travel import TravelPlan
from payment import Payment
from user import User

class DashboardGUI:
    def __init__(self):
        self.user = None
        self.guide = HajjGuide()
        self.plan = None

    def register_user(self, name, email):
        self.user = User(name, email)

    def get_rituals(self):
        return self.guide.get_rituals()

    def setup_travel_plan(self, country, dep_date, ret_date):
        self.plan = TravelPlan(country, dep_date, ret_date)
        return self.plan.estimate_cost()

    def process_payment(self):
        payment = Payment(self.user, 10)
        return payment.process_payment()
