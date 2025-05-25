import datetime

class User:
    def __init__(self, username, email, is_premium=False):
        self.username = username
        self.email = email
        self.is_premium = is_premium
        self.created_at = datetime.datetime.now()

    def upgrade_account(self):
        self.is_premium = True
        print(f"{self.username} upgraded to premium!")
