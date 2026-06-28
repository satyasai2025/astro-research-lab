"""
Astro Research Lab
Application Entry Point
"""

import sys
import traceback

from PySide6.QtWidgets import QApplication, QMessageBox

from app.config.settings import (
    APP_NAME,
    APP_VERSION,
)
from app.database.database import DatabaseManager
from app.ui.windows.main_window import MainWindow


def exception_hook(exc_type, exc_value, exc_tb):
    """
    Global exception handler.
    """

    traceback_text = "".join(
        traceback.format_exception(
            exc_type,
            exc_value,
            exc_tb,
        )
    )

    print(traceback_text)

    try:
        QMessageBox.critical(
            None,
            "Unexpected Error",
            traceback_text,
        )
    except Exception:
        pass


def create_application() -> QApplication:
    """
    Creates and configures QApplication.
    """

    app = QApplication(sys.argv)

    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setOrganizationName("Astro Research Lab")
    app.setOrganizationDomain("local")

    return app


def initialize():
    """
    Initialize application services.
    """

    DatabaseManager.initialize()


def main() -> int:
    """
    Application entry point.
    """

    sys.excepthook = exception_hook

    initialize()

    app = create_application()

    window = MainWindow()

    window.show()
    window.raise_()
    window.activateWindow()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())