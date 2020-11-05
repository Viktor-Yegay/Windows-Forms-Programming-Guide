# -*- coding: utf-8 -*-
import clr
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System import *
from System.Drawing import *
from System.Windows.Forms import *


class TestWindow(Form):
    def __init__(self):
        self._InitializeComponent()
        countries = Array[object](["Бразилия", "Аргентина", "Чили", "Уругвай", "Колумбия"])
        self.listBox1.Items.AddRange(countries)

        self.listBox1.SelectedIndexChanged += self.listBox1_SelectedIndexChanged

    def listBox1_SelectedIndexChanged(self, sender, EventArgs):
        selectedCountry = self.listBox1.SelectedItem.ToString()
        MessageBox.Show(selectedCountry)

    def _InitializeComponent(self):
        self.listBox1 = ListBox()
        # 
        # listBox1
        # 
        self.listBox1.FormattingEnabled = True
        self.listBox1.Location = Point(54, 72)
        self.listBox1.Name = "listBox1"
        self.listBox1.Size = Size(149, 134)
        self.listBox1.TabIndex = 0
        # 
        # Form1
        # 
        self.tSize = Size(305, 287)
        self.Controls.Add(self.listBox1)
        self.Name = "Form1"
        self.Text = "ListBox"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
