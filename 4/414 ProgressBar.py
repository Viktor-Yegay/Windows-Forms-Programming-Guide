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
        self.timer1.Interval = 500 # 500 миллисекунд
        self.timer1.Enabled = True
        self.timer1.Tick += self.timer1_Tick

    # обработчик события Tick таймера
    def timer1_Tick(self, sender, EventArgs):
        self.progressBar1.PerformStep()

    def _InitializeComponent(self):
        self.components = System.ComponentModel.Container()
        self.progressBar1 = ProgressBar()
        self.timer1 = Timer(self.components)
        #
        # progressBar1
        #
        self.progressBar1.Location = Point(60, 138)
        self.progressBar1.Name = "progressBar1"
        self.progressBar1.Size = Size(100, 23)
        self.progressBar1.TabIndex = 0
        #
        # Form1
        #
        self.Size = Size(278, 452)
        self.Controls.Add(self.progressBar1)
        self.Name = "Form1"
        self.Text = "ProgressBar"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
