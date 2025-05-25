# ClosetCraft.py

class ClothingItem:
    def __init__(self, name, category, color, material, times_worn=0):
        self.name = name
        self.category = category
        self.color = color
        self.material = material
        self.times_worn = times_worn

    def wear(self):
        self.times_worn += 1

    def __str__(self):
        return f"{self.name} ({self.color} {self.category}, worn {self.times_worn}x)"


class Outfit:
    def __init__(self, name, items, occasion="Casual"):
        self.name = name
        self.items = items
        self.occasion = occasion

    def total_wears(self):
        return sum(item.times_worn for item in self.items)

    def __str__(self):
        items_str = ", ".join(item.name for item in self.items)
        return f"{self.name} (Occasion: {self.occasion}) - Includes: {items_str}"


class UserWardrobe:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.clothing_items = []
        self.outfits = []

    def add_item(self, item):
        self.clothing_items.append(item)

    def wear_item(self, item_name):
        for item in self.clothing_items:
            if item.name.lower() == item_name.lower():
                item.wear()
                return f"You wore {item.name}. Total wears: {item.times_worn}"
        return "Item not found."

    def create_outfit(self, name, item_names, occasion):
        items = [item for item in self.clothing_items if item.name in item_names]
        if not items:
            return "No matching items found."
        outfit = Outfit(name, items, occasion)
        self.outfits.append(outfit)
        return f"Outfit '{name}' created successfully."

    def wardrobe_summary(self):
        if not self.clothing_items:
            print("No items in wardrobe.")
        for item in self.clothing_items:
            print(item)

    def outfit_summary(self):
        if not self.outfits:
            print("No outfits created.")
        for outfit in self.outfits:
            print(outfit)
def main():
    print("Welcome to ClosetCraft 👚")
    name = input("Enter your name to create your wardrobe: ")
    user = UserWardrobe(name)

    while True:
        print("\n📋 Menu")
        print("1. Add Clothing Item")
        print("2. Wear a Clothing Item")
        print("3. Create an Outfit")
        print("4. View Wardrobe Summary")
        print("5. View Outfit Summary")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            item_name = input("Item Name: ")
            category = input("Category (e.g., shirt, pants): ")
            color = input("Color: ")
            material = input("Material: ")
            item = ClothingItem(item_name, category, color, material)
            user.add_item(item)
            print(f"{item_name} added to wardrobe.")

        elif choice == "2":
            item_name = input("Enter the name of the item you wore: ")
            print(user.wear_item(item_name))

        elif choice == "3":
            outfit_name = input("Outfit Name: ")
            occasion = input("Occasion (e.g., Casual, Formal): ")
            item_names = input("Item names (comma separated): ").split(",")
            item_names = [name.strip() for name in item_names]
            print(user.create_outfit(outfit_name, item_names, occasion))

        elif choice == "4":
            print("\n🧺 Wardrobe Summary")
            user.wardrobe_summary()

        elif choice == "5":
            print("\n👗 Outfit Summary")
            user.outfit_summary()

        elif choice == "6":
            print("Goodbye! Stay stylish 🌟")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
