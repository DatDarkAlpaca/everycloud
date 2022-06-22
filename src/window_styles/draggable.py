from PySide6.QtWidgets import QMainWindow


class Draggable(QMainWindow):
    def __init__(self, parent=None):
        super(Draggable, self).__init__(parent)
        self.offset = None

    def mousePressEvent(self, event):
        self.offset = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = event.globalPos() - self.offset
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.offset = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.offset = event.globalPos()
