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
        self.fileItem = ToolStripMenuItem("Файл")

        self.fileItem.DropDownItems.Add("Создать")
        self.fileItem.DropDownItems.Add(ToolStripMenuItem("Сохранить"))

        self.menuStrip1.Items.Add(self.fileItem)

        self.aboutItem = ToolStripMenuItem("О программе")
        self.aboutItem.Click += self.aboutItem_Click
        self.menuStrip1.Items.Add(self.aboutItem)

    def aboutItem_Click(self, sender, EventArgs):
        MessageBox.Show("О программе")

    def _InitializeComponent(self):
        self.menuStrip1 = MenuStrip()
        # 
        # menuStrip1
        # 
        self.menuStrip1.Location = Point(0, 0)
        self.menuStrip1.Name = "menuStrip1"
        self.menuStrip1.Size = Size(447, 24)
        self.menuStrip1.TabIndex = 0
        self.menuStrip1.Text = "menuStrip1"
        # 
        # Form1
        # 
        self.Size = Size(447, 720)
        self.Controls.Add(self.menuStrip1)
        self.Name = "Form1"
        self.Text = "MenuStrip"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
