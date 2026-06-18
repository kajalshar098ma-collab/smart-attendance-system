📌 Smart Attendance System

A Python-based desktop application built using CustomTkinter and SQLite for managing student records, marking attendance, generating reports, exporting Excel files, and visualizing attendance data.

🚀 Features
👨‍🎓 Add, search, and manage students
📝 Mark daily attendance (Present/Absent)
📊 View attendance reports
📈 Visual pie chart for attendance summary
📁 Export attendance data to Excel
💾 Local SQLite database storage
🖥️ Modern UI using CustomTkinter
🛠️ Tech Stack
Python 3
CustomTkinter
SQLite3
OpenPyXL
Matplotlib (for charts)
📂 Project Structure
SmartAttendance/
│
├── dashboard.py          # Main dashboard UI
├── students.py           # Student management UI
├── attendance.py         # Attendance marking UI
├── reports.py            # Reports section
├── charts.py             # Attendance pie chart
├── export_excel.py       # Excel export feature
├── database.py           # Database operations
│
└── attendance.db         # Auto-generated database (NOT uploaded)
⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/smart-attendance-system.git
cd smart-attendance-system
2. Install dependencies
pip install customtkinter openpyxl matplotlib
▶️ Run the Application

Run the dashboard:

python dashboard.py
🧠 How It Works
Add students in the system
Open Attendance page
Mark Present/Absent
Save attendance to database
View reports & charts
Export data to Excel file
📊 Output Features
Attendance stored in SQLite database
Excel report generated automatically
Pie chart showing Present vs Absent ratio
📁 Export Feature

Generates file:

Attendance_Report.xlsx

Includes:

Attendance records  
Student data
Summary sheet
⚠️ Important Notes
attendance.db is auto-created when project runs
Do NOT upload database file to GitHub
This is a desktop application (not web-based)
📸 Screenshots 

/screenshots/dashboard.png

📌 Future Improvements
Login system (Admin/Student)
Edit attendance feature
Cloud database support
Web version (Flask / Streamlit)
Mobile app version
👨‍💻 Author
Developed using Python
Custom attendance management system for learning and project purposes
📜 License

This project is open-source and free to use for educational purposes.
