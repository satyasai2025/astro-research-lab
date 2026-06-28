"""
Astro Research Lab

House Table Widget
"""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QHeaderView,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)


class HouseTableWidget(QFrame):

    HEADERS = [
        "House",
        "Sign",
        "Degree",
        "Occupants",
        "Kendra",
        "Trikona",
    ]

    def __init__(self):

        super().__init__()

        self.setObjectName("houseTable")

        title = QLabel("House Details")

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

    # ------------------------------------------------------

    def set_chart(self, chart):

        houses = chart.houses

        self.table.setRowCount(len(houses))

        for row, house in enumerate(houses):

            occupants = ", ".join(house.occupants)

            values = [

                house.number,

                house.sign,

                f"{house.degree:.2f}°",

                occupants if occupants else "-",

                "✓" if house.is_kendra else "-",

                "✓" if house.is_trikona else "-",

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

    # ------------------------------------------------------

    def clear(self):

        self.table.setRowCount(0)


if __name__ == "__main__":

    import sys
    from datetime import datetime

    from PyQt6.QtWidgets import QApplication

    from app.engines.chart_engine.builder import ChartEngine

    app = QApplication(sys.argv)

    engine = ChartEngine()

    chart = engine.build_chart(

        name="Demo",

        birth_datetime=datetime(

            1995,

            8,

            15,

            10,

            30,

        ),

        latitude=28.6139,

        longitude=77.2090,

        timezone=5.5,

    )

    widget = HouseTableWidget()

    widget.set_chart(chart)

    widget.resize(900, 450)

    widget.show()

    sys.exit(app.exec())