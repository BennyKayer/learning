"""Signals and Slots example"""

import sys
import functools

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def greeting(who: str) -> None:
    """Slot function"""

    if msg.text():
        msg.setText("")
    else:
        msg.setText(f"Hello {who}")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Signals and slots")
layout = QVBoxLayout()

btn = QPushButton("Greet")
btn.clicked.connect(functools.partial(greeting, "xd"))

layout.addWidget(btn)
msg = QLabel("")
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec())
