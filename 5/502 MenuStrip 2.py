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

        self.newItem = ToolStripMenuItem("Создать")
        self.newItem.Checked = True
        self.newItem.CheckOnClick = True
        self.fileItem.DropDownItems.Add(self.newItem)

        self.saveItem = ToolStripMenuItem("Сохранить")
        self.saveItem.Checked = True
        self.saveItem.CheckOnClick = True
        self.saveItem.CheckedChanged += self.menuItem_CheckedChanged

        self.fileItem.DropDownItems.Add(self.saveItem)

        self.menuStrip1.Items.Add(self.fileItem)

    def menuItem_CheckedChanged(self, sender, EventArgs):
        self.menuItem = sender
        if self.menuItem.CheckState == CheckState.Checked:
            MessageBox.Show("Отмечен")
        elif self.menuItem.CheckState == CheckState.Unchecked:
            MessageBox.Show("Отметка снята")

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
