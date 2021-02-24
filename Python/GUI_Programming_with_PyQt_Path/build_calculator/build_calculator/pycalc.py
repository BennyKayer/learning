"""Calculator build using pyqt"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

__version__ = "0.1"
__author__ = "Paweł Benkowski"


class PyCalcUi(QMainWindow):
    """PyCalc's View (GUI)

    Args:
        QMainWindow ([type]): [description]
    """

    def __init__(self):
        """View Initializer"""
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(235, 235)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignMent(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)


def main():
    pycalc = QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    sys.exit(pycalc.exec())


if __name__ == "__main__":
    main()
