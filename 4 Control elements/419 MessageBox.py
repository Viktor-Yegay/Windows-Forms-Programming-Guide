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

    def button1_Click(self, sender, EventArgs):
        result = MessageBox.Show(
            "Окрасить кнопку в красный цвет?",
            "Сообщение",
            MessageBoxButtons.YesNo,
            MessageBoxIcon.Information,
            MessageBoxDefaultButton.Button1,
            MessageBoxOptions.DefaultDesktopOnly)

        if result == DialogResult.Yes:
            self.button1.BackColor = Color.Red

        self.TopMost = True

        # MessageBox.Show(
        # "Выберите один из вариантов",
        # "Сообщение",
        # MessageBoxButtons.YesNo,
        # MessageBoxIcon.Information,
        # MessageBoxDefaultButton.Button1,
        # MessageBoxOptions.DefaultDesktopOnly)

    def _InitializeComponent(self):

        self.button1 = Button()
        #
        # button1
        #
        self.button1.Location = Point(68, 80)
        self.button1.Name = "button1"
        self.button1.Size = Size(75, 23)
        self.button1.TabIndex = 0
        self.button1.Text = "button1"
        self.button1.UseVisualStyleBackColor = True
        #
        # Form1
        #
        self.tSize = Size(248, 566)
        self.Controls.Add(self.button1)
        self.Name = "Form1"
        self.Text = "MessageBox"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
