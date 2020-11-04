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
        self.button1.Click += self.button1_Click
        # расширенное окно для выбора цвета
        self.colorDialog1.FullOpen = True
        # установка начального цвета для colorDialog
        self.colorDialog1.Color = self.BackColor

    def button1_Click(self, sender, EventArgs):
        if self.colorDialog1.ShowDialog() == DialogResult.Cancel:
            return
        # установка цвета формы
        self.BackColor = self.colorDialog1.Color

    def _InitializeComponent(self):
        self.button1 = Button()
        self.colorDialog1 = ColorDialog()
        #
        # button1
        #
        self.button1.Location = Point(96, 89)
        self.button1.Name = "button1"
        self.button1.Size = Size(75, 23)
        self.button1.TabIndex = 0
        self.button1.Text = "button1"
        self.button1.UseVisualStyleBackColor = True
        #
        # Form1
        #
        self.Size = Size(262, 224)
        self.Controls.Add(self.button1)
        self.Name = "Form1"
        self.Text = "ColorDialog"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
    MessageBox.Show("В C# перекрашивается только форма")
