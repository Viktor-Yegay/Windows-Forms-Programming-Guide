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
        self.textBox1.TextChanged += self.textBox1_TextChanged

    def textBox1_TextChanged(self, sender, EventArgs):
        self.label1.Text = self.textBox1.Text

    def _InitializeComponent(self):
        self.textBox1 = TextBox()
        self.label1 = Label()
        # 
        # textBox1
        # 
        self.textBox1.Location = Point(59, 62)
        self.textBox1.Name = "textBox1"
        self.textBox1.Size = Size(178, 20)
        self.textBox1.TabIndex = 0
        # 
        # label1
        # 
        self.label1.AutoSize = True
        self.label1.Location = Point(98, 106)
        self.label1.Name = "label1"
        self.label1.Size = Size(35, 13)
        self.label1.TabIndex = 1
        self.label1.Text = "label1"
        # 
        # Form1
        # 
        self.Size = Size(305, 162)
        self.Controls.Add(self.label1)
        self.Controls.Add(self.textBox1)
        self.Name = "Form1"
        self.Text = "TextBox"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
