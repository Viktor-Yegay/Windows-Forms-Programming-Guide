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

    def checkBox_CheckedChanged(self, sender, EventArgs):
        checkBox = sender # приводим отправителя к элементу типа CheckBox
        if checkBox.Checked == True:
            MessageBox.Show("Флажок " + checkBox.Text + "  теперь отмечен")
        else:
            MessageBox.Show("Флажок " + checkBox.Text + "  теперь не отмечен")

    def _InitializeComponent(self):
        self.groupBox1 = GroupBox()
        self.checkBox1 = CheckBox()
        self.checkBox2 = CheckBox()
        self.checkBox3 = CheckBox()
        # 
        # groupBox1
        # 
        self.groupBox1.Controls.Add(self.checkBox3)
        self.groupBox1.Controls.Add(self.checkBox2)
        self.groupBox1.Controls.Add(self.checkBox1)
        self.groupBox1.Location = Point(43, 32)
        self.groupBox1.Name = "groupBox1"
        self.groupBox1.Size = Size(200, 100)
        self.groupBox1.TabIndex = 0
        self.groupBox1.TabStop = False
        self.groupBox1.Text = "Свойство CheckState"
        # 
        # checkBox1
        # 
        self.checkBox1.AutoSize = True
        self.checkBox1.Location = Point(7, 20)
        self.checkBox1.Name = "checkBox1"
        self.checkBox1.Size = Size(69, 17)
        self.checkBox1.TabIndex = 0
        self.checkBox1.Text = "Checked"
        self.checkBox1.UseVisualStyleBackColor = True
        self.checkBox1.CheckedChanged += System.EventHandler(self.checkBox_CheckedChanged)
        # 
        # checkBox2
        # 
        self.checkBox2.AutoSize = True
        self.checkBox2.Location = Point(7, 44)
        self.checkBox2.Name = "checkBox2"
        self.checkBox2.Size = Size(90, 17)
        self.checkBox2.TabIndex = 1
        self.checkBox2.Text = "Indeterminate"
        self.checkBox2.UseVisualStyleBackColor = True
        self.checkBox2.CheckedChanged += System.EventHandler(self.checkBox_CheckedChanged)
        # 
        # checkBox3
        # 
        self.checkBox3.AutoSize = True
        self.checkBox3.Location = Point(7, 68)
        self.checkBox3.Name = "checkBox3"
        self.checkBox3.Size = Size(82, 17)
        self.checkBox3.TabIndex = 2
        self.checkBox3.Text = "Unckecked"
        self.checkBox3.UseVisualStyleBackColor = True
        self.checkBox3.CheckedChanged += System.EventHandler(self.checkBox_CheckedChanged)
        # 
        # Form1
        # 
        self.Size = System.Drawing.Size(305, 200)
        self.Controls.Add(self.groupBox1)
        self.Name = "Form1"
        self.Text = "CheckBox"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
