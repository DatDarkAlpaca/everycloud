from PySide6.QtWidgets import QApplication
from everycloud import EveryCloud


def main():
    app = QApplication()

    window = EveryCloud()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
