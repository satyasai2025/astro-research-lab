"""
Astro Research Lab
Modern UI Theme
"""

from PySide6.QtGui import QColor


class Theme:

    # =====================================================
    # COLORS
    # =====================================================

    BACKGROUND = "#0F172A"
    SURFACE = "#1E293B"
    CARD = "#273449"

    PRIMARY = "#6366F1"
    SECONDARY = "#8B5CF6"

    CYAN = "#06B6D4"

    SUCCESS = "#22C55E"
    WARNING = "#F59E0B"
    DANGER = "#EF4444"

    TEXT = "#F8FAFC"
    TEXT_SECONDARY = "#CBD5E1"

    BORDER = "#334155"

    HOVER = "#334155"

    # =====================================================
    # RADIUS
    # =====================================================

    WINDOW_RADIUS = 18

    CARD_RADIUS = 18

    BUTTON_RADIUS = 12

    INPUT_RADIUS = 12

    # =====================================================
    # SPACING
    # =====================================================

    XS = 4

    SM = 8

    MD = 16

    LG = 24

    XL = 32

    XXL = 48

    # =====================================================
    # TYPOGRAPHY
    # =====================================================

    FONT = "Segoe UI"

    H1 = 32

    H2 = 24

    H3 = 20

    BODY = 14

    SMALL = 12

    # =====================================================
    # SIDEBAR
    # =====================================================

    SIDEBAR_WIDTH = 270

    # =====================================================
    # GLOBAL STYLESHEET
    # =====================================================

    @classmethod
    def stylesheet(cls):

        return f"""

        QWidget{{
            background:{cls.BACKGROUND};
            color:{cls.TEXT};
            font-family:{cls.FONT};
            font-size:{cls.BODY}px;
        }}

        QMainWindow{{
            background:{cls.BACKGROUND};
        }}

        QFrame{{
            background:{cls.SURFACE};
            border-radius:{cls.CARD_RADIUS}px;
        }}

        QPushButton{{
            background:{cls.PRIMARY};
            color:white;
            border:none;
            border-radius:{cls.BUTTON_RADIUS}px;
            padding:10px 18px;
            font-weight:600;
        }}

        QPushButton:hover{{
            background:{cls.SECONDARY};
        }}

        QPushButton:pressed{{
            background:#4338CA;
        }}

        QLabel{{
            color:{cls.TEXT};
        }}

        QLineEdit,
        QTextEdit,
        QPlainTextEdit,
        QComboBox,
        QDateEdit,
        QTimeEdit{{
            background:{cls.CARD};
            color:{cls.TEXT};
            border:1px solid {cls.BORDER};
            border-radius:{cls.INPUT_RADIUS}px;
            padding:8px;
        }}

        QTableWidget{{
            background:{cls.SURFACE};
            border:1px solid {cls.BORDER};
            border-radius:14px;
            gridline-color:{cls.BORDER};
            selection-background-color:{cls.PRIMARY};
        }}

        QHeaderView::section{{
            background:{cls.CARD};
            color:{cls.TEXT};
            border:none;
            padding:10px;
            font-weight:bold;
        }}

        QScrollBar:vertical{{
            background:transparent;
            width:10px;
        }}

        QScrollBar::handle:vertical{{
            background:{cls.BORDER};
            border-radius:5px;
        }}

        QStatusBar{{
            background:{cls.SURFACE};
            color:{cls.TEXT_SECONDARY};
        }}

        """