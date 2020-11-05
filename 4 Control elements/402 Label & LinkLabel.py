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
        self._initialize_components()
        # задаем обработчик события
        self.linkLabel1.LinkClicked += self.linkLabel1_LinkClicked

    def _initialize_components(self):
        self.label1 = Label()
        self.linkLabel1 = LinkLabel()

        # label1
        self.label1.AutoSize = True
        self.label1.Location = Point(30, 93.5)
        self.label1.Name = "label1"
        self.label1.Size = Size(22, 13)
        self.label1.TabIndex = 0
        self.label1.Text = "Переход по ссылке"

        # linkLabel1
        self.linkLabel1.AutoSize = True
        self.linkLabel1.Location = Point(150, 93.5)
        self.linkLabel1.Name = "linkLabel1"
        self.linkLabel1.Size = Size(95, 13)
        self.linkLabel1.TabIndex = 1
        self.linkLabel1.TabStop = True
        self.linkLabel1.Text = "https://t.me/stepik_bim"

        # Form1
        self.Size = Size(300, 200)
        self.Controls.Add(self.linkLabel1)
        self.Controls.Add(self.label1)
        self.Name = "Form1"
        self.Text = "Label & LinkLabel"

    def linkLabel1_LinkClicked(self, sender, event_args):
        System.Diagnostics.Process.Start("https://t.me/stepik_bim")


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
