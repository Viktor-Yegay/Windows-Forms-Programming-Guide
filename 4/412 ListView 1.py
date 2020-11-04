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
        self._InitializeComponent()

    def _InitializeComponent(self):
        self.listViewItem1 = ListViewItem("Смартфоны")
        self.listViewItem2 = ListViewItem("Планшеты")
        self.listView1 = ListView()
        # 
        # listView1
        # 
        self.listView1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right
        self.listView1.CheckBoxes = True
        self.listView1.HideSelection = False
        self.listViewItem1.Checked = True
        self.listViewItem1.StateImageIndex = 1
        self.listViewItem2.Checked = True
        self.listViewItem2.StateImageIndex = 1
        self.listView1.Items.AddRange(Array[ListViewItem]([
            self.listViewItem1,
            self.listViewItem2]))
        self.listView1.Location = Point(12, 12)
        self.listView1.Name = "listView1"
        self.listView1.Size = Size(276, 276)
        self.listView1.TabIndex = 0
        self.listView1.UseCompatibleStateImageBehavior = False
        self.listView1.View = View.List
        # 
        # Form1
        # 
        self.ClientSize = Size(300, 300)
        self.Controls.Add(self.listView1)
        self.Name = "Form1"
        self.Text = "ListView"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
