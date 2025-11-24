from PySide6.QtWidgets import QApplication
import sys
from schermate.schermate import View

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = View()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())