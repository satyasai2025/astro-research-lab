"""
Horoscope Manager Page
Astro Research Lab
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QTableWidget,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


class HoroscopePage(QWidget):
    """
    Horoscope Management Page.

    This page will eventually manage:
    - Add Horoscope
    - Edit Horoscope
    - Delete Horoscope
    - Search Horoscope
    - Import Horoscope
    - Open Horoscope
    """

    def __init__(self):
        super().__init__()

        self.initialize_ui()

    def initialize_ui(self):

        main_layout = QVBoxLayout()

        self.setLayout(main_layout)

        # ----------------------------------------
        # Title
        # ----------------------------------------

        title = QLabel("Horoscope Manager")

        title.setAlignment(Qt.AlignmentFlag.AlignLeft)

        title.setStyleSheet("""
            QLabel{
                font-size:28px;
                font-weight:bold;
            }
        """)

        main_layout.addWidget(title)

        # ----------------------------------------
        # Toolbar
        # ----------------------------------------

        toolbar = QHBoxLayout()

        add_button = QPushButton("New Horoscope")

        edit_button = QPushButton("Edit")

        delete_button = QPushButton("Delete")

        import_button = QPushButton("Import")

        toolbar.addWidget(add_button)

        toolbar.addWidget(edit_button)

        toolbar.addWidget(delete_button)

        toolbar.addWidget(import_button)

        toolbar.addStretch()

        main_layout.addLayout(toolbar)

        # ----------------------------------------
        # Horoscope Table
        # ----------------------------------------

        table = QTableWidget()

        table.setColumnCount(6)

        table.setHorizontalHeaderLabels([
            "ID",
            "Name",
            "Birth Date",
            "Birth Time",
            "Birth Place",
            "Gender"
        ])

        table.setRowCount(0)

        main_layout.addWidget(table)