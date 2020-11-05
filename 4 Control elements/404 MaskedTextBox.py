# -*- coding: utf-8 -*-
import clr
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

import System
from System.Drawing import *
from System.Windows.Forms import *


class TestWindow(Form):
    def __init__(self):
        self._InitializeComponent()

    def _InitializeComponent(self):
        self.maskedTextBox1 = MaskedTextBox()
        # 
        # maskedTextBox1
        # 
        self.maskedTextBox1.Location = Point(109, 71)
        self.maskedTextBox1.Mask = "L.L.L?????????"
        self.maskedTextBox1.Name = "maskedTextBox1"
        self.maskedTextBox1.Size = Size(100, 20)
        self.maskedTextBox1.TabIndex = 0
        # 
        # Form1
        # 
        self.Size = Size(305, 162)
        self.Controls.Add(self.maskedTextBox1)
        self.Name = "Form1"
        self.Text = "MaskedTextBox"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
