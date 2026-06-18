from openpyxl import Workbook
from tkinter import messagebox

from database import get_attendance


def export_attendance():

    rows = get_attendance()

    if not rows:

        messagebox.showwarning(
            "No Data",
            "No attendance records found."
        )
        return

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "Attendance Report"

    headers = [
        "Attendance ID",
        "Roll Number",
        "Student Name",
        "Date",
        "Status"
    ]

    sheet.append(headers)

    for row in rows:

        sheet.append(row)

    workbook.save(
        "Attendance_Report.xlsx"
    )

    messagebox.showinfo(
        "Success",
        "Attendance_Report.xlsx exported successfully."
    )