import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import pandas
import seaborn as sns
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client["local"]
collection = db["deneme"]
data = collection.find()
df = pandas.DataFrame.from_dict(data)

class MatplotlibWidget(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        loadUi("tasarim.ui", self)

        self.setWindowTitle("Korelasyon aracı")

        self.pushButton.clicked.connect(self.update_graph)
        self.pushButton_2.clicked.connect(self.calccorr)

        self.addToolBar(NavigationToolbar(self.TheWidget.canvas, self))
        self.comboBox.addItems(df.columns)
        self.comboBox_2.addItems(df.columns)

    def update_graph(self):
        # sns.heatmap(df['cardiovasc_death_rate'].corr(df['diabetes_prevalence']), vmin=-1, vmax=1, annot=True, cmap='Reds', ax = self.TheWidget.canvas.axes)
        self.TheWidget.canvas.axes.clear()
        heatm = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True, cmap='coolwarm',ax = self.TheWidget.canvas.axes)
        self.TheWidget.canvas.axes.set_title('Korelasyon', fontdict={'fontsize': 12}, pad=12)
        self.TheWidget.canvas.draw()
    def calccorr(self):
        try:
            corrvalue = df[self.comboBox.currentText()].corr(df[self.comboBox_2.currentText()])
            corrvalue = round(corrvalue,2)
            self.label_3.setText(str(corrvalue))
            if (corrvalue < -0.5):
                self.label_4.setText("Negatif yönde güçlü ilişki.")
                self.label_4.setStyleSheet("QLabel {color : rgb(117, 83, 250); }")
            elif (corrvalue < 0):
                self.label_4.setText("Negatif yönde zayıf ilişki.")
                self.label_4.setStyleSheet("QLabel {color : rgb(187, 169, 255); }")
            elif (corrvalue < 0.5):
                self.label_4.setText("Pozitif yönde zayıf ilişki.")
                self.label_4.setStyleSheet("QLabel {color : rgb(255, 124, 128); }")
            elif (corrvalue < 1):
                self.label_4.setText("Pozitif yönde güçlü ilişki.")
                self.label_4.setStyleSheet("QLabel {color : rgb(255, 64, 70); }")


        except:
            print("Veri nümerik olmayabilir.")

app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()