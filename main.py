import sys
from PyQt5.QtWidgets import QApplication
from gui.app import ShoeCollectionApp

def main():
    app = QApplication(sys.argv)
    window = ShoeCollectionApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()