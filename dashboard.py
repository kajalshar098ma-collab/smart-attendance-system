import customtkinter as ctk
from tkinter import messagebox

from students import StudentPage
from attendance import AttendancePage
from reports import ReportPage

from charts import show_pie_chart
from export_excel import export_attendance

from database import total_students


class Dashboard(ctk.CTk):

    def __init__(self, username):

        super().__init__()

        self.username = username

        self.title("Smart Attendance System")
        self.geometry("1200x700")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.build_ui()

    def build_ui(self):

        # ==========================
        # HEADER
        # ==========================

        header = ctk.CTkFrame(self)
        header.pack(fill="x", padx=10, pady=10)

        title = ctk.CTkLabel(
            header,
            text="Smart Attendance Dashboard",
            font=("Arial", 28, "bold")
        )
        title.pack(side="left", padx=20, pady=15)

        welcome = ctk.CTkLabel(
            header,
            text=f"Welcome, {self.username}",
            font=("Arial", 16)
        )
        welcome.pack(side="left", padx=20)

        logout_btn = ctk.CTkButton(
            header,
            text="Logout",
            width=120,
            command=self.logout
        )
        logout_btn.pack(side="right", padx=20)

        # ==========================
        # DASHBOARD CARDS
        # ==========================

        card_frame = ctk.CTkFrame(self)
        card_frame.pack(fill="x", padx=20, pady=20)

        self.total_students_card = ctk.CTkLabel(
            card_frame,
            text="",
            width=250,
            height=120,
            corner_radius=15,
            font=("Arial", 22, "bold")
        )
        self.total_students_card.pack(
            side="left",
            padx=20,
            pady=20
        )

        self.refresh_cards()

        # ==========================
        # BUTTON FRAME
        # ==========================

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkButton(
            button_frame,
            text="Manage Students",
            width=220,
            height=50,
            command=self.open_students
        ).grid(row=0, column=0, padx=20, pady=20)

        ctk.CTkButton(
            button_frame,
            text="Mark Attendance",
            width=220,
            height=50,
            command=self.open_attendance
        ).grid(row=0, column=1, padx=20, pady=20)

        ctk.CTkButton(
            button_frame,
            text="Reports",
            width=220,
            height=50,
            command=self.open_reports
        ).grid(row=0, column=2, padx=20, pady=20)

        ctk.CTkButton(
            button_frame,
            text="Attendance Chart",
            width=220,
            height=50,
            command=self.show_chart
        ).grid(row=1, column=0, padx=20, pady=20)

        ctk.CTkButton(
            button_frame,
            text="Export Excel",
            width=220,
            height=50,
            command=self.export_excel_file
        ).grid(row=1, column=1, padx=20, pady=20)

        ctk.CTkButton(
            button_frame,
            text="Refresh Dashboard",
            width=220,
            height=50,
            command=self.refresh_cards
        ).grid(row=1, column=2, padx=20, pady=20)

        # ==========================
        # FOOTER
        # ==========================

        footer = ctk.CTkFrame(self)
        footer.pack(fill="x", side="bottom", padx=10, pady=10)

        ctk.CTkLabel(
            footer,
            text="Smart Attendance System © 2026",
            font=("Arial", 14)
        ).pack(pady=10)

    # ==========================
    # DASHBOARD REFRESH
    # ==========================

    def refresh_cards(self):

        try:

            total = total_students()

            self.total_students_card.configure(
                text=f"👨‍🎓\nTotal Students\n{total}"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==========================
    # OPEN WINDOWS
    # ==========================

    def open_students(self):

        try:

            window = StudentPage(self)
            window.grab_set()

        except Exception as e:

            messagebox.showerror(
                "Student Error",
                str(e)
            )

    def open_attendance(self):

        try:

            window = AttendancePage(self)
            window.grab_set()

        except Exception as e:

            messagebox.showerror(
                "Attendance Error",
                str(e)
            )

    def open_reports(self):

        try:

            window = ReportPage(self)
            window.grab_set()

        except Exception as e:

            messagebox.showerror(
                "Report Error",
                str(e)
            )

    # ==========================
    # CHART
    # ==========================

    def show_chart(self):

        try:

            show_pie_chart()

        except Exception as e:

            messagebox.showerror(
                "Chart Error",
                str(e)
            )

    # ==========================
    # EXPORT EXCEL
    # ==========================

    def export_excel_file(self):

        try:

            export_attendance()

            messagebox.showinfo(
                "Success",
                "Attendance exported successfully!"
            )

        except Exception as e:

            messagebox.showerror(
                "Export Error",
                str(e)
            )

    # ==========================
    # LOGOUT
    # ==========================

    def logout(self):

        answer = messagebox.askyesno(
            "Logout",
            "Do you want to logout?"
        )

        if answer:

            self.destroy()

            from login import LoginPage

            app = LoginPage()
            app.mainloop()