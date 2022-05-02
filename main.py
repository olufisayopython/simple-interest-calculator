import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class appDemo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple interest calculator")
        self.setWindowIcon(QIcon('C:\\Users\\FISAYO\\Downloads\\icons8-calculator-64.png'))
        principalLabel = QLabel('Principal: ')
        self.principalSpinBox = QDoubleSpinBox()
        self.principalSpinBox.setRange(0, 100_000_000_000)
        self.principalSpinBox.setValue(0)
        self.principalSpinBox.setPrefix('$')
        self.principalSpinBox.valueChanged.connect(self.calculate_interest)

        rateLabel = QLabel('Rate:')
        self.rateSpinBox = QDoubleSpinBox()
        self.rateSpinBox.setRange(0, 100)
        self.rateSpinBox.setValue(0)
        self.rateSpinBox.setSuffix('%')
        self.rateSpinBox.valueChanged.connect(self.calculate_interest)

        yearLabel = QLabel('Year:')
        self.yearsComboBox = QComboBox()
        self.yearsComboBox.addItem('1 year')
        self.yearsComboBox.addItems(['{0} years'.format(year) for year in range(2, 50)])
        self.yearsComboBox.currentIndexChanged.connect(self.calculate_interest)
        amountLabel = QLabel('Amount:')
        self.dollarLabel = QLabel()
        self.calculate_interest()
        gridLayout = QGridLayout()
        gridLayout.addWidget(principalLabel, 0, 0)
        gridLayout.addWidget(self.principalSpinBox, 0, 1)
        gridLayout.addWidget(rateLabel, 1, 0)
        gridLayout.addWidget(self.rateSpinBox, 1, 1)
        gridLayout.addWidget(yearLabel, 2, 0)
        gridLayout.addWidget(self.yearsComboBox, 2, 1)
        gridLayout.addWidget(amountLabel, 3, 0)
        gridLayout.addWidget(self.dollarLabel, 3, 1)

        vlayout = QVBoxLayout()
        vlayout.addLayout(gridLayout)

        self.setLayout(vlayout)

    def calculate_interest(self):
        p = self.principalSpinBox.value()
        r = self.rateSpinBox.value()
        y = self.yearsComboBox.currentIndex() + 1
        amount = p*((1 + (r/100.00)) **y)
        self.dollarLabel.setText('$ {0:.2f}'.format(amount))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = appDemo()
    window.show()
    sys.exit(app.exec_())