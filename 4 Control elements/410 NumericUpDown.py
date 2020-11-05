# -*- coding: utf-8 -*-
import clr
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System import *
from System.Drawing import *
from System.Windows.Forms import *


class TestWindow(Form):
    def __init__(self):
        self._initialize_components()

    def _initialize_components(self):
        self.numericUpDown1 = NumericUpDown()
        # 
        # numericUpDown1
        # 
        self.numericUpDown1.DecimalPlaces = 3
        self.numericUpDown1.Increment = 0.001
        self.numericUpDown1.Location = Point(65, 40)
        self.numericUpDown1.Name = "numericUpDown1"
        self.numericUpDown1.Size = Size(120, 20)
        self.numericUpDown1.TabIndex = 0
        self.numericUpDown1.ThousandsSeparator = True
        # 
        # Form1
        # 
        self.ClientSize = Size(250, 100)
        self.Controls.Add(self.numericUpDown1)
        self.Name = "Form1"
        self.Text = "NumericUpDown"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
