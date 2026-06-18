📊 Smart Attendance System

A desktop-based Attendance Management System built using Python, CustomTkinter, and SQLite.
It helps manage students, mark attendance, generate reports, and export data in Excel format with a simple and modern UI.

✨ Features
👨‍🎓 Student Management (Add / View / Search)
📝 Daily Attendance Marking (Present / Absent)
📊 Attendance Reports
📈 Pie Chart Visualization (Present vs Absent)
📁 Export Attendance to Excel
💾 SQLite Database Integration
🖥️ Modern UI using CustomTkinter
🛠️ Tech Stack
Python 3
CustomTkinter (GUI)
SQLite3 (Database)
OpenPyXL (Excel Export)
Matplotlib (Charts)
📂 Project Structure
SmartAttendance/
│
├── dashboard.py          # Main dashboard UI
├── students.py           # Student management window
├── attendance.py         # Attendance marking system
├── reports.py            # Reports section
├── charts.py             # Pie chart visualization
├── export_excel.py       # Excel export functionality
├── database.py           # All database operations
│
└── attendance.db         # Auto-generated database file
🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/kajalshar098ma-collab/smart-attendance-system.git
cd smart-attendance-system
2️⃣ Install Dependencies
pip install customtkinter openpyxl matplotlib
3️⃣ Run the Application
python dashboard.py
🧠 How It Works
Add students into the system
Open “Mark Attendance” page
Select Present/Absent
Save attendance to database
View reports and charts
Export data to Excel file
📊 Output Features

✔ Attendance stored in SQLite database
✔ Excel report generated automatically
✔ Pie chart shows attendance distribution
✔ Search & filter student records

📁 Excel Export

Generates file:

Attendance_Report.xlsx

Includes:

Student details
Attendance records
Summary (Present / Absent count)
⚠️ Important Notes
attendance.db is auto-created when the project runs
Do NOT upload database file to GitHub
This is a desktop application (not web-based)
📸 Screenshots

/screenshots/dashboard.png
🚀 Future Improvements
🔐 Login system (Admin / Student)
☁️ Cloud database support
✏️ Edit attendance records
📱 Mobile version
🌐 Web version (Streamlit / Flask)
👨‍💻 Author

Developed as a Python learning + mini project for attendance automation and GUI development practice.

📜 License

This project is open-source and free to use for educational purposes.

