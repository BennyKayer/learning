"""Hello world with pyQt5"""

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt5 App")
win_info = {
    "pos_x": 100,
    "pos_y": 100,
    "width": 200,
    "height": 80,
}
window.setGeometry(
    win_info["pos_x"], win_info["pos_y"], win_info["width"], win_info["height"]
)
window.move(60, 15)
helloMsg = QLabel("<h1>Hello World</h1>", parent=window)
helloMsg.move(60, 15)

window.show()
sys.exit(app.exec_())
