"""
Add Horoscope Dialog
Astro Research Lab
"""

from PySide6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QTextEdit,
    QTimeEdit,
    QVBoxLayout,
)

from app.database.database import DatabaseManager


class AddHoroscopeDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setWindowTitle("Add Horoscope")

        self.resize(520, 650)

        self.build_ui()

    # --------------------------------------------------

    def build_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel("New Horoscope")

        title.setStyleSheet("""
            font-size:24px;
            font-weight:700;
        """)

        layout.addWidget(title)

        form = QFormLayout()

        # --------------------------------------------

        self.full_name = QLineEdit()

        form.addRow("Full Name", self.full_name)

        # --------------------------------------------

        self.gender = QComboBox()

        self.gender.addItems([
            "Male",
            "Female",
            "Other"
        ])

        form.addRow("Gender", self.gender)

        # --------------------------------------------

        self.birth_date = QDateEdit()

        self.birth_date.setCalendarPopup(True)

        form.addRow("Birth Date", self.birth_date)

        # --------------------------------------------

        self.birth_time = QTimeEdit()

        form.addRow("Birth Time", self.birth_time)

        # --------------------------------------------

        self.birth_place = QLineEdit()

        form.addRow("Birth Place", self.birth_place)

        # --------------------------------------------

        self.latitude = QDoubleSpinBox()

        self.latitude.setRange(-90.0, 90.0)

        self.latitude.setDecimals(6)

        form.addRow("Latitude", self.latitude)

        # --------------------------------------------

        self.longitude = QDoubleSpinBox()

        self.longitude.setRange(-180.0, 180.0)

        self.longitude.setDecimals(6)

        form.addRow("Longitude", self.longitude)

        # --------------------------------------------

        self.timezone = QLineEdit()

        self.timezone.setPlaceholderText("Asia/Kolkata")

        form.addRow("Timezone", self.timezone)

        # --------------------------------------------

        self.ayanamsa = QComboBox()

        self.ayanamsa.addItems([
            "Lahiri",
            "Raman",
            "Krishnamurti",
            "Fagan Bradley"
        ])

        form.addRow("Ayanamsa", self.ayanamsa)

        # --------------------------------------------

        self.notes = QTextEdit()

        self.notes.setMinimumHeight(120)

        form.addRow("Notes", self.notes)

        layout.addLayout(form)

        # --------------------------------------------

        buttons = QDialogButtonBox(

            QDialogButtonBox.Save |
            QDialogButtonBox.Cancel

        )

        buttons.accepted.connect(self.save)

        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

    # --------------------------------------------------

    def save(self):

        if not self.full_name.text().strip():

            QMessageBox.warning(
                self,
                "Validation",
                "Full Name is required."
            )

            return

        DatabaseManager.add_horoscope(

            full_name=self.full_name.text(),

            gender=self.gender.currentText(),

            birth_date=self.birth_date.date().toString("yyyy-MM-dd"),

            birth_time=self.birth_time.time().toString("HH:mm:ss"),

            birth_place=self.birth_place.text(),

            latitude=self.latitude.value(),

            longitude=self.longitude.value(),

            timezone=self.timezone.text(),

            ayanamsa=self.ayanamsa.currentText(),

            notes=self.notes.toPlainText(),

        )

        QMessageBox.information(

            self,

            "Success",

            "Horoscope saved successfully."

        )

        self.accept()