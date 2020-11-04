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
        # установка обработчика события Scroll
        self.trackBar1.Scroll += self.trackBar1_Scroll

    def trackBar1_Scroll(self, sender, EventArgs):
        self.label1.Text = "Текущее значение: {0}".format(self.trackBar1.Value)

    def _InitializeComponent(self):
        self.trackBar1 = TrackBar()
        self.label1 = Label()
        #
        # trackBar1
        #
        self.trackBar1.Location = Point(55, 117)
        self.trackBar1.Name = "trackBar1"
        self.trackBar1.Size = Size(104, 45)
        self.trackBar1.TabIndex = 0
        #
        # label1
        #
        self.label1.AutoSize = True
        self.label1.Location = Point(85, 245)
        self.label1.Name = "label1"
        self.label1.Size = Size(35, 13)
        self.label1.TabIndex = 1
        self.label1.Text = "label1"
        #
        # Form1
        #
        self.Size = Size(278, 452)
        self.Controls.Add(self.label1)
        self.Controls.Add(self.trackBar1)
        self.Name = "Form1"
        self.Text = "TrackBar"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
