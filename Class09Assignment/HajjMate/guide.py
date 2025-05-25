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
