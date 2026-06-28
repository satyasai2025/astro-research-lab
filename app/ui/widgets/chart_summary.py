"""
Astro Research Lab

Chart Summary Widget
"""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QFormLayout,
    QFrame,
    QLabel,
    QVBoxLayout,
)


class ChartSummaryWidget(QFrame):

    def __init__(self):

        super().__init__()

        self.setObjectName("chartSummary")

        self.setMinimumWidth(320)

        self.title = QLabel("Chart Summary")

        self.title.setObjectName("cardTitle")

        self.form = QFormLayout()

        self.name = QLabel("-")

        self.dob = QLabel("-")

        self.time = QLabel("-")

        self.latitude = QLabel("-")

        self.longitude = QLabel("-")

        self.ascendant = QLabel("-")

        self.planets = QLabel("-")

        self.houses = QLabel("-")

        self.form.addRow("Name", self.name)

        self.form.addRow("Birth Date", self.dob)

        self.form.addRow("Birth Time", self.time)

        self.form.addRow("Latitude", self.latitude)

        self.form.addRow("Longitude", self.longitude)

        self.form.addRow("Ascendant", self.ascendant)

        self.form.addRow("Planets", self.planets)

        self.form.addRow("Houses", self.houses)

        layout = QVBoxLayout(self)

        layout.addWidget(self.title)

        layout.addLayout(self.form)

        layout.addStretch()

    # -------------------------------------------------------

    def set_chart(self, chart):

        self.name.setText(chart.name)

        self.dob.setText(chart.birth_date)

        self.time.setText(chart.birth_time)

        self.latitude.setText(f"{chart.latitude:.4f}")

        self.longitude.setText(f"{chart.longitude:.4f}")

        self.ascendant.setText(

            f"{chart.ascendant_sign} "

            f"{chart.ascendant_degree:.2f}°"

        )

        self.planets.setText(

            str(len(chart.planets))

        )

        self.houses.setText(

            str(len(chart.houses))

        )

    # -------------------------------------------------------

    def clear(self):

        self.name.setText("-")

        self.dob.setText("-")

        self.time.setText("-")

        self.latitude.setText("-")

        self.longitude.setText("-")

        self.ascendant.setText("-")

        self.planets.setText("-")

        self.houses.setText("-")