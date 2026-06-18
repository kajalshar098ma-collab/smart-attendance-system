import customtkinter as ctk
from tkinter import messagebox

from database import (
    add_student,
    get_students,
    search_students
)


class StudentPage(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.title("Student Management")
        self.geometry("900x650")

        self.build_ui()

        self.load_students()

    def build_ui(self):

        ctk.CTkLabel(
            self,
            text="Student Management",
            font=("Arial", 24, "bold")
        ).pack(pady=10)

        self.roll = ctk.CTkEntry(
            self,
            placeholder_text="Roll Number"
        )
        self.roll.pack(pady=5)

        self.name = ctk.CTkEntry(
            self,
            placeholder_text="Student Name"
        )
        self.name.pack(pady=5)

        self.class_name = ctk.CTkEntry(
            self,
            placeholder_text="Class"
        )
        self.class_name.pack(pady=5)

        self.email = ctk.CTkEntry(
            self,
            placeholder_text="Email"
        )
        self.email.pack(pady=5)

        ctk.CTkButton(
            self,
            text="Add Student",
            command=self.add_student_ui
        ).pack(pady=10)

        self.search_box = ctk.CTkEntry(
            self,
            placeholder_text="Search Student"
        )

        self.search_box.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkButton(
            self,
            text="Search",
            command=self.search_student
        ).pack(pady=5)

        ctk.CTkButton(
            self,
            text="Show All Students",
            command=self.load_students
        ).pack(pady=5)

        self.student_box = ctk.CTkTextbox(
            self,
            width=850,
            height=350
        )

        self.student_box.pack(
            pady=10,
            padx=10
        )

    def add_student_ui(self):

        try:

            success = add_student(
                self.roll.get().strip(),
                self.name.get().strip(),
                self.class_name.get().strip(),
                self.email.get().strip()
            )

            if success is False:

                messagebox.showerror(
                    "Error",
                    "Roll Number already exists."
                )

                return

            messagebox.showinfo(
                "Success",
                "Student Added Successfully"
            )

            self.roll.delete(0, "end")
            self.name.delete(0, "end")
            self.class_name.delete(0, "end")
            self.email.delete(0, "end")

            self.load_students()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def load_students(self):

        self.student_box.delete(
            "1.0",
            "end"
        )

        students = get_students()

        for student in students:

            self.student_box.insert(
                "end",
                f"""
ID: {student[0]}
Roll: {student[1]}
Name: {student[2]}
Class: {student[3]}
Email: {student[4]}
--------------------------------------
"""
            )

    def search_student(self):

        keyword = self.search_box.get().strip()

        self.student_box.delete(
            "1.0",
            "end"
        )

        students = search_students(keyword)

        for student in students:

            self.student_box.insert(
                "end",
                f"""
ID: {student[0]}
Roll: {student[1]}
Name: {student[2]}
Class: {student[3]}
Email: {student[4]}
--------------------------------------
"""
            )