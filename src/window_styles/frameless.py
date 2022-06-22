from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow


class Frameless:
    @staticmethod
    def setup_flags(parent: QMainWindow):
        parent.setWindowFlag(Qt.FramelessWindowHint)