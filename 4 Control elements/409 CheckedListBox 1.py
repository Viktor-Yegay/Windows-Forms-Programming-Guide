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
        self._initialize_components()

    def _initialize_components(self):
        self.checkedListBox1 = CheckedListBox()
        # 
        # checkedListBox1
        # 
        self.checkedListBox1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right
        self.checkedListBox1.CheckOnClick = True
        self.checkedListBox1.FormattingEnabled = True
        self.checkedListBox1.Items.AddRange(Array[object]([
            "Бразилия",
            "Аргентина",
            "Чили",
            "Уругвай",
            "Колумбия"]))
        self.checkedListBox1.Location = Point(12, 12)
        self.checkedListBox1.Name = "checkedListBox1"
        self.checkedListBox1.Size = Size(176, 274)
        self.checkedListBox1.TabIndex = 0
        # 
        # Form1
        # 
        # self.Size = Size(250, 330)
        self.ClientSize = Size(200, 300)
        self.Controls.Add(self.checkedListBox1)
        self.Name = "Form1"
        self.Text = "Элемент CheckedListBox"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
