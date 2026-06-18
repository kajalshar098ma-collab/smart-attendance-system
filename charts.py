import matplotlib.pyplot as plt

from database import attendance_summary


def show_pie_chart():

    data = attendance_summary()

    if not data:

        plt.figure(figsize=(6, 6))

        plt.text(
            0.5,
            0.5,
            "No Attendance Data Available",
            ha="center",
            va="center",
            fontsize=14
        )

        plt.axis("off")

        plt.show()

        return

    labels = []
    values = []

    for row in data:

        labels.append(row[0])
        values.append(row[1])

    plt.figure(figsize=(7, 7))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title(
        "Attendance Summary"
    )

    plt.show()