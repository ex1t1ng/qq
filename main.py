import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QColor
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw_circle)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

    def draw_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.graphicsView.width() - diameter)
        y = random.randint(0, self.graphicsView.height() - diameter)
        color = QColor(Qt.yellow)
        painter = QPainter()
        painter.begin(self.graphicsView.viewport())
        painter.setBrush(color)
        painter.drawEllipse(QPointF(x, y), diameter, diameter)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
