"""
Astro Research Lab
Modern Theme System
"""

from PySide6.QtGui import QColor


class Theme:
    """
    Global Design System
    """

    # ---------------------------------------------------------
    # Colors
    # ---------------------------------------------------------

    BACKGROUND = "#0F172A"
    SURFACE = "#111827"
    CARD = "#1E293B"

    PRIMARY = "#6366F1"
    PRIMARY_HOVER = "#7C83FF"
    SECONDARY = PRIMARY_HOVER

    SUCCESS = "#22C55E"
    WARNING = "#F59E0B"
    DANGER = "#EF4444"

    TEXT = "#F8FAFC"
    TEXT_SECONDARY = "#94A3B8"

    BORDER = "#334155"

    SIDEBAR = "#111827"

    HOVER = "#1E293B"

    # ---------------------------------------------------------
    # Radius
    # ---------------------------------------------------------

    RADIUS_SMALL = 8
    RADIUS = 14
    RADIUS_LARGE = 22

    # ---------------------------------------------------------
    # Spacing
    # ---------------------------------------------------------

    XS = 4
    SM = 8
    MD = 16
    LG = 24
    XL = 32
    XXL = 48

    # ---------------------------------------------------------
    # Typography
    # ---------------------------------------------------------

    FONT = "Segoe UI"

    H1 = 34
    H2 = 26
    H3 = 20

    BODY = 14
    SMALL = 12

    # ---------------------------------------------------------
    # Icons
    # ---------------------------------------------------------

    SIDEBAR_WIDTH = 250

    # ---------------------------------------------------------
    # Shadow
    # ---------------------------------------------------------

    SHADOW_COLOR = QColor(0, 0, 0, 120)

    SHADOW_BLUR = 35

    SHADOW_OFFSET = 8

    # ---------------------------------------------------------

    @classmethod
    def stylesheet(cls):

        return f"""

        *{{
            font-family:"{cls.FONT}";
            color:{cls.TEXT};
            font-size:14px;
        }}

        QMainWindow{{
            background:{cls.BACKGROUND};
        }}

        QWidget{{
            background:{cls.BACKGROUND};
            color:{cls.TEXT};
        }}

        QLabel{{
            background:transparent;
        }}

        QPushButton{{
            background:{cls.CARD};
            color:{cls.TEXT};
            border:none;
            border-radius:{cls.RADIUS}px;
            padding:10px 16px;
            font-size:14px;
            font-weight:600;
        }}

        QPushButton:hover{{
            background:{cls.PRIMARY};
        }}

        QPushButton:pressed{{
            background:{cls.PRIMARY_HOVER};
        }}

        QLineEdit,
        QTextEdit,
        QPlainTextEdit,
        QComboBox,
        QDateEdit,
        QTimeEdit,
        QSpinBox,
        QDoubleSpinBox{{
            background:{cls.SURFACE};
            border:1px solid {cls.BORDER};
            border-radius:{cls.RADIUS}px;
            padding:8px;
            color:{cls.TEXT};
        }}

        QLineEdit:focus,
        QTextEdit:focus,
        QComboBox:focus{{
            border:2px solid {cls.PRIMARY};
        }}

        QListWidget{{
            background:{cls.SURFACE};
            border:none;
        }}

        QTreeWidget{{
            background:{cls.SURFACE};
            border:none;
        }}

        QTableWidget{{
            background:{cls.SURFACE};
            border:none;
            gridline-color:{cls.BORDER};
        }}

        QHeaderView::section{{
            background:{cls.CARD};
            border:none;
            padding:8px;
            font-weight:600;
        }}

        QScrollArea{{
            border:none;
            background:transparent;
        }}

        QScrollBar:vertical{{
            background:{cls.SURFACE};
            width:10px;
            border:none;
        }}

        QScrollBar::handle:vertical{{
            background:{cls.BORDER};
            border-radius:5px;
        }}

        QScrollBar::handle:vertical:hover{{
            background:{cls.PRIMARY};
        }}

        QStatusBar{{
            background:{cls.SURFACE};
            border-top:1px solid {cls.BORDER};
        }}

        QMenuBar{{
            background:{cls.BACKGROUND};
        }}

        QMenu{{
            background:{cls.SURFACE};
        }}

        QToolTip{{
            background:{cls.CARD};
            color:white;
            border:none;
            padding:6px;
        }}
        """