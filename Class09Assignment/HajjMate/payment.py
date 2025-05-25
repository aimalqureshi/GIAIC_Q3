from user import User

class Payment:
    def __init__(self, user: User, amount):
        self.user = user
        self.amount = amount
        self.status = "Pending"

    def process_payment(self):
        self.status = "Success"
        self.user.upgrade_account()
        return f"Payment of ${self.amount} for {self.user.username} was successful!"
