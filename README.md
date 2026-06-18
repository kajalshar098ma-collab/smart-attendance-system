# 📊 Smart Attendance System

A modern desktop-based Attendance Management System built using **Python**, **CustomTkinter**, and **SQLite**.

It helps manage students, mark daily attendance, generate reports, visualize data, and export records to Excel with a clean and user-friendly interface.

---

## ✨ Features

- 👨‍🎓 Student Management (Add / View / Search / Update)
- 📝 Daily Attendance Marking (Present / Absent)
- 📊 Attendance Reports by Date / Student
- 📈 Pie Chart Visualization of Attendance
- 📁 Export Attendance Data to Excel (.xlsx)
- 💾 SQLite Database Integration
- 🖥️ Modern UI using CustomTkinter
- ⚡ Fast, lightweight, and offline-friendly

---

## 🧱 Project Structure

```
smart-attendance-system/
│
├── dashboard.py          # Main dashboard UI
├── students.py           # Student management module
├── attendance.py         # Attendance marking system
├── reports.py            # Reports generation module
├── charts.py             # Pie chart visualization
├── export_excel.py       # Export data to Excel
├── database.py           # SQLite database operations
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## 🖼️ Screenshots

### 📌 Dashboard UI
![Dashboard](screenshots/dashboard.png)


---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-attendance-system.git
cd smart-attendance-system
```

---

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available yet, install manually:

```bash
pip install customtkinter pandas openpyxl matplotlib
```

---

## 🚀 How to Run

```bash
python dashboard.py
```

---

## 📊 Modules Overview

### 👨‍🎓 Student Management
Add, update, delete, and search student records.

### 📝 Attendance System
Mark students as Present or Absent daily.

### 📈 Reports
Generate attendance reports based on student or date filters.

### 📊 Charts
Visualize attendance statistics using pie charts.

### 📁 Export
Export attendance data into Excel for external use.

---

## 💡 Future Improvements

- 🔐 Login system with authentication
- ☁️ Cloud database integration
- 📱 Mobile-friendly version
- 📅 Monthly attendance calendar view
- 🔔 Email/SMS attendance alerts

---

## 🤝 Contributing

```
1. Fork the repository
2. Create a new branch (feature-name)
3. Commit your changes
4. Push to branch
5. Create a Pull Request
```

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## ⭐ Support

If you like this project, don’t forget to give it a ⭐ on GitHub!
