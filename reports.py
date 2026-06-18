import customtkinter as ctk

from database import (
    get_students,
    attendance_by_date,
    get_attendance_percentage
)


class ReportPage(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.title("Attendance Reports")
        self.geometry("1000x700")

        ctk.CTkLabel(
            self,
            text="Attendance Reports",
            font=("Arial", 26, "bold")
        ).pack(pady=10)

        self.date_entry = ctk.CTkEntry(
            self,
            placeholder_text="YYYY-MM-DD"
        )

        self.date_entry.pack(pady=10)

        ctk.CTkButton(
            self,
            text="Search Date",
            command=self.search_date
        ).pack(pady=5)

        ctk.CTkButton(
            self,
            text="Show Attendance Summary",
            command=self.load_percentages
        ).pack(pady=5)

        self.report_box = ctk.CTkTextbox(
            self,
            width=900,
            height=500
        )

        self.report_box.pack(
            pady=20,
            padx=20
        )

        self.load_percentages()

    def load_percentages(self):

        self.report_box.delete(
            "1.0",
            "end"
        )

        students = get_students()

        for student in students:

            percentage = get_attendance_percentage(
                student[0]
            )

            self.report_box.insert(
                "end",
                f"""
Roll Number : {student[1]}
Student Name: {student[2]}
Attendance  : {percentage:.2f} %

------------------------------------------
"""
            )

    def search_date(self):

        self.report_box.delete(
            "1.0",
            "end"
        )

        date = self.date_entry.get().strip()

        rows = attendance_by_date(date)

        if not rows:

            self.report_box.insert(
                "end",
                "No records found.\n"
            )

            return

        for row in rows:

            self.report_box.insert(
                "end",
                f"""
Roll Number : {row[1]}
Student Name: {row[2]}
Date        : {row[3]}
Status      : {row[4]}

------------------------------------------
"""
            )