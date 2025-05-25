from user import User
from dashboard import Dashboard

if __name__ == "__main__":
    user1 = User("Aimal123", "aimal@email.com")
    app_dashboard = Dashboard(user1)

    app_dashboard.welcome()
    app_dashboard.show_guide()
    app_dashboard.setup_travel_plan("Pakistan", "2025-06-01", "2025-07-10")
    
    print("\nUser decides to upgrade...")
    app_dashboard.simulate_payment()

    app_dashboard.welcome()
