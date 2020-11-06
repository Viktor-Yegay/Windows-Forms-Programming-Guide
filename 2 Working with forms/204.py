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
        self.Text = 'Привет мир!'
        self.Size = Size(260, 280)
        self.FormBorderStyle = FormBorderStyle.Fixed3D
        self.CenterToScreen()
        parent_dir = path.dirname(path.abspath(__file__))
        self.BackgroundImage = Image.FromFile(parent_dir + '\\' + 'image.jpg')
        self.BackgroundImageLayout = ImageLayout.Center
        self.BackColor = Color.Aquamarine
        self.Load += self.Form1_Load

        self._initialize_components()

    def _initialize_components(self):
        self._btn_1 = Button()
        self._btn_1.Location = Point(92.5, 200)
        self._btn_1.Name = 'button1'
        self._btn_1.Size = Size(75, 23)
        self._btn_1.TabIndex = 0
        self._btn_1.Text = 'button1'
        self._btn_1.UseVisualStyleBackColor = True
        self._btn_1.Parent = self
        self._btn_1.Click += self._button_click

    def _button_click(self, sender, event_args):
        MessageBox.Show("Доброго времени суток")

    def Form1_Load(self, sender, event_args):
        self.BackColor = Color.Yellow


class Form2(Form):
    def __init__(self, f):
        f.BackColor = Color.Yellow
        self.Name = 'Form2'
        self.Text = 'Пока мир!'
        self.Size = Size(260, 280)
        self.FormBorderStyle = FormBorderStyle.Fixed3D
        self.CenterToScreen()
        parent_dir = path.dirname(path.abspath(__file__))
        self.BackgroundImage = Image.FromFile(parent_dir + '\\' + 'image.jpg')
        self.BackgroundImageLayout = ImageLayout.Center
        self.BackColor = Color.Aquamarine


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
