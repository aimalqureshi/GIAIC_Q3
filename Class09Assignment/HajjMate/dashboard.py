from guide import HajjGuide
from travel import TravelPlan
from payment import Payment
from user import User

class Dashboard:
    def __init__(self, user: User):
        self.user = user
        self.guide = HajjGuide()
        self.plan = None

    def welcome(self):
        print(f"\n🕌 Welcome to HajjMate, {self.user.username}!")
        if self.user.is_premium:
            print("✅ Premium Access: Full guide and planning features available.")
        else:
            print("🔒 Limited Access: Upgrade to Premium for full experience.")

    def setup_travel_plan(self, country, dep_date, ret_date):
        self.plan = TravelPlan(country, dep_date, ret_date)
        cost = self.plan.estimate_cost()
        print(f"\n🌍 Travel Plan from {country}")
        print(f"Estimated Hajj Cost: ${cost}")

    def show_guide(self):
        self.guide.show_rituals()

    def simulate_payment(self):
        payment = Payment(self.user, 10)
        print(payment.process_payment())
