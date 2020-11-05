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
        self.koef = 1
        self._InitializeComponent()

        self.Width = 400
        self.button1.Width = 40
        self.button1.Left = 40
        self.button1.Text = ""
        self.button1.BackColor = Color.Aqua

        self.timer1.Interval = 500 # 500 миллисекунд
        self.timer1.Enabled = True
        self.button1.Click += self.button1_Click
        self.timer1.Tick += self.timer1_Tick

    # обработчик события Tick таймера
    def timer1_Tick(self, sender, EventArgs):
        if self.button1.Left == (self.Width - self.button1.Width - 10):
            self.koef = -1
        elif self.button1.Left == 0:
            self.koef = 1
        self.button1.Left += 10 * self.koef

    # обработчик нажатия на кнопку
    def button1_Click(self, sender, EventArgs):
        if self.timer1.Enabled == True:
            self.timer1.Stop()
        else:
            self.timer1.Start()

    def _InitializeComponent(self):
        self.components = System.ComponentModel.Container()
        self.timer1 = Timer(self.components)
        self.button1 = Button()
        #
        # button1
        #
        self.button1.Location = Point(92, 74)
        self.button1.Name = "button1"
        self.button1.Size = Size(75, 23)
        self.button1.TabIndex = 0
        self.button1.Text = "button1"
        self.button1.UseVisualStyleBackColor = True
        #
        # Form1
        #
        self.Size = Size(278, 452)
        self.Controls.Add(self.button1)
        self.Name = "Form1"
        self.Text = "Timer"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
