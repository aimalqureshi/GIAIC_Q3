# File: hajjmate_app.py

import datetime

# --------------------------
# User Authentication Class
# --------------------------
class User:
    def __init__(self, username, email, is_premium=False):
        self.username = username
        self.email = email
        self.is_premium = is_premium
        self.created_at = datetime.datetime.now()

    def upgrade_account(self):
        self.is_premium = True
        print(f"{self.username} upgraded to premium!")

# ------------------------
# Hajj Ritual Guide Class
# ------------------------
class HajjGuide:
    def __init__(self):
        self.rituals = [
            "Ihram - Intention and Clothing",
            "Tawaf - Circling the Kaaba",
            "Sa’i - Walking between Safa and Marwa",
            "Mina - Day of Tarwiyah",
            "Arafah - Day of Arafat",
            "Muzdalifah - Night Stay",
            "Ramy - Stoning the Devil",
            "Qurbani - Animal Sacrifice",
            "Tawaf al-Ifadah - Final Tawaf",
        ]

    def show_rituals(self):
        print("\n🌙 Hajj Rituals Guide:")
        for step, ritual in enumerate(self.rituals, 1):
            print(f"{step}. {ritual}")

# ------------------------
# Travel Planning Class
# ------------------------
class TravelPlan:
    def __init__(self, country, departure_date, return_date):
        self.country = country
        self.departure_date = departure_date
        self.return_date = return_date
        self.estimated_cost = 0

    def estimate_cost(self):
        base_cost = 3000
        country_multiplier = 1.2 if self.country == "USA" else 1.0
        self.estimated_cost = base_cost * country_multiplier
        return self.estimated_cost

# --------------------------
# Payment Simulation Class
# --------------------------
class Payment:
    def __init__(self, user: User, amount):
        self.user = user
        self.amount = amount
        self.status = "Pending"

    def process_payment(self):
        # Simulate success
        self.status = "Success"
        self.user.upgrade_account()
        return f"Payment of ${self.amount} for {self.user.username} was successful!"

# ----------------------------
# Application Dashboard Logic
# ----------------------------
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

# ---------------------
# Simulated Main Flow
# ---------------------
if __name__ == "__main__":
    user1 = User("Ahmed123", "ahmed@email.com")
    app_dashboard = Dashboard(user1)

    app_dashboard.welcome()
    app_dashboard.show_guide()
    app_dashboard.setup_travel_plan("Pakistan", "2025-06-01", "2025-07-10")
    
    print("\nUser decides to upgrade...")
    app_dashboard.simulate_payment()

    app_dashboard.welcome()
