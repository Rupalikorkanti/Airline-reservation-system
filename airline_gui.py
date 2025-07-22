import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rupalikor@123",  # 👈 Replace with your password
    database="AirlineDB"
)
cursor = conn.cursor()

# GUI Window
root = tk.Tk()
root.title("Airline Reservation System")
root.geometry("900x600")

# Frames
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

middle_frame = tk.Frame(root)
middle_frame.pack(pady=10)

bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

# --- Flights Table ---
tk.Label(top_frame, text="Available Flights", font=('Arial', 14)).pack()

flight_tree = ttk.Treeview(top_frame, columns=("ID", "Airline", "Origin", "Destination"), show='headings', height=5)
flight_tree.pack()

for col in ["ID", "Airline", "Origin", "Destination"]:
    flight_tree.heading(col, text=col)

cursor.execute("SELECT FlightID, Airline, Origin, Destination FROM Flights")
for row in cursor.fetchall():
    flight_tree.insert('', 'end', values=row)

# --- Seats Table ---
def get_available_seats():
    selected = flight_tree.focus()
    if not selected:
        messagebox.showwarning("Select Flight", "Please select a flight first.")
        return

    flight_id = flight_tree.item(selected)['values'][0]

    cursor.execute("SELECT SeatID, SeatNumber FROM Seats WHERE FlightID = %s AND IsBooked = 0", (flight_id,))
    rows = cursor.fetchall()

    for i in seat_tree.get_children():
        seat_tree.delete(i)
    for row in rows:
        seat_tree.insert('', 'end', values=row)

tk.Button(middle_frame, text="Show Available Seats", command=get_available_seats).pack()

tk.Label(middle_frame, text="Available Seats", font=('Arial', 14)).pack()
seat_tree = ttk.Treeview(middle_frame, columns=("SeatID", "SeatNumber"), show='headings', height=5)
seat_tree.pack()

for col in ["SeatID", "SeatNumber"]:
    seat_tree.heading(col, text=col)

# --- Booking Inputs ---
form_frame = tk.Frame(bottom_frame)
form_frame.pack()

tk.Label(form_frame, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Email:").grid(row=1, column=0)
email_entry = tk.Entry(form_frame)
email_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Phone:").grid(row=2, column=0)
phone_entry = tk.Entry(form_frame)
phone_entry.grid(row=2, column=1)

# --- Book Seat Function ---
def book_seat():
    seat_selected = seat_tree.focus()
    if not seat_selected:
        messagebox.showwarning("No Seat", "Please select a seat.")
        return

    seat_id = seat_tree.item(seat_selected)['values'][0]
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if not all([name, email, phone]):
        messagebox.showwarning("Incomplete Info", "Please fill all fields.")
        return

    try:
        cursor.execute("""
            INSERT INTO Customers (FullName, Email, Phone)
            VALUES (%s, %s, %s)
        """, (name, email, phone))
        customer_id = cursor.lastrowid

        cursor.execute("""
            UPDATE Seats SET IsBooked = 1 WHERE SeatID = %s
        """, (seat_id,))

        conn.commit()
        messagebox.showinfo("Success", "Seat booked successfully!")
        get_available_seats()
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", str(e))

tk.Button(bottom_frame, text="Book Seat", command=book_seat, bg="green", fg="white").pack(pady=10)

root.mainloop()
