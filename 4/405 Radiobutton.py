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

    def radioButton_CheckedChanged(self, sender, EventArgs):
        # приводим отправителя к элементу типа RadioButton
        radioButton = sender
        if radioButton.Checked:
            MessageBox.Show("Вы выбрали " + radioButton.Text)

    def _InitializeComponent(self):
        self.groupBox1 = GroupBox()
        self.radioButton1 = RadioButton()
        self.radioButton2 = RadioButton()
        self.radioButton3 = RadioButton()
        self.radioButton4 = RadioButton()
        # 
        # groupBox1
        # 
        self.groupBox1.Controls.Add(self.radioButton4)
        self.groupBox1.Controls.Add(self.radioButton3)
        self.groupBox1.Controls.Add(self.radioButton2)
        self.groupBox1.Controls.Add(self.radioButton1)
        self.groupBox1.Location = Point(43, 32)
        self.groupBox1.Name = "groupBox1"
        self.groupBox1.Size = Size(200, 118)
        self.groupBox1.TabIndex = 0
        self.groupBox1.TabStop = False
        self.groupBox1.Text = "Языки программирования"
        # 
        # radioButton1
        # 
        self.radioButton1.AutoSize = True
        self.radioButton1.Location = Point(7, 20)
        self.radioButton1.Name = "radioButton1"
        self.radioButton1.Size = Size(39, 17)
        self.radioButton1.TabIndex = 0
        self.radioButton1.TabStop = True
        self.radioButton1.Text = "C#"
        self.radioButton1.UseVisualStyleBackColor = True
        self.radioButton1.CheckedChanged += System.EventHandler(self.radioButton_CheckedChanged)
        # 
        # radioButton2
        # 
        self.radioButton2.AutoSize = True
        self.radioButton2.Location = Point(7, 44)
        self.radioButton2.Name = "radioButton2"
        self.radioButton2.Size = Size(56, 17)
        self.radioButton2.TabIndex = 1
        self.radioButton2.TabStop = True
        self.radioButton2.Text = "C/C++"
        self.radioButton2.UseVisualStyleBackColor = True
        self.radioButton2.CheckedChanged += System.EventHandler(self.radioButton_CheckedChanged)
        # 
        # radioButton3
        # 
        self.radioButton3.AutoSize = True
        self.radioButton3.Location = Point(7, 68)
        self.radioButton3.Name = "radioButton3"
        self.radioButton3.Size = Size(64, 17)
        self.radioButton3.TabIndex = 2
        self.radioButton3.TabStop = True
        self.radioButton3.Text = "VB.NET"
        self.radioButton3.UseVisualStyleBackColor = True
        self.radioButton3.CheckedChanged += System.EventHandler(self.radioButton_CheckedChanged)
        # 
        # radioButton4
        # 
        self.radioButton4.AutoSize = True
        self.radioButton4.Location = Point(7, 92)
        self.radioButton4.Name = "radioButton4"
        self.radioButton4.Size = Size(48, 17)
        self.radioButton4.TabIndex = 3
        self.radioButton4.TabStop = True
        self.radioButton4.Text = "Java"
        self.radioButton4.UseVisualStyleBackColor = True
        self.radioButton4.CheckedChanged += System.EventHandler(self.radioButton_CheckedChanged)
        # 
        # Form1
        # 
        self.Size = Size(305, 198)
        self.Controls.Add(self.groupBox1)
        self.Name = "Form1"
        self.Text = "Radiobutton"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
