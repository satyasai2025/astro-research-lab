"""
Astro Research Lab

Planet Table Widget
"""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QLabel,
)


class PlanetTableWidget(QFrame):

    HEADERS = [
        "Planet",
        "Sign",
        "Degree",
        "House",
        "Dignity",
        "Retro",
    ]

    def __init__(self):

        super().__init__()

        self.setObjectName("planetTable")

        title = QLabel("Planet Positions")

        title.setObjectName("cardTitle")

        self.table = QTableWidget()

        self.table.setColumnCount(len(self.HEADERS))

        self.table.setHorizontalHeaderLabels(self.HEADERS)

        self.table.verticalHeader().setVisible(False)

        self.table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        self.table.setSelectionMode(
            QTableWidget.SelectionMode.NoSelection
        )

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout = QVBoxLayout(self)

        layout.addWidget(title)

        layout.addWidget(self.table)

    # --------------------------------------------------------

    def set_chart(self, chart):

        planets = list(chart.planets.values())

        self.table.setRowCount(len(planets))

        for row, planet in enumerate(planets):

            values = [

                planet.name,

                planet.sign,

                f"{planet.degree:.2f}°",

                str(planet.house),

                planet.dignity,

                "R" if planet.retrograde else "-",

            ]

            for col, value in enumerate(values):

                item = QTableWidgetItem(str(value))

                item.setTextAlignment(

                    Qt.AlignmentFlag.AlignCenter

                )

                self.table.setItem(

                    row,

                    col,

                    item,

                )

    # --------------------------------------------------------

    def clear(self):

        self.table.setRowCount(0)