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
        self.checkedListBox2 = CheckedListBox()
        self.label1 = Label()
        self.label2 = Label()
        # 
        # checkedListBox1
        # 
        self.checkedListBox1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left
        self.checkedListBox1.CheckOnClick = True
        self.checkedListBox1.FormattingEnabled = True
        self.checkedListBox1.Items.AddRange(Array[object]([
            "C#",
            "C/C++"]))
        self.checkedListBox1.Location = Point(12, 42)
        self.checkedListBox1.Name = "checkedListBox1"
        self.checkedListBox1.Size = Size(187, 244)
        self.checkedListBox1.TabIndex = 0
        # 
        # checkedListBox2
        # 
        self.checkedListBox2.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right
        self.checkedListBox2.CheckOnClick = True
        self.checkedListBox2.FormattingEnabled = True
        self.checkedListBox2.Items.AddRange(Array[object]([
            "C#",
            "C/C++",
            "Java",
            "VB.NET",
            "JavaScript",
            "PHP",
            "Object-C",
            "Python",
            "Ruby",
            "Delphi",
            "Swift",
            "F#"]))
        self.checkedListBox2.Location = Point(205, 42)
        self.checkedListBox2.MultiColumn = True
        self.checkedListBox2.Name = "checkedListBox2"
        self.checkedListBox2.Size = Size(183, 244)
        self.checkedListBox2.TabIndex = 1
        # 
        # label1
        # 
        self.label1.AutoSize = True
        self.label1.Location = Point(57, 9)
        self.label1.Name = "label1"
        self.label1.Size = Size(95, 13)
        self.label1.TabIndex = 2
        self.label1.Text = "MultiColumn=False"
        # 
        # label2
        # 
        self.label2.AutoSize = True
        self.label2.Location = Point(252, 9)
        self.label2.Name = "label2"
        self.label2.Size = Size(92, 13)
        self.label2.TabIndex = 3
        self.label2.Text = "MultiColumn=True"
        # 
        # Form1
        # 
        self.ClientSize = Size(400, 300)
        self.Controls.Add(self.label2)
        self.Controls.Add(self.label1)
        self.Controls.Add(self.checkedListBox2)
        self.Controls.Add(self.checkedListBox1)
        self.Name = "Form1"
        self.Text = "Элемент CheckedListBox"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
