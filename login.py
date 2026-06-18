import customtkinter as ctk
from tkinter import messagebox

from dashboard import Dashboard

from database import (
    validate_user,
    register_user
)


class LoginPage(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Smart Attendance System")
        self.geometry("500x550")

        ctk.set_appearance_mode("dark")

        ctk.CTkLabel(
            self,
            text="Smart Attendance System",
            font=("Arial", 28, "bold")
        ).pack(pady=30)

        self.username = ctk.CTkEntry(
            self,
            width=250,
            placeholder_text="Username"
        )
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(
            self,
            width=250,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=10)

        ctk.CTkButton(
            self,
            text="Login",
            width=200,
            command=self.login
        ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="Register",
            width=200,
            command=self.open_register
        ).pack(pady=10)

    def login(self):

        username = self.username.get().strip()
        password = self.password.get().strip()

        user = validate_user(
            username,
            password
        )

        if user:

            self.destroy()

            dashboard = Dashboard(username)

            dashboard.mainloop()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password"
            )

    def open_register(self):

        RegisterPage(self)


class RegisterPage(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.title("Register Account")
        self.geometry("400x450")

        ctk.CTkLabel(
            self,
            text="Create Account",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        self.username = ctk.CTkEntry(
            self,
            width=250,
            placeholder_text="Username"
        )
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(
            self,
            width=250,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=10)

        self.role = ctk.CTkOptionMenu(
            self,
            values=["Admin", "Student"]
        )
        self.role.pack(pady=10)

        ctk.CTkButton(
            self,
            text="Create Account",
            command=self.register
        ).pack(pady=20)

    def register(self):

        username = self.username.get().strip()
        password = self.password.get().strip()
        role = self.role.get()

        if not username or not password:

            messagebox.showerror(
                "Error",
                "Please fill all fields"
            )
            return

        success = register_user(
            username,
            password,
            role
        )

        if success:

            messagebox.showinfo(
                "Success",
                "Account Created Successfully"
            )

            self.destroy()

        else:

            messagebox.showerror(
                "Error",
                "Username Already Exists"
            )