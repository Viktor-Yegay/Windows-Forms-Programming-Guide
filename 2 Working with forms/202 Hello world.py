# -*- coding: utf-8 -*-
from os import path

import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import *
from System.Windows.Forms import *


class TestWindow(Form):
    def __init__(self):
        self.Name = 'Form1'
        self.Text = 'Hello world'
        self.Size = Size(300, 300)

        self.FormBorderStyle = FormBorderStyle.Fixed3D

        self.CenterToScreen()

        parent_dir = path.dirname(path.abspath(__file__))
        self.BackgroundImage = Image.FromFile(parent_dir + '\\' + 'image.jpg')
        self.BackgroundImageLayout = ImageLayout.Center

        self._initialize_components()

    def _initialize_components(self):
        self._btn_1 = Button()
        self._btn_1.Location = Point(104, 200)
        self._btn_1.Name = 'button1'
        self._btn_1.Size = Size(75, 23)
        self._btn_1.TabIndex = 0
        self._btn_1.Text = 'button1'
        self._btn_1.UseVisualStyleBackColor = True
        self._btn_1.Parent = self
        self._btn_1.Click += self._button_click

    def _button_click(self, sender, event_args):
        MessageBox.Show("Привет!")


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
