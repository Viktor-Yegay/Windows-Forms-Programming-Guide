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

        self.comboBox1.SelectedIndexChanged += self.comboBox1_SelectedIndexChanged

    def comboBox1_SelectedIndexChanged(self, sender, EventArgs):
        selectedState = self.comboBox1.SelectedItem.ToString()
        MessageBox.Show(selectedState)

    def _InitializeComponent(self):
        self.comboBox1 = ComboBox()
        # 
        # comboBox1
        # 
        self.comboBox1.FormattingEnabled = True
        self.comboBox1.Items.AddRange(Array[object]([
            "Бразилия",
            "Аргентина",
            "Чили",
            "Венесуэла",
            "Колумбия"]))
        self.comboBox1.Location = Point(77, 82)
        self.comboBox1.Name = "comboBox1"
        self.comboBox1.Size = Size(121, 21)
        self.comboBox1.TabIndex = 0
        # 
        # Form1
        # 
        self.Size = Size(305, 287)
        self.Controls.Add(self.comboBox1)
        self.Name = "Form1"
        self.Text = "ComboBox"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
