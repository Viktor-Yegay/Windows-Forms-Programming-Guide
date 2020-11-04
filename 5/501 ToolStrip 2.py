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
        self.clearBtn = ToolStripButton()
        self.clearBtn.Text = "Поиск"
        self.clearBtn.DisplayStyle = ToolStripItemDisplayStyle.ImageAndText
        self.clearBtn.Image = Image.FromFile(r"F:\YandexDisk\Windows Forms Programming Guide\5\IronMan32x32.png")
        # добавляем на панель инструментов
        self.toolStrip1.Items.Add(self.clearBtn)

    def _InitializeComponent(self):
        self.toolStrip1 = ToolStrip()
        # 
        # toolStrip1
        # 
        self.toolStrip1.Location = Point(0, 0)
        self.toolStrip1.Name = "toolStrip1"
        self.toolStrip1.Size = Size(544, 25)
        self.toolStrip1.TabIndex = 0
        self.toolStrip1.Text = "toolStrip1"
        # 
        # Form1
        # 
        self.Size = Size(544, 439)
        self.Controls.Add(self.toolStrip1)
        self.Name = "Form1"
        self.Text = "ToolStrip"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
