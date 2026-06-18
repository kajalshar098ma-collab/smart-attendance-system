from database import initialize_database
from login import LoginPage


def main():

    initialize_database()

    app = LoginPage()

    app.mainloop()


if __name__ == "__main__":

    main()