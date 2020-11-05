# -*- coding: utf-8 -*-
import clr
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

# import System
from System import *
from System.Drawing import *
from System.Windows.Forms import *


class TestWindow(Form):
    def __init__(self):
        self._InitializeComponent()
        self.source = AutoCompleteStringCollection()
        # 1-ый вариант
        # self.source.Add("Кузнецов")
        # self.source.Add("Иванов")
        # self.source.Add("Петров")
        # self.source.Add("Кустов")
        # 2-ой вариант
        # self.source.AddRange(System.Array[System.String](["Кузнецов", "Иванов", "Петров", "Кустов"]))
        self.source.AddRange(Array[String]([
            "Кузнецов",
            "Иванов",
            "Петров",
            "Кустов"
            ]))
        self.textBox1.AutoCompleteCustomSource = self.source
        self.textBox1.AutoCompleteMode = AutoCompleteMode.SuggestAppend
        self.textBox1.AutoCompleteSource = AutoCompleteSource.CustomSource

    def _InitializeComponent(self):
        self.textBox1 = TextBox()
        # 
        # textBox1
        # 
        self.textBox1.Location = Point(59, 62)
        self.textBox1.Name = "textBox1"
        self.textBox1.Size = Size(178, 20)
        self.textBox1.TabIndex = 0
        # 
        # Form1
        # 
        self.Size = Size(305, 162)
        self.Controls.Add(self.textBox1)
        self.Name = "Form1"
        self.Text = "TextBox"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
