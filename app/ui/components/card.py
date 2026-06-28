"""
Astro Research Lab

Reusable Premium Card Component
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QFrame,
    QGraphicsDropShadowEffect,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
)

from app.ui.themes.theme import Theme


class Card(QFrame):
    """
    Premium reusable dashboard card.
    """

    def __init__(
        self,
        title: str = "",
        value: str = "",
        subtitle: str = "",
        icon: str = "",
        parent=None,
    ):
        super().__init__(parent)

        self.title = title
        self.value = value
        self.subtitle = subtitle
        self.icon = icon

        self.build_ui()

    # ---------------------------------------------------------

    def build_ui(self):

        self.setObjectName("PremiumCard")

        self.setMinimumSize(300, 180)

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed,
        )

        self.setStyleSheet(f"""
        QFrame#PremiumCard {{
            background:{Theme.CARD};
            border:1px solid {Theme.BORDER};
            border-radius:18px;
        }}

        QFrame#PremiumCard:hover {{
            border:2px solid {Theme.PRIMARY};
        }}
        """)

        shadow = QGraphicsDropShadowEffect(self)

        shadow.setBlurRadius(30)

        shadow.setOffset(0, 8)

        shadow.setColor(QColor(0, 0, 0, 120))

        self.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(22, 22, 22, 22)

        layout.setSpacing(10)

        # -------------------------------------------------

        self.iconLabel = QLabel(self.icon)

        self.iconLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.iconLabel.setStyleSheet("""
        QLabel{
            font-size:34px;
            background:transparent;
        }
        """)

        layout.addWidget(self.iconLabel)

        # -------------------------------------------------

        self.titleLabel = QLabel(self.title)

        self.titleLabel.setStyleSheet(f"""
        QLabel{{
            color:{Theme.TEXT_SECONDARY};
            font-size:15px;
            font-weight:600;
            background:transparent;
        }}
        """)

        layout.addWidget(self.titleLabel)

        # -------------------------------------------------

        layout.addStretch()

        # -------------------------------------------------

        self.valueLabel = QLabel(self.value)

        self.valueLabel.setStyleSheet(f"""
        QLabel{{
            color:{Theme.TEXT};
            font-size:36px;
            font-weight:700;
            background:transparent;
        }}
        """)

        layout.addWidget(self.valueLabel)

        # -------------------------------------------------

        self.subtitleLabel = QLabel(self.subtitle)

        self.subtitleLabel.setWordWrap(True)

        self.subtitleLabel.setStyleSheet(f"""
        QLabel{{
            color:{Theme.TEXT_SECONDARY};
            font-size:13px;
            background:transparent;
        }}
        """)

        layout.addWidget(self.subtitleLabel)

    # ---------------------------------------------------------

    def setTitle(self, title: str):

        self.title = title

        self.titleLabel.setText(title)

    # ---------------------------------------------------------

    def setValue(self, value: str):

        self.value = value

        self.valueLabel.setText(value)

    # ---------------------------------------------------------

    def setSubtitle(self, subtitle: str):

        self.subtitle = subtitle

        self.subtitleLabel.setText(subtitle)

    # ---------------------------------------------------------

    def setIcon(self, icon: str):

        self.icon = icon

        self.iconLabel.setText(icon)