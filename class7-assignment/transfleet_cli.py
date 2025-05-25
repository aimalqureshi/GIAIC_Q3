# transfleet_cli.py

from datetime import datetime

class Driver:
    def __init__(self, driver_id, name, license_number):
        self.driver_id = driver_id
        self.name = name
        self.license_number = license_number
        self.assigned_vehicle = None

    def assign_vehicle(self, vehicle):
        self.assigned_vehicle = vehicle

    def __str__(self):
        return f"{self.name} (License: {self.license_number})"


class Trip:
    def __init__(self, origin, destination, distance, fuel_used, driver):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.fuel_used = fuel_used
        self.driver = driver
        self.date = datetime.now().strftime('%Y-%m-%d')

    def cost_estimate(self, fuel_price_per_litre):
        return self.fuel_used * fuel_price_per_litre


class Vehicle:
    def __init__(self, vehicle_id, model, fuel_capacity):
        self.vehicle_id = vehicle_id
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.trips = []
        self.maintenance_logs = []

    def add_trip(self, trip):
        self.trips.append(trip)

    def log_maintenance(self, description, date):
        self.maintenance_logs.append({"description": description, "date": date})

    def total_distance(self):
        return sum(t.distance for t in self.trips)

    def fuel_efficiency(self):
        total_fuel = sum(t.fuel_used for t in self.trips)
        return self.total_distance() / total_fuel if total_fuel else 0

    def __str__(self):
        return f"{self.model} (ID: {self.vehicle_id})"


class FleetManager:
    def __init__(self):
        self.vehicles = {}
        self.drivers = {}

    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.vehicle_id] = vehicle

    def add_driver(self, driver):
        self.drivers[driver.driver_id] = driver

    def assign_driver_to_vehicle(self, driver_id, vehicle_id):
        driver = self.drivers.get(driver_id)
        vehicle = self.vehicles.get(vehicle_id)
        if driver and vehicle:
            driver.assign_vehicle(vehicle)
            print(f"Assigned {driver.name} to {vehicle.model}")
        else:
            print("Invalid driver or vehicle ID")

    def log_trip(self, vehicle_id, trip):
        vehicle = self.vehicles.get(vehicle_id)
        if vehicle:
            vehicle.add_trip(trip)
            print("Trip logged successfully.")
        else:
            print("Vehicle not found.")

    def log_maintenance(self, vehicle_id, description, date):
        vehicle = self.vehicles.get(vehicle_id)
        if vehicle:
            vehicle.log_maintenance(description, date)
            print("Maintenance log updated.")
        else:
            print("Vehicle not found.")

    def vehicle_report(self, vehicle_id):
        v = self.vehicles.get(vehicle_id)
        if not v:
            print("Vehicle not found.")
            return

        print(f"\n--- Report for {v.model} ---")
        print(f"Total Distance: {v.total_distance()} km")
        print(f"Fuel Efficiency: {v.fuel_efficiency():.2f} km/l")
        print("Maintenance Records:")
        for log in v.maintenance_logs:
            print(f"- {log['date']}: {log['description']}")

    def fleet_summary(self):
        print("\n--- Fleet Summary ---")
        for v in self.vehicles.values():
            print(f"{v} | Distance: {v.total_distance()} km | Efficiency: {v.fuel_efficiency():.2f} km/l")


def main():
    manager = FleetManager()

    while True:
        print("\n===== TransFleet CLI Menu =====")
        print("1. Add Vehicle")
        print("2. Add Driver")
        print("3. Assign Driver to Vehicle")
        print("4. Log Trip")
        print("5. Log Maintenance")
        print("6. View Vehicle Report")
        print("7. View Fleet Summary")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            vid = input("Vehicle ID: ")
            model = input("Model: ")
            fuel_cap = float(input("Fuel Capacity (litres): "))
            manager.add_vehicle(Vehicle(vid, model, fuel_cap))

        elif choice == "2":
            did = input("Driver ID: ")
            name = input("Name: ")
            license_no = input("License Number: ")
            manager.add_driver(Driver(did, name, license_no))

        elif choice == "3":
            did = input("Driver ID: ")
            vid = input("Vehicle ID: ")
            manager.assign_driver_to_vehicle(did, vid)

        elif choice == "4":
            vid = input("Vehicle ID: ")
            origin = input("From: ")
            dest = input("To: ")
            dist = float(input("Distance (km): "))
            fuel = float(input("Fuel used (litres): "))
            did = input("Driver ID: ")
            trip = Trip(origin, dest, dist, fuel, manager.drivers.get(did))
            manager.log_trip(vid, trip)

        elif choice == "5":
            vid = input("Vehicle ID: ")
            desc = input("Maintenance Description: ")
            date = input("Date (YYYY-MM-DD): ")
            manager.log_maintenance(vid, desc, date)

        elif choice == "6":
            vid = input("Vehicle ID: ")
            manager.vehicle_report(vid)

        elif choice == "7":
            manager.fleet_summary()

        elif choice == "8":
            print("Exiting TransFleet CLI.")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
