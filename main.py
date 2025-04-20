import tkinter as tk
from tkinter import messagebox
import sqlite3

# Set up database
conn = sqlite3.connect('hospital.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    doctor TEXT
)
''')
conn.commit()

# GUI
def submit():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    doctor = doctor_var.get()

    if name and age and gender and doctor:
        c.execute("INSERT INTO appointments (name, age, gender, doctor) VALUES (?, ?, ?, ?)", 
                  (name, age, gender, doctor))
        conn.commit()
        messagebox.showinfo("Success", "Appointment booked successfully!")
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

app = tk.Tk()
app.title("Hospital Management System")

tk.Label(app, text="Patient Name").grid(row=0, column=0)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1)

tk.Label(app, text="Age").grid(row=1, column=0)
age_entry = tk.Entry(app)
age_entry.grid(row=1, column=1)

tk.Label(app, text="Gender").grid(row=2, column=0)
gender_var = tk.StringVar()
tk.OptionMenu(app, gender_var, "Male", "Female", "Other").grid(row=2, column=1)

tk.Label(app, text="Doctor").grid(row=3, column=0)
doctor_var = tk.StringVar()
tk.OptionMenu(app, doctor_var, "Dr. Smith", "Dr. John", "Dr. Priya").grid(row=3, column=1)

tk.Button(app, text="Book Appointment", command=submit).grid(row=4, column=0, columnspan=2, pady=10)

app.mainloop()
