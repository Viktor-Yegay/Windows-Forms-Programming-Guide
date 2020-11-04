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

        self.saveItem = ToolStripMenuItem("Сохранить")
        self.saveItem.Checked = True
        self.saveItem.CheckOnClick = True
        self.saveItem.Click += self.saveItem_Click
        self.saveItem.ShortcutKeys = Keys.Control | Keys.P

        self.fileItem.DropDownItems.Add(self.saveItem)
        self.menuStrip1.Items.Add(self.fileItem)

    def saveItem_Click(self, sender, EventArgs):
        MessageBox.Show("Сохранение")

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
