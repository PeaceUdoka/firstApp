import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    w = QWidget()
    w.resize(250, 150)
    w.setWindowTitle("LuckyGuess")
    w.move(200,50)
    b = QLabel(w)
    number = int(input("Enter your lucky number: "))
    try:
        if number == 7:
            b.setText("Hoorah!!! You're a winner!")
        else:
            b.setText("Sorry... Try again.")
    except VaueError:
        print("Oops! That's not a number")
    w.show()

    sys.exit(app.exec_())