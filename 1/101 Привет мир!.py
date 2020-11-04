# -*- coding: utf-8 -*-
import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import *
from System.Windows.Forms import *


class TestWindow(Form):
    def __init__(self):
        self.Name = 'Form1'
        self.Text = 'Привет мир!'
        self.Size = Size(284, 261)
        self._initialize_components()

    def _initialize_components(self):
        self._btn_1 = Button()
        self._btn_1.Location = Point(104, 113)
        self._btn_1.Name = 'button1'
        self._btn_1.Size = Size(75, 23)
        self._btn_1.TabIndex = 0
        self._btn_1.Text = 'button1'
        self._btn_1.UseVisualStyleBackColor = True
        self._btn_1.Parent = self
        self._btn_1.Click += self._button_click

    def _button_click(self, sender, event_args):
        MessageBox.Show("Привет")


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
