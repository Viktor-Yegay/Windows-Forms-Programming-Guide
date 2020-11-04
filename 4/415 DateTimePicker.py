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
        self.dateTimePicker1.Format = DateTimePickerFormat.Time
        self.dateTimePicker1.ValueChanged += self.dateTimePicker1_ValueChanged

    def dateTimePicker1_ValueChanged(self, sender, EventArgs):
        self.label1.Text = "Вы выбрали: {0}".format(self.dateTimePicker1.Value.ToLongTimeString())
        # self.label1.Text = "Вы выбрали: {0}".format(self.dateTimePicker1.Text)

    def _InitializeComponent(self):
        self.dateTimePicker1 = DateTimePicker()
        self.label1 = Label()
        #
        # dateTimePicker1
        #
        self.dateTimePicker1.Location = Point(40, 108)
        self.dateTimePicker1.Name = "dateTimePicker1"
        self.dateTimePicker1.Size = Size(200, 20)
        self.dateTimePicker1.TabIndex = 0
        #
        # label1
        #
        self.label1.AutoSize = True
        self.label1.Location = Point(87, 64)
        self.label1.Name = "label1"
        self.label1.Size = Size(35, 13)
        self.label1.TabIndex = 1
        self.label1.Text = "label1"
        #
        # Form1
        #
        self.Size = Size(292, 452)
        self.Controls.Add(self.label1)
        self.Controls.Add(self.dateTimePicker1)
        self.Name = "Form1"
        self.Text = "DateTimePicker"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
