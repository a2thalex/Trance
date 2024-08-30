import sys
from PyQt6.QtWidgets import QApplication
from beat_maker import BeatMaker

def main():
    app = QApplication(sys.argv)
    beat_maker = BeatMaker()
    beat_maker.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
