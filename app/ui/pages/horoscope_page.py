"""
Horoscope Manager Page
Astro Research Lab
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QAbstractItemView,
    QHeaderView,
)

from app.database.database import DatabaseManager
from app.ui.dialogs.add_horoscope_dialog import AddHoroscopeDialog


class HoroscopePage(QWidget):

    def __init__(self):

        super().__init__()

        self.records = []

        self.build_ui()

        self.load_data()

    # ---------------------------------------------------------

    def build_ui(self):

        root = QVBoxLayout(self)

        root.setContentsMargins(25, 25, 25, 25)

        root.setSpacing(20)

        # =====================================================
        # Header
        # =====================================================

        header = QHBoxLayout()

        title = QLabel("Horoscope Manager")

        title.setStyleSheet("""

            QLabel{

                font-size:28px;

                font-weight:700;

            }

        """)

        header.addWidget(title)

        header.addStretch()

        self.total_label = QLabel("Total : 0")

        self.total_label.setStyleSheet("""

            QLabel{

                font-size:14px;

                font-weight:600;

            }

        """)

        header.addWidget(self.total_label)

        root.addLayout(header)

        # =====================================================
        # Toolbar
        # =====================================================

        toolbar = QHBoxLayout()

        self.search_box = QLineEdit()

        self.search_box.setPlaceholderText(
            "Search by name, place, gender or ayanamsa..."
        )

        self.search_box.textChanged.connect(
            self.search_records
        )

        toolbar.addWidget(
            self.search_box,
            1,
        )

        self.refresh_button = QPushButton("🔄 Refresh")

        self.refresh_button.clicked.connect(
            self.load_data
        )

        toolbar.addWidget(
            self.refresh_button
        )

        self.add_button = QPushButton("➕ Add Horoscope")

        self.add_button.clicked.connect(
            self.add_horoscope
        )

        toolbar.addWidget(
            self.add_button
        )

        self.delete_button = QPushButton("🗑 Delete")

        self.delete_button.clicked.connect(
            self.delete_selected
        )

        toolbar.addWidget(
            self.delete_button
        )

        root.addLayout(toolbar)

        # =====================================================
        # Table
        # =====================================================

        self.table = QTableWidget()

        self.table.setColumnCount(7)

        self.table.setHorizontalHeaderLabels(

            [

                "ID",

                "Full Name",

                "Gender",

                "Birth Date",

                "Birth Time",

                "Birth Place",

                "Ayanamsa",

            ]

        )

        self.table.setSelectionBehavior(

            QAbstractItemView.SelectRows

        )

        self.table.setSelectionMode(

            QAbstractItemView.SingleSelection

        )

        self.table.setEditTriggers(

            QAbstractItemView.NoEditTriggers

        )

        self.table.setAlternatingRowColors(True)

        self.table.verticalHeader().setVisible(False)

        header = self.table.horizontalHeader()

        header.setSectionResizeMode(
            QHeaderView.Stretch
        )

        header.setSectionResizeMode(
            0,
            QHeaderView.ResizeToContents
        )

        root.addWidget(
            self.table,
            1,
        )

        # =====================================================
        # Footer
        # =====================================================

        footer = QHBoxLayout()

        self.status_label = QLabel("Ready")

        footer.addWidget(
            self.status_label
        )

        footer.addStretch()

        root.addLayout(
            footer
        )

    # ---------------------------------------------------------

    def populate_table(
        self,
        rows,
    ):

        self.records = rows

        self.table.setRowCount(
            len(rows)
        )

        for row_index, row in enumerate(rows):

            self.table.setItem(
                row_index,
                0,
                QTableWidgetItem(str(row["id"]))
            )

            self.table.setItem(
                row_index,
                1,
                QTableWidgetItem(row["full_name"])
            )

            self.table.setItem(
                row_index,
                2,
                QTableWidgetItem(row["gender"])
            )

            self.table.setItem(
                row_index,
                3,
                QTableWidgetItem(row["birth_date"])
            )

            self.table.setItem(
                row_index,
                4,
                QTableWidgetItem(row["birth_time"])
            )

            self.table.setItem(
                row_index,
                5,
                QTableWidgetItem(row["birth_place"])
            )

            self.table.setItem(
                row_index,
                6,
                QTableWidgetItem(row["ayanamsa"])
            )

        self.update_statistics()

        self.status_label.setText(
            f"{len(rows)} horoscope(s) loaded"
        )
            # ---------------------------------------------------------

    def load_data(self):

        rows = DatabaseManager.get_all_horoscopes()

        self.populate_table(rows)
        self.update_statistics()

    # ---------------------------------------------------------

    def search_records(self):

        keyword = self.search_box.text().strip()

        if keyword == "":

            self.load_data()

            return

        rows = DatabaseManager.search_horoscopes(keyword)

        self.populate_table(rows)

    # ---------------------------------------------------------

    def add_horoscope(self):

        dialog = AddHoroscopeDialog(self)

        if dialog.exec():

            self.load_data()

            self.status_label.setText(
                "Horoscope added successfully."
            )

    # ---------------------------------------------------------

    def selected_id(self):

        selected = self.table.selectedItems()

        if not selected:

            return None

        return int(selected[0].text())

    # ---------------------------------------------------------

    def delete_selected(self):

        horoscope_id = self.selected_id()

        if horoscope_id is None:

            QMessageBox.information(

                self,

                "Delete Horoscope",

                "Please select a horoscope."

            )

            return

        answer = QMessageBox.question(

            self,

            "Delete Horoscope",

            "Delete selected horoscope?"

        )

        if answer != QMessageBox.StandardButton.Yes:

            return

        DatabaseManager.delete_horoscope(
            horoscope_id
        )

        self.load_data()

        self.status_label.setText(
            "Horoscope deleted."
        )

    # ---------------------------------------------------------

    def refresh(self):

        self.search_box.clear()

        self.load_data()

        self.status_label.setText(
            "Data refreshed."
        )
            # ---------------------------------------------------------

    def clear_table(self):

        self.table.setRowCount(0)

        self.records.clear()

        self.total_label.setText("Total : 0")

        self.status_label.setText("No records")

    # ---------------------------------------------------------

    def selected_record(self):

        row = self.table.currentRow()

        if row < 0:

            return None

        return {

            "id": self.table.item(row, 0).text(),

            "full_name": self.table.item(row, 1).text(),

            "gender": self.table.item(row, 2).text(),

            "birth_date": self.table.item(row, 3).text(),

            "birth_time": self.table.item(row, 4).text(),

            "birth_place": self.table.item(row, 5).text(),

            "ayanamsa": self.table.item(row, 6).text(),

        }

    # ---------------------------------------------------------

    def update_statistics(self):

        total = DatabaseManager.total_horoscopes()

        self.total_label.setText(
            f"Total : {total}"
        )

        self.status_label.setText(
            f"Database contains {total} horoscope(s)"
        )

    # ---------------------------------------------------------

    def showEvent(self, event):

        super().showEvent(event)

        self.load_data()

        self.update_statistics()

    # ---------------------------------------------------------

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.table.resizeColumnsToContents()

        self.table.horizontalHeader().setStretchLastSection(True)

    # ---------------------------------------------------------

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_F5:

            self.refresh()

            return

        if event.key() == Qt.Key_Delete:

            self.delete_selected()

            return

        super().keyPressEvent(event)