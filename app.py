from model import Model
from PyQt5.QtCore import *
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat
from PyQt5.QtWidgets import QApplication, QLabel, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QLineEdit
import time

model = Model()

APP_TITLE = "343 Stock Price Monitor"
VERSION = " v1.0"
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 480

running = True

class AThread(QThread):
  def run(self):
    global running
    stock_name = stock_name_input_field.text()
    if not running:
      running = True
    while running:
      text_area.verticalScrollBar().setValue(text_area.verticalScrollBar().maximum())
      if running == False:
        break
      stock_price = model.getStockPrice(stock_name)
      msg = str(stock_price) + " @ " + model.getTime()
      getStockPrice(msg + " - " + model.strategy1(float(stock_price)))
      text_area.verticalScrollBar().setValue(text_area.verticalScrollBar().maximum())
      time.sleep(0.1)


thread = AThread()

def getStockPrice(stock_price):
  text_area.append(stock_price)

def run():
  thread.start()
  stock_name = stock_name_input_field.text()
  text_area.append("Getting prices for " + stock_name)
  run_button.setEnabled(False)


def stop():
  global running
  text_area.verticalScrollBar().setValue(text_area.verticalScrollBar().maximum())
  running = False
  run_button.setEnabled(True)
  text_area.append("******** STOPPED. ***********")



###### Set up UI ######
app = QApplication([])

###### Main Window ######
window = QWidget()
window.setObjectName("window")
window.setStyleSheet(open("style/style.qss", "r").read())
window.setWindowTitle(APP_TITLE + VERSION)
window.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
###### Left Side Panel ######
left_side = QWidget()
left_side.setObjectName("leftSide")
left_side_layout = QVBoxLayout()
left_side_layout.setAlignment(Qt.AlignTop)
left_side_layout.addWidget(QLabel("Stock Name:"))
stock_name_input_field = QLineEdit()
left_side_layout.addWidget(stock_name_input_field)
left_side_layout.addWidget(QLabel("Number of Shares:"))
shares_input_field = QLineEdit()
left_side_layout.addWidget(shares_input_field)
run_button = QPushButton("Run")
run_button.setObjectName("runButton")
run_button.clicked.connect(run)
left_side_layout.addWidget(run_button)
stop_button = QPushButton("Stop")
stop_button.setObjectName("stopButton")
stop_button.clicked.connect(stop)
left_side_layout.addWidget(stop_button)
left_side.setLayout(left_side_layout)
###### Right Side Panel ######
right_side = QWidget()
right_side.setObjectName("rightSide")
right_side_layout = QHBoxLayout()
right_side_layout.setAlignment(Qt.AlignTop)

text_area = QTextEdit()
text_area.setObjectName("textArea")
text_area.setPlaceholderText("Messages will go here.")
text_area.setEnabled(False)
right_side_layout.addWidget(text_area)
right_side.setLayout(right_side_layout)
main_layout = QHBoxLayout()
main_layout.addWidget(left_side)
main_layout.addWidget(right_side)
window.setLayout(main_layout)
window.show()
app.exec_()
