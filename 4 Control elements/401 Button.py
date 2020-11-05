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

    def button1_Click(self, sender, EventArgs):
        MessageBox.Show("Hello World")

    def _InitializeComponent(self):
        self.button1 = Button()
        # 
        # button1
        # 
        self.button1.Location = Point(119, 97)
        self.button1.Name = "button1"
        self.button1.Size = Size(75, 23)
        self.button1.TabIndex = 0
        self.button1.Text = "button1"
        self.button1.UseVisualStyleBackColor = True
        self.button1.Click += System.EventHandler(self.button1_Click)
        # 
        # Form1
        # 
        self.Size = Size(305, 229)
        self.Controls.Add(self.button1)
        self.Name = "Form1"
        self.Text = "Button"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
