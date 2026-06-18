import customtkinter as ctk
from datetime import datetime
from tkinter import messagebox

from database import (
    get_students,
    save_attendance,
    attendance_exists
)


class AttendancePage(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.title("Attendance Management")
        self.geometry("800x650")

        self.vars = []

        ctk.CTkLabel(
            self,
            text="Mark Attendance",
            font=("Arial", 26, "bold")
        ).pack(pady=20)

        students = get_students()

        if not students:

            ctk.CTkLabel(
                self,
                text="No students available.\nPlease add students first.",
                font=("Arial", 18)
            ).pack(pady=30)

            return

        scroll_frame = ctk.CTkScrollableFrame(
            self,
            width=700,
            height=450
        )

        scroll_frame.pack(
            pady=10,
            padx=20,
            fill="both",
            expand=True
        )

        for student in students:

            student_id = student[0]
            roll = student[1]
            name = student[2]

            var = ctk.BooleanVar()

            checkbox = ctk.CTkCheckBox(
                scroll_frame,
                text=f"{roll} - {name}",
                variable=var
            )

            checkbox.pack(
                anchor="w",
                padx=10,
                pady=5
            )

            self.vars.append(
                (
                    student_id,
                    var
                )
            )

        ctk.CTkButton(
            self,
            text="Save Attendance",
            width=250,
            height=40,
            command=self.save_attendance_data
        ).pack(pady=20)

    def save_attendance_data(self):

        today = datetime.now().strftime("%Y-%m-%d")

        try:

            saved_count = 0

            for student_id, var in self.vars:

                status = (
                    "Present"
                    if var.get()
                    else "Absent"
                )

                if not attendance_exists(
                    student_id,
                    today
                ):

                    save_attendance(
                        student_id,
                        today,
                        status
                    )

                    saved_count += 1

            if saved_count > 0:

                messagebox.showinfo(
                    "Success",
                    f"{saved_count} attendance records saved successfully."
                )

            else:

                messagebox.showwarning(
                    "Already Marked",
                    "Attendance for today already exists."
                )

            self.destroy()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )