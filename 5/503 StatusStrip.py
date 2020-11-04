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
        # self.dateLabel = ToolStripLabel()
        # self.timeLabel = ToolStripLabel()
        # self.infoLabel = ToolStripLabel()
        # self.timer = Timer()

        self._InitializeComponent()

        self.infoLabel = ToolStripLabel()
        self.infoLabel.Text = "Текущие дата и время:"
        self.dateLabel = ToolStripLabel()
        self.timeLabel = ToolStripLabel()

        self.statusStrip1.Items.Add(self.infoLabel)
        self.statusStrip1.Items.Add(self.dateLabel)
        self.statusStrip1.Items.Add(self.timeLabel)

        self.timer = Timer()
        self.timer.Interval = 1000
        self.timer.Tick += self.timer_Tick
        self.timer.Start()

    def timer_Tick(self, sender, EventArgs):
        self.dateLabel.Text = System.DateTime.Now.ToLongDateString()
        self.timeLabel.Text = System.DateTime.Now.ToLongTimeString()

    def _InitializeComponent(self):
        self.statusStrip1 = StatusStrip()
        # 
        # statusStrip1
        # 
        self.statusStrip1.Location = Point(0, 698)
        self.statusStrip1.Name = "statusStrip1"
        self.statusStrip1.Size = Size(447, 22)
        self.statusStrip1.TabIndex = 0
        self.statusStrip1.Text = "statusStrip1"
        # 
        # Form1
        # 
        self.Size = Size(447, 720)
        self.Controls.Add(self.statusStrip1)
        self.Name = "Form1"
        self.Text = "StatusStrip"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
