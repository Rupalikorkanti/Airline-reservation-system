✈️ Airline Reservation System
A complete airline reservation system built with Python Tkinter and MySQL database. This project demonstrates database management, GUI development, and system integration.
📋 Project Overview
This airline reservation system allows users to:
•	View available flights
•	Check seat availability
•	Make seat reservations
•	Manage customer information
•	Track booking status
🛠️ Technology Stack
•	Frontend: Python Tkinter GUI
•	Backend: MySQL Database
•	Language: Python 3.x
•	Database Connector: mysql-connector-python
📁 Project Structure
airline-reservation-system/
├── airline_gui.py          # Main GUI application
├── airline_database.sql    # Database schema and sample data
└── README.md              # Project documentation
Step 1: Install Dependencies
bash
pip install mysql-connector-python
pip install tkinter 
Step 2: Database Setup
1.	Start your MySQL server
2.	Open MySQL command line or workbench
3.	Execute the SQL script:
bash
mysql -u root -p < airline_database.sql
Step 3: Configure Database Connection
1.	Open airline_gui.py
2.	Update the database connection parameters:
python
conn = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="rupalikor@123,  # 👈 Replace with your MySQL password
    database="AirlineDB"
)
Step 4: Run the Application
bash
python airline_gui.py
📊 Database Schema
Tables
1.	Flights - Flight information (airline, routes, times)
2.	Customers - Customer personal details
3.	Seats - Seat configuration and availability
4.	Bookings - Reservation records
Features
•	Foreign key constraints for data integrity
•	Triggers for automatic seat status updates
•	Views for complex queries
•	Sample data for testing
🖥️ Application Features
Flight Management
•	Display all available flights
•	Filter by origin/destination
•	Real-time seat availability
Booking System
•	Select flights and seats
•	Customer registration
•	Booking confirmation
•	Error handling and validation
User Interface
•	Intuitive Tkinter GUI
•	Tree view for data display
•	Form inputs for booking
•	Message boxes for user feedback
💡 Usage Guide
1.	View Flights: The main window shows all available flights
2.	Select Flight: Click on a flight to select it
3.	Check Seats: Click "Show Available Seats" to see open seats
4.	Make Booking: 
o	Select an available seat
o	Fill in customer details (Name, Email, Phone)
o	Click "Book Seat" to confirm
🔧 Customization Options
Adding More Flights
sql
INSERT INTO Flights (Airline, Origin, Destination, DepartureTime, ArrivalTime, TotalSeats)
VALUES ('Your Airline', 'Origin', 'Destination', '2025-07-15 09:00:00', '2025-07-15 11:00:00', 180);
Adding More Seats
sql
INSERT INTO Seats (FlightID, SeatNumber, IsBooked)
VALUES (1, 'C1', 0), (1, 'C2', 0), (1, 'C3', 0);
🐛 Troubleshooting
Common Issues
Database Connection Error
•	Verify MySQL server is running
•	Check username/password in code
•	Ensure database "AirlineDB" exists
Import Error (tkinter)
•	On Ubuntu/Debian: sudo apt-get install python3-tk
•	On Windows: Reinstall Python with tkinter option
Permission Denied
•	Check MySQL user privileges
•	Grant necessary permissions to your user
📈 Future Enhancements
•	Payment integration
•	Email booking confirmations
•	Flight search filters
•	Admin panel for flight management
•	Web-based interface
•	Reporting and analytics
👨‍💻 Author
Rupali korkanti
