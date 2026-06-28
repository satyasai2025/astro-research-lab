"""
Astro Research Lab

Premium Statistic Card
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout

from app.ui.components.card import Card
from app.ui.themes.theme import Theme


class StatCard(Card):
    """
    Dashboard KPI Card.

    Example

    StatCard(
        icon="👤",
        title="Horoscopes",
        value="12,458",
        subtitle="+245 This Month"
    )
    """

    def __init__(
        self,
        icon: str,
        title: str,
        value: str,
        subtitle: str,
        trend: str = "",
        parent=None,
    ):

        super().__init__(
            icon=icon,
            title=title,
            value=value,
            subtitle=subtitle,
            parent=parent,
        )

        self.trend = trend

        self.build_footer()

    # ---------------------------------------------------------

    def build_footer(self):

        footer = QHBoxLayout()

        footer.setContentsMargins(0, 10, 0, 0)

        footer.setSpacing(8)

        self.trendLabel = QLabel(self.trend)

        self.trendLabel.setStyleSheet(f"""
        QLabel {{
            color:{Theme.SUCCESS};
            font-size:13px;
            font-weight:600;
            background:transparent;
        }}
        """)

        footer.addWidget(self.trendLabel)

        footer.addStretch()

        self.layout().addLayout(footer)

    # ---------------------------------------------------------

    def setTrend(
        self,
        trend: str,
    ):

        self.trend = trend

        self.trendLabel.setText(trend)

    # ---------------------------------------------------------

    def setTrendColor(
        self,
        color: str,
    ):

        self.trendLabel.setStyleSheet(f"""
        QLabel {{
            color:{color};
            font-size:13px;
            font-weight:600;
            background:transparent;
        }}
        """)