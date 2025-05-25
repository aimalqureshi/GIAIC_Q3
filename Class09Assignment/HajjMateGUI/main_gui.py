import tkinter as tk
from tkinter import messagebox, PhotoImage
from dashboard_gui import DashboardGUI

app = tk.Tk()
app.title("HajjMate - Your Hajj Companion")
app.geometry("600x700")
app.configure(bg="#f7f7f7")

dashboard = DashboardGUI()

# Load Logo
try:
    logo = PhotoImage(file="logo.png")
    logo_label = tk.Label(app, image=logo, bg="#f7f7f7")
    logo_label.pack(pady=10)
except Exception as e:
    print("Logo not loaded:", e)

# User Info
tk.Label(app, text="Name:", bg="#f7f7f7").pack()
name_entry = tk.Entry(app)
name_entry.pack()

tk.Label(app, text="Email:", bg="#f7f7f7").pack()
email_entry = tk.Entry(app)
email_entry.pack()

def register():
    name = name_entry.get()
    email = email_entry.get()
    dashboard.register_user(name, email)
    messagebox.showinfo("Registered", f"Welcome {name}!")

tk.Button(app, text="Register", command=register).pack(pady=5)

# Rituals Display
def show_rituals():
    rituals = dashboard.get_rituals()
    messagebox.showinfo("Hajj Rituals", "\n".join(rituals))

tk.Button(app, text="Show Hajj Guide", command=show_rituals).pack(pady=5)

# Travel Planning
tk.Label(app, text="Country:", bg="#f7f7f7").pack()
country_entry = tk.Entry(app)
country_entry.pack()

tk.Label(app, text="Departure Date:", bg="#f7f7f7").pack()
dep_entry = tk.Entry(app)
dep_entry.pack()

tk.Label(app, text="Return Date:", bg="#f7f7f7").pack()
ret_entry = tk.Entry(app)
ret_entry.pack()

def plan_trip():
    cost = dashboard.setup_travel_plan(
        country_entry.get(), dep_entry.get(), ret_entry.get()
    )
    messagebox.showinfo("Estimated Cost", f"Your Hajj trip will cost approximately ${cost}")

tk.Button(app, text="Plan My Hajj Trip", command=plan_trip).pack(pady=5)

# Premium Upgrade
def upgrade():
    result = dashboard.process_payment()
    messagebox.showinfo("Upgrade Status", result)

tk.Button(app, text="Upgrade to Premium ($10)", bg="gold", command=upgrade).pack(pady=10)

# Start GUI Loop
app.mainloop()
